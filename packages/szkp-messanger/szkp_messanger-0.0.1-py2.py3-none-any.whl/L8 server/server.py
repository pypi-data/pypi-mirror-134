"""
This module use for work messenger server.

Classes
-------
InitDb
    Initialization connect to database.
Clients(eng.base)
    Extend parent and create ``Clients`` table to database in declarative style.
ClientsHistory(eng.base)
    Extend parent and create ``ClientsHistory`` table to database in declarative style.
ContactList(eng.base)
    Extend parent and create ``ContactList`` table to database in declarative style.
ServerPortDesc
    The data descriptor for checking the port number used in the ``ServerVerifier`` metaclass.
ServerPort
    Storing an object of the ``ServerPortDesc`` descriptor class and the default port number.
ServerVerifier(type)
    Extend parent metaclass for ``Server`` class.
Server(metaclass=ServerVerifier)
    Messenger server with metaclass ``ServerVerifier``.
"""

import argparse
import json
import re
import time
import subprocess
from socket import socket, AF_INET, SOCK_STREAM
from hmac import compare_digest
from select import select

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, BINARY

from common.func import send_msg, get_msg
from common.settings import *
from log.conf.server_log_config import *
from decors import log, Log


class InitDb:
    """
    This class initialization connection to database.
    """

    def __init__(self, path_db=DEFAULT_PATH_SERVER):
        """
        This class constructor create connect to database, declarative style table class, session object.

        Parameters
        ----------
        eng
            Dialect an object for interacting with a database located along the ``path_db`` path.
        base
            Base class for declarative style classes with database ``eng`` engine.
        session_maker
            Session factory object.
        session
            Session for interacting with the database.
        """
        self.eng = create_engine(f'sqlite:///{path_db}', echo=True)
        self.base = declarative_base(self.eng)
        self.session_maker = sessionmaker(self.eng)
        self.session = self.session_maker()


eng = InitDb()


class Clients(eng.base):
    """
    This class extend parent and create table ``client`` to database in declarative style.
    """

    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)  #: ID, primary key.
    login = Column(String)  #: Column for username.
    info = Column(String)  #: Column for information of user.
    password = Column(BINARY)  #: Column for user password.

    def __init__(self, login, info, password):
        """
        This class constructor uses for assigning a value to an attribute.

        Parameters
        ----------
        login
            Column for username.
        info
            Column for information of user.
        password
            Column for user password.
        """
        self.login = login
        self.info = info
        self.password = password

    def __repr__(self):
        """
        This function returns a string representation of the object.

        Returns
        -------
        str
            Username.
        """
        return f'{self.login}'


class ClientsHistory(eng.base):
    """
    This class extend parent and create table ``client_history`` to database in declarative style.
    """

    __tablename__ = 'client_history'
    id = Column(Integer, primary_key=True)  #: ID, primary key.
    entry_time = Column(String)  #: Column for client entry time.
    ip_address = Column(String)  #: Column for client ip-address.

    def __init__(self, entry_time, ip_address):
        """
        This class constructor uses for assigning a value to an attribute.

        Parameters
        ----------
        entry_time
            Column for client entry time.
        ip_address
            Column for client ip-address.
        """
        self.entry_time = entry_time
        self.ip_address = ip_address

    def __repr__(self):
        """
        This function returns a string representation of the object.

        Returns
        -------
        str
            Entry time and ip-address client.
        """
        return f'Entry time: {self.entry_time}, ip-address: {self.ip_address}'


class ContactList(eng.base):
    """
    This class extend parent and create table ``contact_list`` to database in declarative style.
    """

    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True)  #: ID, primary key.
    id_owner = Column(Integer, ForeignKey('client.id'))  #: Column for id of owner user contact in ``Clients`` table.
    id_client = Column(Integer, ForeignKey('client.id'))  #: Column for id of contact in ``Clients`` table.

    def __init__(self, id_owner, id_client):
        """
        This class constructor uses for assigning a value to an attribute.

        Parameters
        ----------
        id_owner
            Column for id of owner user contact in ``Clients`` table.
        id_client
            Column for id of contact in ``Clients`` table.
        """
        self.id_owner = id_owner
        self.id_client = id_client

    def __repr__(self):
        """
        This function returns a string representation of the object.

        Returns
        -------
        str
            Contact id from ``Clients`` table.
        """
        return f'{self.id_client}'


class ServerPortDesc:
    """
    This class is used as a data descriptor for checks port number.
    """

    def __init__(self, port=None):
        """
        This class constructor uses for assigning a value to an ``port`` attribute.

        Parameters
        ----------
        port
            Number port.
        """
        self.port = port

    def __get__(self, instance, cls):
        """
        This descriptor return ``port`` attribute.

        Returns
        -------
        int
            Port number.
        """
        return self.port

    def __set__(self, instance, val):
        """
        This descriptor check port number ``val`` parameter and assigns it ``port`` attribute.

        Parameters
        ----------
        logger.critical(f'attempt to start server run on port < 1024 or > 65535')
            Record a message 'attempt to start server run on...' through a logger object at a critical level.
        sys.exit(1)
            Shutdown messenger server.
        port
            Number port.
        """
        if val < 1024 or val > 65535 and val >= 0:
            logger.critical(f'attempt to start server run on port < 1024 or > 65535')
            sys.exit(1)
        self.port = val


class ServerPort:
    """
    This class stores the object of the data descriptor ``ServerPortDesc`` and the default port number.
    """

    port = ServerPortDesc()
    default = DEFAULT_PORT


class ServerVerifier(type):
    """
    This metaclass extends parent for class ``Server``.
    """

    def __call__(cls, *args, **kwargs):
        """
        This function checks in the ``Server`` class the use of the ``connect`` method for socket and TCP protocol.

        Parameters
        ----------
        dis_out
            Output of the stdout stream server.py module.
        cls.obj.connection()
            Call method ``connection`` class ``Server``.

        Returns
        -------
        ``Server`` class object
            For not to call ``connection`` method ``Server`` class when working in test mode.

        Raises
        ------
        ValueError
            When using ``connect`` and not ``SOCK_STREAM`` for sockets.
        """
        cls.obj = super().__call__(*args, **kwargs)
        dis_out = subprocess.run(['python', '-m', 'dis', 'server.py'], capture_output=True,
                                 universal_newlines=True).stdout
        if len(re.findall('\(connect\)', dis_out)) > 0:
            raise ValueError('Server not can use "connect" for sockets')
        elif len(re.findall('\(SOCK_DGRAM\)', dis_out)) > 0 or \
                len(re.findall('\(SOCK_RAW\)', dis_out)) > 0 or \
                len(re.findall('\(SOCK_RDM\)', dis_out)) > 0 or \
                len(re.findall('\(SOCK_SEQPACKET\)', dis_out)) > 0:
            raise ValueError('Socket must use TCP')
        if cls.obj.test:
            return cls
        else:
            cls.obj.connection()
        return cls


class Server(metaclass=ServerVerifier):
    """
    This class for work messenger server.

    Methods
    -------
    connection
        Create a server connection to listen to client messages.
    process_client_msg(msg)
        Check clients requests and forming response.
    read
        Accepts a request from the client.
    write
        Send server response.
    arg_parser
        Command line interface.
    """

    def __init__(self, test=False, db_path=None):
        """
        This class constructor for configuration of a class object.

        Parameters
        ----------
        test
            Testing mode.
        none_type
            Object class ``NoneType`` for checks request to database.
        port
            Object of the storage class of the data descriptor object.
        logger
            Object logger for logging.
        all_clients
            Storage list of all connected clients.
        presence_clients
            Storage ``dict`` data type clients who sent a presence.
        par
            Command line interface object.
        name
            Converting a command line parameter string to object.
        l_address
            Ip-address for start messenger server from command line.
        l_port
            Number port for start messenger server from command line.
        db_path
            Path to database from command line.
        eng
            Connection object to database messenger server.
        sys.exit()
            Shutdown messenger server.
        port.port
            Check number port via data descriptor ``ServerPortDesc``.
        logger.info
            Record a message 'server is ...' through a logger object at an info level.
        """
        self.test = test
        self.none_type = None
        self.port = ServerPort()
        self.logger = logging.getLogger('chat.server')
        self.all_clients = []
        self.presence_clients = {}
        self.par = self.arg_parser(self.port)
        self.name = self.par.parse_args()
        self.l_address = self.name.a
        self.l_port = self.name.p
        self.db_path = self.name.d
        self.eng = InitDb()
        if db_path:
            self.db_path = db_path
        if os.path.exists(self.db_path):
            self.eng = InitDb(self.db_path)
        elif os.path.exists(DEFAULT_PATH_SERVER) and self.db_path != '':
            print('Database do not exist')
            sys.exit()
        self.port.port = self.l_port
        logger.info(f'server is running on port / address: {self.port.port} / {self.l_address}')

    @log
    def connection(self):
        """
        This method create connecting messenger server using sockets.

        Parameters
        ----------
        st.bind
            Bind socket object ``st`` with ip-address ``l_address`` and port ``port.port``.
        st.listen(MAX_CONNECT)
            Configures the messenger server to receive messages from clients with ``MAX_CONNECT`` maximum queue.
        st.settimeout(0.5)
            Set timeout for socket operation ``st`` socket object.
        sock
            Client socket object.
        address
            Client ip-address.
        eng.session.add
            Add record in ``ClientsHistory`` table with ``time.ctime(time.time())`` and ``address[0]`` arguments.
        eng.session.commit()
            Save unsaved changes ``session`` session in database.
        all_clients.append(sock)
            Add client socket object ``sock`` in ``all_clients`` list.
        rd
            Expected client socket object to read.
        wt
            Expected client socket object to write.
        er
            Expected client socket object to error.
        req_clients
            JIM format client messages.
        presence_clients[r]
            Client socket object that sent the presence.
        write
            Send messages to clients depending on their messages.
        """
        with socket(AF_INET, SOCK_STREAM) as st:
            st.bind((self.l_address, self.port.port))
            st.listen(MAX_CONNECT)
            st.settimeout(0.5)
            while True:
                try:
                    sock, address = st.accept()
                    if address:
                        self.eng.session.add(ClientsHistory(time.ctime(time.time()), address[0]))
                        self.eng.session.commit()
                except OSError:
                    pass
                else:
                    self.all_clients.append(sock)
                finally:
                    rd = []
                    wt = []
                    try:
                        rd, wt, er = select(self.all_clients, self.all_clients, [])
                    except Exception:
                        pass
                    req_clients = self.read(rd, self.all_clients)
                    if req_clients:
                        for r in req_clients:
                            if req_clients[r][ACT] == PRESENCE:
                                self.presence_clients[r] = req_clients[r]
                        self.write(req_clients, self.all_clients, self.presence_clients)
                    print('read_req', req_clients)

    @log
    def process_client_msg(self, msg):
        """
        This method forming messanger server response for clients.

        Parameters
        ----------
        response_400
            Messenger server response about a bad client request.
        response_200
            Messenger server response about a successful client request.
        logger.info
            Record a message 'server generating response for client: ...' through a logger object at an info level.
        alert_id
            List of client contacts IDs.
        alert_login
            List of client contacts usernames.
        response_202
            Messenger server response with list of client contacts usernames ``alert_login``.
        eng.session.add
            Add client contacts in ``ContactList`` table ``session`` session.
        eng.session.commit()
            Save unsaved changes in ``session`` session.
        id_contact
            ID client contact.
        eng.session.delete(id_contact)
            Delete a contact from the ``ContactList`` table with the ID ``id_contact`` ``session`` session.
        response_xxx
            Messenger server response about a successful added or deleted client contact.
        logger.warning(f'server generating response for client: {response_400}')
            Record a message 'server generating response for ...' through a logger object at an warning level.

        Returns
        -------
        dict
            Messenger server response.
        """
        response_400 = {RESPONSE: 400, ERROR: 'Bad request'}
        if ACT in msg and msg[ACT] == PRESENCE and TIME in msg and USER in msg:
            response_200 = {RESPONSE: 200,
                            SALT: self.eng.session.query(Clients).filter_by(login=msg[USER][AC_NAME])
                                      .first().password[64:].hex()}
            logger.info(f'server generating response for client: {response_200}')
            return response_200
        elif ACT in msg and msg[ACT] == MESSAGE and TIME in msg and TO in msg and FROM in msg and MESSAGE in msg:
            response_200 = {RESPONSE: 200}
            logger.info(f'server generating response for client: {response_200}')
            return response_200
        elif ACT in msg and msg[ACT] == GET_CONTACTS and TIME in msg and USER in msg:
            try:
                alert_id = self.eng.session.query(ContactList).filter_by(id_owner=self.eng.session.query(Clients)
                                                                         .filter_by(login=msg[USER][AC_NAME])
                                                                         .first().id).all()
                alert_login = [str(self.eng.session.query(Clients).get(str(n))) for n in alert_id]
            except Exception:
                logger.info(f'server generating response for client: {response_400}')
                return response_400
            response_202 = {RESPONSE: 202, ALERT: alert_login}
            logger.info(f'server generating response for client: {response_202}')
            return response_202
        elif ACT in msg and msg[ACT] == ADD_CONTACT or msg[ACT] == DEL_CONTACT and TIME in msg and \
                USER in msg and USER_ID in msg:
            if msg[ACT] == ADD_CONTACT:
                if self.eng.session.query(Clients).filter_by(login=msg[USER_ID]).first() is not self.none_type or \
                        self.eng.session.query(Clients).filter_by(login=msg[USER][AC_NAME]).first() is not \
                        self.none_type:
                    try:
                        self.eng.session.add(ContactList(id_owner=self.eng.session.query(Clients)
                                                         .filter_by(login=msg[USER][AC_NAME]).first().id,
                                                         id_client=self.eng.session.query(Clients)
                                                         .filter_by(login=msg[USER_ID]).first().id))
                        self.eng.session.commit()
                    except Exception:
                        logger.info(f'server generating response for client: {response_400}')
                        return response_400
                else:
                    return response_400
            elif msg[ACT] == DEL_CONTACT:
                if self.eng.session.query(Clients).filter_by(login=msg[USER_ID]).first() is not self.none_type or \
                        self.eng.session.query(Clients).filter_by(login=msg[USER][AC_NAME]).first() is not \
                        self.none_type:
                    try:
                        id_contact = self.eng.session.query(ContactList).filter_by(id_owner=self.eng.session
                                                                                   .query(Clients)
                                                                                   .filter_by(login=msg[USER][AC_NAME])
                                                                                   .first().id, id_client=self.eng
                                                                                   .session.query(Clients)
                                                                                   .filter_by(login=msg[USER_ID])
                                                                                   .first().id).first()
                        self.eng.session.delete(id_contact)
                        self.eng.session.commit()
                    except Exception:
                        logger.info(f'server generating response for client: {response_400}')
                        return response_400
                else:
                    return response_400
            response_xxx = {RESPONSE: 'xxx'}
            return response_xxx
        elif msg[ACT] == CHECK_CLIENT:
            if self.eng.session.query(Clients).filter_by(login=msg[USER][AC_NAME]).first() is not self.none_type and \
                    compare_digest(self.eng.session.query(Clients).filter_by(login=msg[USER][AC_NAME]).first().password,
                                   bytes.fromhex(msg[USER][PASSWORD])):
                return {RESPONSE: 200}
            else:
                return {RESPONSE: 401}
        logger.warning(f'server generating response for client: {response_400}')
        return response_400

    @log
    def read(self, clients, all_clients):
        """
        This method gets messages from clients.

        Parameters
        ----------
        req_clients
            JIM format clients messages.
        logger.critical
            Record a message 'server cannot decode message from ...' through a logger object at an critical level.
        logger.info
            Record a message 'server getting request from...' through a logger object at an info level.
        s.close()
            Close client ``s`` socket.
        all_clients.remove(s)
            Delete client ``s`` socket from ``all_clients`` list.

        Returns
        -------
        dict
            JIM format messages clients.
        """
        req_clients = {}
        for s in clients:
            try:
                try:
                    req_clients[s] = get_msg(s)
                except (ValueError, json.JSONDecodeError):
                    logger.critical(f'server cannot decode message from client {s.getpeername()}')
                logger.info(f'server getting request from {s.getpeername()}, and message {req_clients[s]}')
                print(req_clients[s])
            except Exception:
                logger.info(f'Client {s.fileno()} {s.getpeername()} disconnected')
                s.close()
                all_clients.remove(s)
        return req_clients

    @Log()
    def write(self, req_clients, all_clients, presence_clients):
        """
        This method send messages to clients.

        Parameters
        ----------
        client_msg
            JIM format client message.
        logger.warning
            Record a message 'Client {r.fileno()} {r.getpeername()}...' through a logger object at an warning level.
        r.close()
            Close client ``r`` socket.
        all_clients.remove(r)
            Delete client ``r`` socket from ``all_clients`` list.
        """
        for r in req_clients:
            try:
                client_msg = req_clients[r]
                if client_msg[ACT] == PRESENCE:
                    send_msg(r, self.process_client_msg(client_msg))
                elif client_msg[ACT] == MESSAGE and self.process_client_msg(client_msg) == {RESPONSE: 200}:
                    for w in presence_clients:
                        if req_clients[r][TO] == presence_clients[w][USER][AC_NAME] and \
                                presence_clients[w][MODE] == DEFAULT_MODE:
                            send_msg(w, client_msg)
                    send_msg(r, self.process_client_msg(client_msg))
                elif client_msg[ACT] == GET_CONTACTS or client_msg[ACT] == ADD_CONTACT \
                        or client_msg[ACT] == DEL_CONTACT or client_msg[ACT] == CHECK_CLIENT:
                    send_msg(r, self.process_client_msg(client_msg))
            except Exception:
                logger.warning(f'Client {r.fileno()} {r.getpeername()} disconnected')
                r.close()
                all_clients.remove(r)

    @Log()
    def arg_parser(self, def_port):
        """
        This method create command line interface.

        Parameters
        ----------
        p
            Object ``ArgumentParser`` for getting parameters in command line.
        p.add_argument('-p'...)
            Definition of the argument ``-p`` with default value ``def_port.default`` for messenger server port.
        p.add_argument('-a'...)
            Definition of the argument ``-n`` for messenger server ip-address.
        p.add_argument('-d'...)
            Definition of the argument ``-d`` for messenger server path to database.

        Returns
        -------
        Object ``ArgumentParser``
            For further conversion of parameters into objects.
        """
        p = argparse.ArgumentParser()
        p.add_argument('-p', default=def_port.default, type=int)
        p.add_argument('-a', default='')
        p.add_argument('-d', default='')
        return p


if __name__ == '__main__':
    # eng.base.metadata.create_all(eng.eng)  # Uncomment to create database
    Tim = Clients('Tim', 'Default user',
                  b'nI\xf7\xee\xdb S\x9f4\xc8x\xad\x9d\x9a\xbcu\x1e\xa9\xf5G8\xabsY@\x08\x84\xb2b\xc0\xd1\x08Bqo\xc4\
                  xf1\x0cS\xb0\xff:\x16XJ\xccj\xbe\xa4\xac\xa8\xcc\xd92X#\xdb1u\xd7\xfc74\x9cS\xb7\xf5\xee1\x19\xf1\xe2\
                  x8f}5\x9c\x92\xc2\x88\xc5')
    Kevin = Clients('Kevin', 'Default user',
                    b"\xe5\xd7\xcd\xde\x90\xe2r\x8d\x1b\x046\xc7O6{\x92\xdbn'\x0f\x1c[\x05\xe6To\xf8\xd9\x0c\x99,\x0b5E\
                    xc01\xcd\xc5\xeb\xc9\xeb;\x07!\xbf\x05\xd9\xf5\xee\xf7\x86%\xaey6\xc1\x10\t\xefo\xb4\x7f\n\xfe\xf0\
                    xe3\xe9Jf]l9\xc8\xfc\xccV\xd6\xe1\x02,")
    Dora = Clients('Dora', 'Default user',
                   b'\xe7\xa6\xf6\x9a\x18\xc3\xd2\xe7|@e;\x08\xee\x9c3\x0e)\xaew\x1a\x80T\xd8\xad\xc1Dr\x1d\xe53\xb5\
                   x92\xc7/C\xaf\x14"\xb4\x87\xf5\xfdm\x878q\xd6\x0f\x8eQ\xb8\xee\x0fG\x81l\x96\xd5\xb7j\xf8g\xe1\x83H\
                   x8cr%J7\x94\xb6\xcc\xdb\xa5\xa7\xc5\xf4b')
    user_0 = Clients('user_0', 'Default user',
                     b'b\xda\xc8\x86h\xe4\xb1\x1dt\xf9L\x8d\xe0\x8eL2L\xbfb\x12\x12#(\xc71\x0bM\xcd\x17"k\xe2\xf8\xf0\t\
                     xf6\xe3\xdfT\x08\xc3:V\xcd\xc3\x90\x05\xc89\xfaJ\xcdX7\xb7\x17\xb2\xee.\x94\xd3CB]#\xebl9\xffi\
                     xca=\\K\x8d;\x88\xbe!W')
    user_1 = Clients('user_1', 'Default user',
                     b'\x97\xc5\xb9\x8c8\x90\x85\xa8\x13\xbc\xab[A\x91\xc0\xcb\x1b\xfc\x0b\xe5\x95)\xb7U\xaem\xfav\x0f\
                     x9b\x07\x97r\xb8\xea\x0e\xf5$\xd6\x85\x17\x9d\xe9!*\x9e\xf5l\xdb%\xe0\x8b|\x02\xaaf\xa4[R@\x95\
                     xdc%\x7f\xa6\x00\x80\xda\x97k\xa9\xec~\x8a\x9d\x80:l%I')
    eng.session.add_all([Tim, Kevin, Dora, user_0, user_1])
    # eng.session.commit()  # Uncomment to fill database
    eng.session.add_all([ContactList(Tim.id, Kevin.id),
                         ContactList(Tim.id, Dora.id),
                         ContactList(Kevin.id, Tim.id),
                         ContactList(Kevin.id, Dora.id),
                         ContactList(Dora.id, Tim.id),
                         ContactList(Dora.id, Kevin.id),
                         ContactList(user_0.id, user_1.id),
                         ContactList(user_0.id, Tim.id),
                         ContactList(user_1.id, user_0.id),
                         ContactList(user_1.id, Kevin.id)])
    # eng.session.commit()  # Uncomment to fill database
    server = Server()
