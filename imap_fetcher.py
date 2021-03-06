"""
Copyright (c) Pier-Luc Brault
plbrault@gmail.com

This file is part of Imap2Gmail.
Please read LICENSE.txt for complete copyright and license notice.
"""

import imaplib
import email
import re

class ImapFetcher:
    
    _MAILBOX_LIST_ITEM_PATTERN = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
    
    _connection = None
    
    def open_connection(self, host, port, username, password, ssl=False):
        if self._connection != None:
            self.close_connection()
        self._connection = imaplib.IMAP4_SSL(host, port) if ssl else imaplib.IMAP4(host, port)
        self._connection.login(username, password)
    
    def close_connection(self):
        self._connection.shutdown()
        self._connection = None
        
    def get_mailbox_list(self):
        mailbox_list = []
        for mailbox in self._connection.list()[1]:
            if type(mailbox) == bytes:
                mailbox = mailbox.decode("utf-8")
            name = self._MAILBOX_LIST_ITEM_PATTERN.match(mailbox).groups()[2]
            mailbox_list.append(name)
        return mailbox_list
    
    def fetch_message(self, message_id):
        raw_message = self._connection.fetch(message_id, '(RFC822)')[1][0][1]
        message = email.message_from_bytes(raw_message)
        try:
            message.set_charset("utf-8")
        except:
            pass
        return message
    
    def fetch_new_messages(self):
        messages = []
        for mailbox in self.get_mailbox_list():
            self._connection.select(mailbox)
            new_message_ids = self._connection.search(None, 'UNSEEN')[1][0].split(b' ')
            for message_id in new_message_ids:
                if message_id.isdigit():
                    messages.append(self.fetch_message(message_id))
        return messages
