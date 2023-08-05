"""
This module use for rendering of the PyQt GUI server.py module.

Classes
-------
AdminServer (QMainWindow)
    Extend class QMainWindow for rendering of the GUI of the server.py module.
"""

import sys
import subprocess

from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QLabel, QLineEdit, QPushButton, QFileDialog, \
    QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from server import Clients, ClientsHistory


class AdminServer(QMainWindow):
    """
    This class create graphics interface for server.py module uses PyQt.

    Methods
    -------
    gui()
        Places and adjusts graphics elements on the window.
    dialog_conn()
        Dialog window for choice path to database and request username.
    fill()
        Fills in data from statistics and clients tables.
    identification()
        Check enters username to exist in clients table.
    start_server()
        Run server.py module with parameters needs for a run messenger server.
    """

    def __init__(self):
        """
        Constructor ``__init__`` extend parent and defines instance variables for common use of them in class methods.

        Parameters
        ----------
        none_type
            Object class ``NoneType`` for checks request to database.
        model_clients
            Instance class ``QStandardItemModel`` to create a model of the object ``list_clients``.
        model_statistics
            Instance class ``QStandardItemModel`` to create a model of the object ``list_statistics``.
        field_conn
            Instance class ``QLineEdit`` to display the path of the selected database.
        list_clients
            Instance class ``QListView`` to display clients from the clients table.
        list_statistics
            Instance class ``QListView`` to display statistics from the client history table.
        field_status_server
            Instance class ``QLineEdit`` to display the status works messenger server.
        field_identification_status
            Instance class ``QLineEdit`` to display the identification status.
        list_clients.setModel(model_clients)
            Set ``model_clients`` model to the ``list_clients`` object.
        list_statistics.setModel(model_statistics)
            Set ``model_statistics`` model to the ``list_statistics`` object.
        gui
            Call method ``gui`` for setting and show main window.
        """
        super(AdminServer, self).__init__()
        self.none_type = None
        self.model_clients = QStandardItemModel()
        self.model_statistics = QStandardItemModel()
        self.field_conn = QLineEdit()
        self.list_clients = QListView()
        self.list_statistics = QListView()
        self.field_status_server = QLineEdit()
        self.field_identification_status = QLineEdit()
        self.list_clients.setModel(self.model_clients)
        self.list_statistics.setModel(self.model_statistics)
        self.gui()

    def gui(self):
        r"""
        This method create main window gui server.py module.

        Parameters
        ----------
        button_conn
            Instance class ``QPushButton`` for choices database and identification.
        button_conn.setText
            Set text 'Select DB \nand start\n server' for the ``button_conn`` object.
        label_clients
            Instance class ``QLabel`` for label 'Clients'.
        label_statistics
            Instance class ``QLabel`` for label 'Statistics'.
        label_conn
            Instance class ``QLabel`` for label 'Path to database'.
        label_status_server
            Instance class ``QLabel`` for label 'Server status'.
        label_status_identification
            Instance class ``QLabel`` for label 'Identification status'.
        label_clients.setGeometry
            Set the location of the object ``label_clients`` in pixels: x:65, y:5, h:50, w:15.
        list_clients.setGeometry
            Set the location of the object ``list_clients`` in pixels: x:5, y:25, h:150, w:470.
        label_statistics.setGeometry
            Set the location of the object ``label_statistics`` in pixels: x:305, y:245, h:50, w:15.
        list_statistics.setGeometry
            Set the location of the object ``list_statistics`` in pixels: x:160, y:265, h:335, w:230.
        label_conn.setGeometry
            Set the location of the object ``label_conn`` in pixels: x:250, y:5, h:90, w:15.
        field_conn.setGeometry
            Set the location of the object ``field_conn`` in pixels: x:160, y:25, h:265, w:30.
        field_status_server.setGeometry
            Set the location of the object ``field_status_server`` in pixels: x:160, y:85, h:335, w:30.
        label_status_server.setGeometry
            Set the location of the object ``label_status_server`` in pixels: x:290, y:65, h:70, w:15.
        button_conn.setGeometry
            Set the location of the object ``button_conn`` in pixels: x:430, y:24, h:65, w:56.
        field_identification_status.setGeometry
            Set the location of the object ``field_identification_status`` in pixels: x:160, y:205, h:335, w:30.
        label_status_identification.setGeometry
            Set the location of the object ``label_status_identification`` in pixels: x:275, y:185, h:100, w:15.
        field_conn.setReadOnly(True)
            Set read-only setting for object ``field_conn``.
        field_status_server.setReadOnly(True)
            Set read-only setting for object ``field_status_server``.
        field_identification_status.setReadOnly(True)
            Set read-only setting for object ``field_identification_status``.
        button_conn.clicked.connect(dialog_conn)
            Connect click event to the object ``button_conn`` for calls method ``dialog_conn``.
        layout().addWidget(list_clients)
            Add an object ``list_clients`` to the main window layer.
        layout().addWidget(label_clients)
            Add an object ``label_clients`` to the main window layer.
        layout().addWidget(list_statistics)
            Add an object ``list_statistics`` to the main window layer.
        layout().addWidget(label_statistics)
            Add an object ``label_statistics`` to the main window layer.
        layout().addWidget(label_conn)
            Add an object ``label_conn`` to the main window layer.
        layout().addWidget(field_conn)
            Add an object ``field_conn`` to the main window layer.
        layout().addWidget(button_conn)
            Add an object ``button_conn`` to the main window layer.
        layout().addWidget(field_status_server)
            Add an object ``field_status_server`` to the main window layer.
        layout().addWidget(label_status_server)
            Add an object ``label_status_server`` to the main window layer.
        layout().addWidget(label_status_identification)
            Add an object ``label_status_identification`` to the main window layer.
        layout().addWidget(field_identification_status)
            Add an object ``field_identification_status`` to the main window layer.
        setGeometry
            Set parameters main window in pixels: x:500, y:500, h:500, w:500.
        setWindowTitle('Administration')
            Set text 'Administration' to the title main window.
        show()
            Call method ``show`` for show main window.
        """
        button_conn = QPushButton()
        button_conn.setText('Select DB \nand start\n server')
        label_clients = QLabel('Clients')
        label_statistics = QLabel('Statistics')
        label_conn = QLabel('Path to database')
        label_status_server = QLabel('Server status')
        label_status_identification = QLabel('Identification status')
        label_clients.setGeometry(65, 5, 50, 15)
        self.list_clients.setGeometry(5, 25, 150, 470)
        label_statistics.setGeometry(305, 245, 50, 15)
        self.list_statistics.setGeometry(160, 265, 335, 230)
        label_conn.setGeometry(250, 5, 90, 15)
        self.field_conn.setGeometry(160, 25, 265, 30)
        self.field_status_server.setGeometry(160, 85, 335, 30)
        label_status_server.setGeometry(290, 65, 70, 15)
        button_conn.setGeometry(430, 24, 65, 56)
        self.field_identification_status.setGeometry(160, 205, 335, 30)
        label_status_identification.setGeometry(275, 185, 100, 15)
        self.field_conn.setReadOnly(True)
        self.field_status_server.setReadOnly(True)
        self.field_identification_status.setReadOnly(True)
        button_conn.clicked.connect(self.dialog_conn)
        self.layout().addWidget(self.list_clients)
        self.layout().addWidget(label_clients)
        self.layout().addWidget(self.list_statistics)
        self.layout().addWidget(label_statistics)
        self.layout().addWidget(label_conn)
        self.layout().addWidget(self.field_conn)
        self.layout().addWidget(button_conn)
        self.layout().addWidget(self.field_status_server)
        self.layout().addWidget(label_status_server)
        self.layout().addWidget(label_status_identification)
        self.layout().addWidget(self.field_identification_status)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Administration')
        self.show()

    def dialog_conn(self):
        """
        This method call dialog window for choice path to database and request username.

        Parameters
        ----------
        start
            Variable for saving state running messenger server.
        file
            Path to the selected database in dialog window.
        check
            Checks the click on the button 'Ok'.
        new_eng
            Connect to database.
        session_maker
            Session factory.
        new_session
            Session object.
        model_clients.clear()
            Clearing the model ``model_clients`` for object ``list_clients``.
        model_statistics.clear()
            Clearing the model ``model_statistics`` for object ``list_statistics``.
        field_status_server.setText
            Set text 'Connection successfully, server not working' for the ``field_status_server`` object.
        field_conn.setText(file)
            Set text of the ``file`` object for the ``field_conn`` object.
        new_session.query(Clients).all()
            Fill in the ``new_session`` session as a result of the query with all records of the 'Clients' table.
        field_status_server.setText
            Set text 'Invalid database selected. Select database...' for the ``field_status_server`` object.
        field_identification_status.clear()
            Clearing the field ``field_identification_status``.
        start.terminate()
            Stop the execution of messenger server.
        """
        global start
        file, check = QFileDialog.getOpenFileName(self, 'Path to database', '', 'All files (*)')
        if check:
            if 'start' in globals() and start is not self.none_type:
                start.terminate()
            new_eng = create_engine(f'sqlite:///{file}', echo=True)
            session_maker = sessionmaker(bind=new_eng)
            new_session = session_maker()
            self.model_clients.clear()
            self.model_statistics.clear()
            self.field_status_server.setText('Connection successfully, server not working')
            self.field_conn.setText(file)
            try:
                new_session.query(Clients).all()
                start = self.fill(new_session, file)
            except Exception:
                self.field_status_server.setText('Invalid database selected. Select database messanger server.')
                self.field_identification_status.clear()
                if 'start' in globals() and start is not self.none_type:
                    start.terminate()

    def fill(self, new_session, file):
        """
        This method fills in the fields ``list_clients`` and ``list_statistics`` with data.

        Parameters
        ----------
        clients
            All records in the ``Clients`` table from the ``new_session`` session.
        statistics
            All records in the ``ClientsHistory`` table from the ``new_session`` session.
        row
            Instance class ``QStandardItem`` for forming a string for filling fields.
        model_clients.appendRow(row)
            Add ``row`` string in the ``model_clients`` model.
        model_statistics.appendRow(row)
            Add ``row`` string in the ``model_statistics`` model.
        run_server = self.start_server(file)
            Instance class ``Popen`` for the starting messenger server with path to database ``file``.

        Returns
        -------
        Object ``Popen``
            Start messenger server.
        """
        if self.identification(new_session) == 0:
            clients = new_session.query(Clients).all()
            statistics = new_session.query(ClientsHistory).all()
            for client in clients:
                row = QStandardItem(str(client))
                self.model_clients.appendRow(row)
            for indicator in statistics:
                row = QStandardItem(str(indicator))
                self.model_statistics.appendRow(row)
            run_server = self.start_server(file)
            return run_server

    def identification(self, new_session):
        """
        This method identifies the user by checking for the existence of the username in the ``Clients`` table.

        Parameters
        ----------
        login
            Enter login in dialog window.
        ok
            Checks the click on the button 'Ok'.
        new_session.query(Clients).filter_by(login=login).first()
            Query to the ``Clients`` table with the filter of the entered login from the dialog window.
        field_identification_status.setText
            Set text 'User identification complete' for the object ``field_identification_status``.
        field_identification_status.setText
            Set text 'UUser identification do not complete' for the object ``field_identification_status``.
        start.terminate()
            Stop the execution of messenger server.

        Returns
        -------
        int
            Success code. 0 - success, 1 - unsuccessful.
        """
        login, ok = QInputDialog().getText(self, 'Enter your login', 'Login: ', QLineEdit.Normal)
        if login and ok:
            if new_session.query(Clients).filter_by(login=login).first():
                self.field_identification_status.setText('User identification complete')
                return 0
            else:
                self.field_identification_status.setText('User identification do not complete')
                if 'start' in globals() and start is not self.none_type:
                    start.terminate()
                return 1

    def start_server(self, file):
        """
        This method starting messenger server via module server.py.

        Parameters
        ----------
        run_server
            Instance class ``Popen`` for starting messenger server via server.py module.
        field_status_server.setText
            Set text 'Connection successfully and server working' for the object ``field_status_server``.

        Returns
        -------
        Object ``Popen``
            Start messenger server.
        """
        run_server = subprocess.Popen(['python', '../server.py', '-d', f'{file}'])
        self.field_status_server.setText('Connection successfully and server working')
        return run_server


if __name__ == '__main__':
    app = QApplication(sys.argv)
    adm = AdminServer()
    sys.exit(app.exec_())
