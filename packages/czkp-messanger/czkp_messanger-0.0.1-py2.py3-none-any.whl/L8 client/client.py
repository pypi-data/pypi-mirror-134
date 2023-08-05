"""
This module use for work messenger client.

Classes
-------
MessageHistory(eng.base)
    Extend parent and create model declarative style.
ContactList(eng.base)
    Extend parent and create model declarative style.
ClientVerifier(type)
    Extend parent metaclass for the ``Client`` class.
Client(metaclass=ClientVerifier)
    Client part of the messenger.
"""

import argparse
import json
import subprocess
import threading
import time
import re
from socket import socket, AF_INET, SOCK_STREAM
from hashlib import pbkdf2_hmac

from sqlalchemy import Column, String, Integer

from common.func import send_msg, get_msg
from common.settings import *
from log.conf.client_log_config import *
from decors import log, Log, login_required
from server import InitDb


eng = InitDb(DEFAULT_PATH_CLIENT)


class MessageHistory(eng.base):
    """
    This class extend parent and create model with declarative style.
    """

    __tablename__ = 'message_history'
    id = Column(Integer, primary_key=True)  #: ID, primary key.
    from_user = Column(String)  #: Column for from whom the message came.
    whom_user = Column(String)  #: Column to whom the message went.
    message = Column(String)  #: Column messages.

    def __init__(self, from_user, whom_user, message):
        """
        This class constructor uses for assigning a value to an attribute.

        Parameters
        ----------
        from_user
            Column for from whom the message came.
        whom_user
            Column to whom the message went.
        message
            Column messages.
        """
        self.from_user = from_user
        self.whom_user = whom_user
        self.message = message

    def __repr__(self):
        """
        This function returns a string representation of the object.

        Returns
        -------
        str
            Object message history.
        """
        return f'message history (from_user, whom_user, message): {self.from_user}, {self.whom_user}, {self.message}'


class ContactList(eng.base):
    """
    This class extend parent and create model with declarative style.
    """

    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True)  #: ID, primary key.
    client = Column(String)  #: Column for client username.
    contact = Column(String)  #: Column for client contact.

    def __init__(self, owner, contact):
        """
        This class constructor uses for assigning a value to an attribute.

        Parameters
        ----------
        client
            Column for client username.
        contact
            Column for client contact.
        """
        self.client = owner
        self.contact = contact

    def __repr__(self):
        """
        This function returns a string representation of the object.

        Returns
        -------
        str
            Client contact object.
        """
        return f'User: {self.client}, contact: {self.contact}'


class ClientVerifier(type):
    """
    This metaclass extends parent for class ``Client``.
    """

    def __call__(cls, *args, **kwargs):
        """
        This function checks on use ``accept`` and ``listen`` for sockets and TCP mode.

        Parameters
        ----------
        dis_out
            Output of the stdout stream client.py module.
        reg
            Regular expression of the search in ``dis_out``.
        reg_str
            Conversion ``list`` data type in ``str`` data type.
        reg_init
            Regular expression of the search in ``reg_str`` for search the required block of the call stack.
        cls.obj.connection()
            Call method ``connection`` class ``Client``.

        Returns
        -------
        ``Client`` class object
            For not to call ``connection`` method ``Client`` class when working in test mode.

        Raises
        ------
        ValueError
            When use ``accept`` and ``listen`` for sockets and TCP mode.
        """
        cls.obj = super().__call__(*args, **kwargs)
        dis_out = subprocess.run(['python', '-m', 'dis', 'client.py'], capture_output=True,
                                 universal_newlines=True).stdout
        reg = re.findall('.*', dis_out)
        reg_str = ''.join(reg)
        if dis_out != '':
            reg_init = re.findall(' <code object __init__.*?Disassembly of <code object', reg_str)[1]
            if len(re.findall('\(accept\)', dis_out)) > 0 or len(re.findall('\(listen\)', dis_out)) > 0:
                raise ValueError('Client not can use "accept" and "listen" for sockets')
            elif len(re.findall('\(SOCK_DGRAM\)', dis_out)) > 0 or \
                    len(re.findall('\(SOCK_RAW\)', dis_out)) > 0 or \
                    len(re.findall('\(SOCK_RDM\)', dis_out)) > 0 or \
                    len(re.findall('\(SOCK_SEQPACKET\)', dis_out)) > 0:
                raise ValueError('Socket must use TCP')
            elif len(re.findall('\(socket\)', reg_init)) > 0:
                raise ValueError('Socket can not running in "__init__"')
        if cls.obj.test:
            return cls
        else:
            cls.obj.connection()
        return cls


class Client(metaclass=ClientVerifier):
    """
    This class for work client part messenger.

    Methods
    -------
    connection
        Connect via socket to the messenger server.
    create_presence(ac_name, mode)
        Presence message in JIM format.
    filler(client_name, contacts)
        Add contacts in ``ContactList`` table.
    deleter(client_name, contacts)
        Delete list contacts in ``ContactList`` table.
    sender(sock, ac_name)
        Send messages to the messenger server.
    recipient(sock, ac_name)
        Receive messages from the messenger server.
    save_msg(ac_name, to, msg)
        Save message in ``MessageHistory`` table.
    create_message(ac_name, to, msg)
        Message for sends addressee.
    get_contacts(ac_name)
        List contacts.
    add_contact(ac_name, add_name)
        Add contact in ``ContactList`` table.
    del_contact(ac_name, del_name)
        Delete contact in ``ContactList`` table.
    check_client(ac_name, password)
        Checks existence client in ``Client`` table on messenger server.
    arg_parser
        Command line interface.
    """

    def __init__(self, test=False, login=None, password=None):
        """
        This class constructor for configuration of a class object.

        Parameters
        ----------
        test
            Tests mode.
        authorized
            User authorization is passed or not.
        queue
            Message exchange queue.
        salt
            The salt for hash password.
        logger
            Object logger for logging.
        par
            Command line interface object.
        name
            Converting a command line parameter string to object.
        serv_address
            Ip-address messenger server from command line.
        serv_port
            Port messenger server from command line.
        client_name
            Messenger server username from command line.
        password
            Messenger server password from command line.
        db
            Path to database from command line.
        message
            Text message from command line.
        to
            Whom the message from command line.
        append_contact
            Contact being added from command line.
        mode
            Client part messenger work mode from command line.
        console_add_contact
            Contact being added from console work mode client part messenger.
        console_del_contact
            Contact being delete from console work mode client part messenger.
        eng
            Connection object to database client part messenger.
        login
            Username passed to the class.
        logger.critical
            Record a message 'attempt to start client on ...' through a logger object at a critical level.
        sys.exit(1)
            Shutdown client part messenger.
        """
        self.test = test
        self.authorized = False
        self.queue = 0
        self.salt = ''
        self.logger = logging.getLogger('chat.client')
        self.par = self.arg_parser()
        self.name = self.par.parse_args()
        self.serv_address = self.name.a
        self.serv_port = self.name.p
        self.client_name = self.name.n
        self.password = self.name.s
        self.db = self.name.d
        self.message = self.name.m
        self.to = self.name.t
        self.append_contact = self.name.c
        self.mode = self.name.r
        self.console_add_contact = ''
        self.console_del_contact = ''
        self.eng = InitDb(self.db)
        if login:
            self.client_name = login
        if password:
            self.password = password
        if not self.client_name:
            self.client_name = input('Input client name: ')
        if not self.password:
            self.password = input('Input password: ')
        if self.serv_port < 1024 or self.serv_port > 65535:
            self.logger.critical(f'attempt to start client on server port < 1024 or > 65535')
            sys.exit(1)

    @Log()
    def connection(self):
        """
        This method connects to the messenger server using sockets.

        Parameters
        ----------
        socket
            Socket object with IPv4 protocol and type TCP-socket.
        s.connect
            Connect to server with ip-address ``serv_address`` and port ``serv_port``.
        logger.info
            Record a message 'client running on server address...' through a logger object at info level.
        send_msg
            Send presence message with username ``client_name`` and mode ``mode`` via ``s`` socket object.
        rt
            Create a separate thread with the ``recipient`` method work in it with arguments ``s`` and ``client_name``.
        rt.daemon
            Set up a demonic ``rt`` thread.
        rt.start()
            Start ``rt`` thread.
        sr
            Create a separate thread with the ``sender`` method work in it with arguments ``s`` and ``client_name``.
        sr.daemon
            Set up a demonic ``sr`` thread.
        sr.start()
            Start ``sr`` thread.
        sr.join()
            Threads will wait for the execution of the ``sr`` thread to complete.
        logger.critical
            Record a message 'client cannot decode message from server' through a logger object at critical level.
        """
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((self.serv_address, self.serv_port))
            logger.info(
                f'client running on server address / port, client name: {self.serv_address} / {self.serv_port}, '
                f'{self.client_name}')
            send_msg(s, self.create_presence(self.client_name, self.mode))
            try:
                rt = threading.Thread(target=self.recipient, args=(s, self.client_name))
                rt.daemon = True
                rt.start()
                sr = threading.Thread(target=self.sender, args=(s, self.client_name))
                sr.daemon = True
                sr.start()
                sr.join()
            except (ValueError, json.JSONDecodeError):
                logger.critical(f'client cannot decode message from server')

    @staticmethod
    @Log()
    def create_presence(ac_name='Guest', mode=DEFAULT_MODE):
        """
        This method creates a JIM format presence message.

        Parameters
        ----------
        presence
            Message presence of the JIM format.
        logger.info
            Record a message 'presence "{presence}" created' through a logger object at info level.

        Returns
        -------
        dict
            Presence message.
        """
        presence = {
            ACT: PRESENCE,
            TIME: time.time(),
            USER: {
                AC_NAME: ac_name
            },
            MODE: mode
        }
        logger.info(f'presence "{presence}" created')
        return presence

    @login_required
    @Log()
    def filler(self, client_name, contacts):
        """
        This method fills contacts in ``ContactList`` table.

        Parameters
        ----------
        eng.session.add
            Append ``client_name`` username ``contact`` contact in ``session`` session in ``ContactList`` table.
        eng.session.commit()
            Save do not saved data in ``session`` session.
        """
        for contact in contacts:
            self.eng.session.add(ContactList(client_name, contact))
        self.eng.session.commit()

    @login_required
    @Log()
    def deleter(self, client_name, contacts):
        """
        This method delete contacts in ``ContactList`` table.

        Parameters
        ----------
        eng.session.query(ContactList).filter_by
            Delete record in ``ContactList`` table with filtered ``client=client_name, contact=contact`` filter.
        eng.session.commit()
            Save do not saved data in ``session`` session.
        """
        for contact in contacts:
            self.eng.session.query(ContactList).filter_by(client=client_name, contact=contact).delete()
        self.eng.session.commit()

    @log
    def sender(self, sock, ac_name):
        """
        This method send JIM format messages to messenger server.

        Parameters
        ----------
        queue
            A variable used as a queue for client-server interaction.
        pass_hash
            Hash of the ``password`` in 'utf-8' encoding with algorithm 'sha512',  ``salt`` and 100000 repetitions.
        salted_hash
            Concatenation ``pass_hash`` hash and ``salt`` salt.
        authorized
            Set ``True`` value variable ``authorized`` when user authorization complete.
        client_name
            Username.
        new_contact
            Message JIM format for add contact.
        filler
            Add contacts from the ``append_contact`` list to the ``client_name`` client to the ``ContactList`` table.
        action
            The action letter entered by the user.
        to
            Enter by the addressee user.
        msg
            Enter by user the text message.
        jim_contacts
            JIM format message for getting contacts.
        console_add_contact
            Enter user contact for add in ``ContactList`` table.
        jim_add_contact
            Add contact in ``ContactList`` table with arguments ``ac_name`` username and ``console_add_contact``.
        console_del_contact
            Enter user contact for delete from ``ContactList`` table.
        jim_del_contact
            Delete contact from ``ContactList`` table with arguments ``ac_name`` username and ``console_del_contact``.
        logger.critical
            Record a message '"sender()" return exception {e}' through a logger object at critical level.
        """
        while True:
            if self.queue == 1:
                self.queue = 0
                pass_hash = pbkdf2_hmac('sha512', self.password.encode('utf-8'), bytes.fromhex(self.salt), 100000)
                salted_hash = pass_hash + bytes.fromhex(self.salt)
                send_msg(sock, self.check_client(self.client_name, salted_hash.hex()))
                while True:
                    if self.queue == 1:
                        self.queue = 0
                        self.authorized = True
                        print(f'User name: {ac_name}')
                        break
                    if self.queue == 3:
                        self.queue = 0
                        self.client_name = ''
                        break
                break
        if self.append_contact:
            while True:
                if self.queue == 0:
                    self.queue = 1
                    new_contact = self.add_contact(self.client_name, self.append_contact)
                    send_msg(sock, new_contact)
                    while True:
                        if self.queue == 0:
                            self.filler(self.client_name, [self.append_contact])
                            break
                        elif self.queue == 2:
                            self.queue = 0
                            break
                    break
        if self.message:
            while True:
                if self.queue == 0:
                    send_msg(sock, self.create_message(ac_name=self.client_name, to=self.to, msg=self.message))
                    while True:
                        if self.queue == 1:
                            self.queue = 0
                            self.save_msg(self.client_name, self.to, self.message)
                            break
                    break
        if not self.message and not self.to and not self.append_contact and self.client_name and self.mode == 'console':
            while True:
                try:
                    action = input('Input action ("m" for sending message, "c" for getting list contacts, '
                                   '"a" for add contact, "d" for delete contact, "e" for exit): ')
                    if action == 'm':
                        to = input('Input user name of the message recipient: ')
                        msg = input('input text message: ')
                        jim_msg = self.save_msg(ac_name, to, msg)
                        send_msg(sock, jim_msg)
                    elif action == 'c':
                        jim_contacts = self.get_contacts(ac_name=ac_name)
                        send_msg(sock, jim_contacts)
                    elif action == 'a':
                        self.console_add_contact = input('Input contact name for adding in contact list: ')
                        jim_add_contact = self.add_contact(ac_name=ac_name, add_name=self.console_add_contact)
                        send_msg(sock, jim_add_contact)
                    elif action == 'd':
                        self.console_del_contact = input('Input contact name for deleting in contact list: ')
                        jim_del_contact = self.del_contact(ac_name=ac_name, del_name=self.console_del_contact)
                        send_msg(sock, jim_del_contact)
                    elif action == 'e':
                        break
                except Exception as e:
                    logger.critical(f'"sender()" return exception {e}')
                    break

    @Log()
    def recipient(self, sock, ac_name):
        """
        This method receive messages from messenger server.

        Parameters
        ----------
        server_answer
            Response from messenger server gets via ``get_msg`` function.
        queue
            A variable used as a queue for client-server interaction.
        salt
            'Salt' from the user password.
        eng.session.add
            Add message in ``MessageHistory`` table in ``session`` session.
        eng.session.commit()
            Save unsaved changes in ``session`` session.
        console_add_contact
            Being added contact in ``ContactList`` table.
        deleter
            Delete ``[console_del_contact]`` contacts ``client_name`` user in ``ContactList`` table.
        console_del_contact
            Being deleted contact in ``ContactList`` table.
        logger.critical
            Record a message '"sender()" return exception {e}' through a logger object at critical level.
        """
        while True:
            try:
                server_answer = get_msg(sock)
                if server_answer:
                    self.queue = 1
                if SALT in server_answer:
                    self.salt = server_answer[SALT]
                if ACT in server_answer:
                    if server_answer[ACT] == MESSAGE and server_answer[TO] == ac_name:
                        self.eng.session.add(MessageHistory(from_user=server_answer[FROM],
                                                            whom_user=server_answer[TO],
                                                            message=server_answer[MESSAGE]))
                        self.eng.session.commit()
                        self.queue = 0
                        print(f'\nReceived message: "{server_answer[MESSAGE]}" from {server_answer[FROM]}')
                elif server_answer[RESPONSE] == 202:
                    self.filler(self.client_name, server_answer[ALERT])
                    print(f'\nContacts: {server_answer[ALERT]}')
                elif server_answer[RESPONSE] == 'xxx':
                    self.queue = 0
                    if self.console_add_contact:
                        self.filler(self.client_name, [self.console_add_contact])
                        self.console_add_contact = ''
                    elif self.console_del_contact:
                        self.deleter(self.client_name, [self.console_del_contact])
                        self.console_del_contact = ''
                    print(f'\nAdd/delete contacts')
                elif server_answer[RESPONSE] == 400:
                    self.queue = 2
                    print(f'\nNot valid request')
                elif server_answer[RESPONSE] == 401:
                    self.queue = 3
                    print(f'\nUser does not exist or password wrong')
            except (ConnectionError, ConnectionAbortedError, ConnectionResetError):
                logger.critical(f'connection with the user {ac_name} is lost')
                break

    @login_required
    @log
    def save_msg(self, ac_name, to, msg):
        """
        This method save message in ``MessageHistory`` table.

        Parameters
        ----------
        eng.session.add
            Add message in ``MessageHistory`` table in ``session`` session.
        self.eng.session.commit()
            Save unsaved changes in ``session`` session.

        Returns
        -------
        dict
            JIM format message.
        """
        self.eng.session.add(MessageHistory(from_user=ac_name, whom_user=to, message=msg))
        self.eng.session.commit()
        return self.create_message(ac_name=ac_name, to=to, msg=msg)

    @login_required
    @log
    def create_message(self, ac_name='Guest', to='Server', msg=None):
        """
        This method create JIM format message.

        Parameters
        ----------
        message
            JIM format message.
        logger.info
            Record a message 'message "{message}" created' through a logger object at info level.

        Returns
        -------
        dict
            JIM format message.
        """
        message = {
            ACT: MESSAGE,
            TIME: time.time(),
            TO: to,
            FROM: ac_name,
            MESSAGE: msg
        }
        logger.info(f'message "{message}" created')
        return message

    @login_required
    @Log()
    def get_contacts(self, ac_name):
        """
        This method create JIM format message for getting contacts.

        Parameters
        ----------
        contacts
            JIM format message.
        logger.info
            Record a message 'client request "{contacts}" created' through a logger object at info level.

        Returns
        -------
        dict
            JIM format message.
        """
        contacts = {
            ACT: GET_CONTACTS,
            TIME: time.time(),
            USER: {
                AC_NAME: ac_name
            }
        }
        logger.info(f'client request "{contacts}" created')
        return contacts

    @login_required
    @Log()
    def add_contact(self, ac_name, add_name):
        """
        This method create JIM format message for adding contacts in ``ContactList`` table.

        Parameters
        ----------
        contact
            JIM format message.
        logger.info
            Record a message 'client request "{contact}" created' through a logger object at info level.

        Returns
        -------
        dict
            JIM format message.
        """
        contact = {
            ACT: ADD_CONTACT,
            USER_ID: add_name,
            TIME: time.time(),
            USER: {
                AC_NAME: ac_name
            }
        }
        logger.info(f'client request "{contact}" created')
        return contact

    @login_required
    @Log()
    def del_contact(self, ac_name, del_name):
        """
        This method create JIM format message for deleting contacts from ``ContactList`` table.

        Parameters
        ----------
        contact
            JIM format message.
        logger.info
            Record a message 'client request "{contact}" created' through a logger object at info level.

        Returns
        -------
        dict
            JIM format message.
        """
        contact = {
            ACT: DEL_CONTACT,
            USER_ID: del_name,
            TIME: time.time(),
            USER: {
                AC_NAME: ac_name
            }
        }
        logger.info(f'client request "{contact}" created')
        return contact

    @staticmethod
    @Log()
    def check_client(ac_name, password):
        """
        This method create JIM format message for checking exist of the user and validity password in ``Clients`` table.

        Parameters
        ----------
        check
            JIM format message.
        logger.info
            Record a message 'client request "{check}" created' through a logger object at info level.

        Returns
        -------
        dict
            JIM format message.
        """
        check = {
            ACT: CHECK_CLIENT,
            TIME: time.time(),
            USER: {
                AC_NAME: ac_name,
                PASSWORD: password
            }
        }
        logger.info(f'client request "{check}" created')
        return check

    @staticmethod
    @log
    def arg_parser():
        """
        This method create command line interface.

        Parameters
        ----------
        p
            Object ``ArgumentParser`` for getting parameters in command line.
        p.add_argument('a'...)
            Definition of the argument ``a`` with default value ``DEFAULT_IP_ADDRESS`` for messenger server ip-address.
        p.add_argument('p'...)
            Definition of the argument ``p`` with default value ``DEFAULT_PORT`` for messenger server port.
        p.add_argument('-n'...)
            Definition of the argument ``-n`` for username.
        p.add_argument('-d'...)
            Definition of the argument ``-d`` with default value ``DEFAULT_PATH_CLIENT`` for path to client database.
        p.add_argument('-m'...)
            Definition of the argument ``-m`` for text message.
        p.add_argument('-t'...)
            Definition of the argument ``-t`` for message addressee.
        p.add_argument('-c'...)
            Definition of the argument ``-c`` for being added contact.
        p.add_argument('-r'...)
            Definition of the argument ``-r`` for work mode client part messenger.
        p.add_argument('-s'...)
            Definition of the argument ``-s`` for user password.

        Returns
        -------
        Object ``ArgumentParser``
            For further conversion of parameters into objects.
        """
        p = argparse.ArgumentParser()
        p.add_argument('a', default=DEFAULT_IP_ADDRESS, nargs='?')
        p.add_argument('p', default=DEFAULT_PORT, type=int, nargs='?')
        p.add_argument('-n', default='', nargs='?')
        p.add_argument('-d', default=DEFAULT_PATH_CLIENT, nargs='?')
        p.add_argument('-m', default='', nargs='?')
        p.add_argument('-t', default='', nargs='?')
        p.add_argument('-c', default='', nargs='?')
        p.add_argument('-r', default=DEFAULT_MODE, nargs='?')
        p.add_argument('-s', default='', nargs='?')
        return p


if __name__ == '__main__':
    # eng.base.metadata.create_all(eng.eng)  # Uncomment to create database
    client = Client()
