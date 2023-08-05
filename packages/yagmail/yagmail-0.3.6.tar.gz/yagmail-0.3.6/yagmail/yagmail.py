import os
import keyring
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.encoders
import mimetypes

import requests

from .error import YagConnectionClosed
from .error import YagAddressError

try:
    import lxml.html
except ImportError:
    pass 

class Connect():
    """ Connection is the class that contains the smtp"""

    def __init__(self, user=None, password=None, host='smtp.gmail.com', port='587',
                 starttls=True, set_debuglevel=0, **kwargs):
        if user is None:
            user = self._findUseruserHome()
        self.user, self.userName = self._makeAddrAliasuser(user)
        self.isClosed = None
        self.host = host
        self.port = port
        self.starttls = starttls
        self.debuglevel = set_debuglevel
        self.kwargs = kwargs
        self.login(password)
        self.cache = {}

    def send(self, to = None, subject = None, contents = None, attachments = None, cc = None, bcc = None,
             previewOnly=False, useCache=False):
        """ Use this to send an email with gmail"""
        addresses = self._resolveAddresses(to, cc, bcc) 
        msg = self._prepareMsg(addresses, subject, contents, attachments, useCache)
        if previewOnly:
            return addresses, msg.as_string()
        else:
            return self.smtp.sendmail(self.user, addresses['recipients'], msg.as_string())

    def close(self):
        self.isClosed = True
        self.smtp.quit()

    def login(self, password):
        self.smtp = smtplib.SMTP(self.host, self.port, **self.kwargs)
        self.smtp.set_debuglevel(self.debuglevel)
        if self.starttls is not None:
            self.smtp.ehlo()
            if self.starttls:
                self.smtp.starttls()
            else:
                self.smtp.starttls(**self.starttls)
            self.smtp.ehlo()
        if password is None:
            password = keyring.get_password('yagmail', self.user)
            if '@' not in self.user:
                self.user += '@gmail.com'
            if password is None:
                password = keyring.get_password('yagmail', self.user)
            if password is None:
                import getpass
                password = getpass.getpass('Password for <{}>: '.format(self.user))
                answer = ''
                try: 
                    input = raw_input 
                except NameError: 
                    pass
                while answer != 'y' and answer != 'n':
                    answer = input('Save username and password in keyring? [y/n]: ').strip()
                if answer == 'y':    
                    register(self.user, password)    
        self.smtp.login(self.user, password)
        self.isClosed = False

    def _resolveAddresses(self, to, cc, bcc):
        addresses = {'recipients': []}
        if to is not None:
            self._makeAddrAliasTarget(to, addresses, 'to')
        elif cc is not None and bcc is not None:
            self._makeAddrAliasTarget([self.user, self.userName], addresses, 'to')
        else:
            addresses['recipients'].append(self.user)
        if cc is not None:
            self._makeAddrAliasTarget(cc, addresses, 'cc')
        if bcc is not None:
            self._makeAddrAliasTarget(bcc, addresses, 'bcc')
        return addresses

    def _prepareMsg(self, addresses, subject, contents, attachments, useCache):
        if self.isClosed:
            raise YagConnectionClosed('Login required again')
        hasEmbeddedImage, contentObjects = self._prepareContents(contents, useCache)
        msg = MIMEMultipart()
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)
        self._addSubject(msg, subject)
        self._addRecipients(msg, addresses)
        if hasEmbeddedImage:
            msg.preamble = "You need a MIME enabled mail reader to see this message."
        if contents is not None:    
            for contentObject, contentString in zip(contentObjects, contents):
                if contentObject['main_type'] == 'image':
                    if isinstance(contentString, dict):
                        for x in contentString:
                            hashed_ref = contentString[x]
                    else:
                        hashed_ref = str(abs(hash(os.path.basename(contentString))))
                    msgImgText = MIMEText('<img src="cid:{}" title="{}"/>'.format(hashed_ref, hashed_ref), 'html')
                    contentObject['mimeObject'].add_header('Content-ID', '<{}>'.format(hashed_ref)) 
                    msgAlternative.attach(msgImgText) 
                    email.encoders.encode_base64(contentObject['mimeObject']) 
                msg.attach(contentObject['mimeObject'])
        if attachments or attachments is None:
            pass
        # attachments = self._prepareattachments(msg, attachments, useCache)
        return msg

    def _prepareattachments(self, msg, attachments, useCache=False):
        pass

    def _prepareContents(self, contents, useCache=False):
        mimeObjects = []
        hasEmbeddedImage = False
        if contents is not None:
            if isinstance(contents, str):
                contents = [contents]
            for content in contents:
                if useCache: 
                    if content not in self.cache:
                        contentObject = self._getMIMEObject(content)
                        self.cache[content] = contentObject
                    contentObject = self.cache[content]
                else:
                    contentObject = self._getMIMEObject(content)
                if contentObject['main_type'] == 'image': 
                    hasEmbeddedImage = True
                mimeObjects.append(contentObject)
        return hasEmbeddedImage, mimeObjects

    def _addRecipients(self, msg, addresses):
        msg['user'] = self.userName
        if 'To' in addresses:
            msg['To'] = addresses['To']
        else:
            msg['To'] = self.userName
        if 'cc' in addresses:
            msg['Cc'] = addresses['cc']
        if 'bcc' in addresses:
            msg['Bcc'] = addresses['bcc']

    def _findUseruserHome(self):
        home = os.path.expanduser("~")
        with open(home + '/.yagmail') as f:
            return f.read().strip()

    def _makeAddrAliasuser(self, x):
        if isinstance(x, str):
            return (x, x)
        if isinstance(x, dict):
            if len(x) == 1:
                return (list(x.keys())[0], list(x.values())[0])
        raise YagAddressError

    def _makeAddrAliasTarget(self, x, addresses, which):
        if isinstance(x, str):
            addresses['recipients'].append(x)
            addresses['To'] = x
            return addresses
        if isinstance(x, list) or isinstance(x, tuple):
            if not all([isinstance(k, str) for k in x]):
                raise YagAddressError
            addresses['recipients'].extend(x)
            addresses[which] = '; '.join(x)
            return addresses
        if isinstance(x, dict):
            addresses['recipients'].extend(x.keys())
            addresses[which] = '; '.join(x.values())
            return addresses
        raise YagAddressError

    def _addSubject(self, msg, Subject):
        if not Subject:
            return
        if isinstance(Subject, list):
            Subject = ' '.join(Subject)
        msg['Subject'] = Subject

    def _getMIMEObject(self, contentString):
        contentObject = {'mimeObject': None, 'encoding': None, 'main_type': None, 'sub_type': None} 
        if isinstance(contentString, dict):
            for x in contentString:
                contentString, contentName = x, contentString[x]
        else:
            contentName = os.path.basename(contentString)        
        if os.path.isfile(contentString):
            try:
                with open(contentString) as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(contentString, 'rb') as f:
                    content = f.read()
        else:
            try:
                r = requests.get(contentString)
                # pylint: disable=protected-access
                # Used to obtain the raw content of requests object
                content = r._content
                if 'content-type' in r.headers:
                    main_type, sub_type = r.headers['content-type'].split('/')
                    contentObject['main_type'] = main_type
                    contentObject['sub_type'] = sub_type
            except (IOError, ValueError, requests.exceptions.MissingSchema):
                contentObject['main_type'] = 'text'
                try:
                    html_tree = lxml.html.fromstring(contentString)
                    if html_tree.find('.//*') is not None or html_tree.tag != 'p':
                        contentObject['mimeObject'] = MIMEText(contentString, 'html')
                        contentObject['sub_type'] = 'html'
                    else:
                        contentObject['mimeObject'] = MIMEText(contentString)
                except NameError: 
                    contentObject['mimeObject'] = MIMEText(contentString) 
                if contentObject['sub_type'] is None:
                    contentObject['sub_type'] = 'plain'
                return contentObject

        if contentObject['main_type'] is None:
            content_type, content_encoding = mimetypes.guess_type(contentString)
            contentObject['encoding'] = content_encoding

            if content_type is not None:
                contentObject['main_type'], contentObject['sub_type'] = content_type.split('/')

        if contentObject['main_type'] is None or contentObject['encoding'] is not None:
            contentObject['main_type'] = 'application'
            contentObject['sub_type'] = 'octet-stream'

        mimeObject = MIMEBase(contentObject['main_type'], contentObject['sub_type'], name = contentName)
        mimeObject.set_payload(content) 
        contentObject['mimeObject'] = mimeObject
        return contentObject

    def __del__(self):
        self.close()


def register(username, password):
    """ Use this to add a new gmail account to your OS' keyring so it can be used in yagmail"""
    keyring.set_password('yagmail', username, password)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Send a (g)mail with yagmail.') 
    parser.add_argument('-to', '-t', help='Send an email to address "TO"', nargs='+') 
    parser.add_argument('-subject', '-s', help='Subject of email', nargs='+') 
    parser.add_argument('-contents', '-c', help='Contents to send', nargs='+') 
    parser.add_argument('-user', '-u', help='Username') 
    parser.add_argument('-password', '-p', help='Preferable to use keyring rather than password here') 
    args = parser.parse_args() 
    Connect(args.user, args.password).send(to = args.to, subject = args.subject, contents = args.contents)
    
    
