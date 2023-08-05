"""
This module use for rendering of the PyQt GUI client.py module.

Classes
-------
ClientChat (QMainWindow)
    Extend class QMainWindow for rendering of the GUI of the module client.py.
ChatTableView (QTableView)
    Extend class QTableView for definition of a new signal - double click.
"""

import sys
import os
import subprocess

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import pyqtSignal


class ClientChat(QMainWindow):
    """
    This class create graphics interface for module client.py uses PyQt.

    Methods
    -------
    gui()
        Places and adjusts graphics elements on the window.
    identification()
        Checks the correctness of the entered login and password enters on the main window.
    show_history(clicked_login)
        Shows message history selected ``contact(clicked_login)``.
    add_contact()
        Adds contact in contact list.
    send_message()
        Sends message selected contact.
    """

    def __init__(self):
        r"""
        Constructor ``__init__`` extend parent and defines instance variables for common use of them in class methods.

        Parameters
        -----------
        login
            Entered login.
        password
            Entered password.
        clicked_login
            Clicked login in contact list.
        path_db
            Absolute path to client database.
        connect
            Create connect to client database.
        connect.setDatabaseName(path_db)
            Set ``path_db`` path to connect client database.
        list_contacts
            Instance class ``ChatTableView`` with new signal of double-clicked.
        model_contacts
            Instance class ``QSqlTableModel`` to create a model of the object ``list_contacts``.
        model_contacts.setTable('contact_list')
            Filling the model ``model_contacts`` with data from the ``contact_list`` table.
        list_contacts.setModel(model_contacts)
            Set ``model_contacts`` model to the ``list_contacts`` object.
        list_contacts.setColumnHidden
            Set hiding column with 0 index to the ``list_contacts`` object.
        list_contacts.setColumnHidden
            Set hiding column with 1 index to the ``list_contacts`` object.
        list_contacts.setColumnWidth
            Set column width with index 2 to 150 pixel to the ``list_contacts`` object.
        list_contacts.setShowGrid(False)
            Set the grid display off to the ``list_contacts`` object.
        list_contacts.horizontalHeader().hide()
            Set the horizontal header hide to the ``list_contacts`` object.
        list_contacts.verticalHeader().hide()
            Set the vertical header hide to the ``list_contacts`` object.
        list_history_messages
            Instance class ``QTableView`` for view history massage.
        model_history_messages
            Instance class ``QSqlTableModel`` to create a model of the object ``list_history_messages``.
        model_history_messages.setTable('message_history')
            Filling the model ``model_history_messages`` with data from the ``message_history`` table.
        list_history_messages.setModel(model_history_messages)
            Set ``model_history_messages`` model to the ``list_history_messages`` object.
        list_history_messages.setColumnHidden
            Set hiding column with 0 index to the ``list_history_messages`` object.
        list_history_messages.setColumnHidden
            Set hiding column with 2 index to the ``list_history_messages`` object.
        list_history_messages.horizontalHeader().setStretchLastSection(True)
            Set the stretch of the last column to the ``list_history_messages`` object to the window size.
        list_history_messages.setShowGrid(False)
            Set the grid display off to the ``list_history_messages`` object.
        list_history_messages.horizontalHeader().hide()
            Set the horizontal header hide to the ``list_history_messages`` object.
        list_history_messages.verticalHeader().hide()
            Set the vertical header hide to the ``list_history_messages`` object.
        field_enter_message
            Instance class ``QLineEdit`` for enters message.
        field_enter_message.setPlaceholderText
            Set placeholder with text 'Enter your message' for the ``field_enter_message`` object.
        field_enter_contact
            Instance class ``QLineEdit`` for enters contact.
        field_enter_contact.setPlaceholderText
            Set placeholder with text 'Enter contact' for the ``field_enter_contact`` object.
        field_identification_login
            Instance class ``QLineEdit`` for enters username.
        field_identification_password
            Instance class ``QLineEdit`` for enters password.
        field_identification_status
            Instance class ``QLineEdit`` for viewing identification status.
        button_send
            Instance class ``QPushButton`` for sends message.
        button_send.setText('Send')
            Set text 'Send' for the ``button_send`` object.
        button_add_contact
            Instance class ``QPushButton`` for adds contact.
        button_add_contact.setText
            Set text 'Add\n contact' for the ``button_add_contact`` object.
        button_ident_login
            Instance class ``QPushButton`` for user identification.
        button_ident_login.setText('Enter')
            Set text 'Enter' for the ``button_ident_login`` object.
        gui
            Call method ``gui`` for setting and show main window.
        """
        super(ClientChat, self).__init__()
        self.login = ''
        self.password = ''
        self.clicked_login = ''
        self.path_db = os.path.abspath('../storage_client.db')
        self.connect = QSqlDatabase.addDatabase('QSQLITE')
        self.connect.setDatabaseName(self.path_db)
        self.list_contacts = ChatTableView()
        self.model_contacts = QSqlTableModel(self)
        self.model_contacts.setTable('contact_list')
        self.list_contacts.setModel(self.model_contacts)
        self.list_contacts.setColumnHidden(0, True)
        self.list_contacts.setColumnHidden(1, True)
        self.list_contacts.setColumnWidth(2, 150)
        self.list_contacts.setShowGrid(False)
        self.list_contacts.horizontalHeader().hide()
        self.list_contacts.verticalHeader().hide()
        self.list_history_messages = QTableView()
        self.model_history_messages = QSqlTableModel(self)
        self.model_history_messages.setTable('message_history')
        self.list_history_messages.setModel(self.model_history_messages)
        self.list_history_messages.setColumnHidden(0, True)
        self.list_history_messages.setColumnHidden(2, True)
        self.list_history_messages.horizontalHeader().setStretchLastSection(True)
        self.list_history_messages.setShowGrid(False)
        self.list_history_messages.horizontalHeader().hide()
        self.list_history_messages.verticalHeader().hide()
        self.field_enter_message = QLineEdit()
        self.field_enter_message.setPlaceholderText('Enter your message')
        self.field_enter_contact = QLineEdit()
        self.field_enter_contact.setPlaceholderText('Enter contact')
        self.field_identification_login = QLineEdit()
        self.field_identification_password = QLineEdit()
        self.field_identification_status = QLineEdit()
        self.button_send = QPushButton()
        self.button_send.setText('Send')
        self.button_add_contact = QPushButton()
        self.button_add_contact.setText('Add\n contact')
        self.button_ident_login = QPushButton()
        self.button_ident_login.setText('Enter')
        self.gui()

    def gui(self):
        r"""
        This method create main window gui client.py module.

        Parameters
        ----------
        label_contacts
            Instance class ``QLabel`` for label 'Contacts'.
        label_history_messages
            Instance class ``QLabel`` for label 'History messages'.
        label_identification_status
            Instance class ``QLabel`` for label 'Identification status'.
        label_identification_login
            Instance class ``QLabel`` for label 'Enter your login'.
        label_identification_password
            Instance class ``QLabel`` for label 'Enter your password'.
        label_contacts.setGeometry
            Set the location of the object ``label_contacts`` in pixels: x:60, y:5, h:60, w:15.
        list_contacts.setGeometry
            Set the location of the object ``list_contacts`` in pixels: x:5, y:25, h:150, w:415.
        field_enter_contact.setGeometry
            Set the location of the object ``field_enter_contact`` in pixels: x:5, y:445, h:95, w:50.
        label_history_messages.setGeometry
            Set the location of the object ``label_history_messages`` in pixels: x:285, y:125, h:90, w:15.
        list_history_messages.setGeometry
            Set the location of the object ``list_history_messages`` in pixels: x:160, y:145, h:335, w:295.
        field_enter_message.setGeometry
            Set the location of the object ``field_enter_message`` in pixels: x:160, y:445, h:280, w:50.
        field_identification_login.setGeometry
            Set the location of the object ``field_identification_login`` in pixels: x:160, y:25, h:145, w:30.
        label_identification_login.setGeometry
            Set the location of the object ``label_identification_login`` in pixels: x:195, y:5, h:90, w:15.
        field_identification_password.setGeometry
            Set the location of the object ``field_identification_password`` in pixels: x:310, y:25, h:145, w:30.
        label_identification_password.setGeometry
            Set the location of the object ``label_identification_password`` in pixels: x:333, y:5, h:100, w:15.
        field_identification_status.setGeometry
            Set the location of the object ``field_identification_status`` in pixels: x:160, y:85, h:335, w:30.
        label_identification_status.setGeometry
            Set the location of the object ``label_identification_status`` in pixels: x:278, y:65, h:100, w:15.
        button_send.setGeometry
            Set the location of the object ``button_send`` in pixels: x:445, y:445, h:50, w:50.
        button_add_contact.setGeometry
            Set the location of the object ``button_add_contact`` in pixels: x:105, y:445, h:50, w:50.
        button_ident_login.setGeometry
            Set the location of the object ``button_ident_login`` in pixels: x:460, y:25, h:35, w:30.
        field_identification_status.setReadOnly(True)
            Set read-only setting for object ``field_identification_status``.
        layout().addWidget(list_contacts)
            Add an object ``list_contacts`` to the main window layer.
        layout().addWidget(label_contacts)
            Add an object ``label_contacts`` to the main window layer.
        layout().addWidget(field_enter_contact)
            Add an object ``field_enter_contact`` to the main window layer.
        layout().addWidget(field_enter_message)
            Add an object ``field_enter_message`` to the main window layer.
        layout().addWidget(list_history_messages)
            Add an object ``list_history_messages`` to the main window layer.
        layout().addWidget(label_history_messages)
            Add an object ``label_history_messages`` to the main window layer.
        layout().addWidget(field_identification_login)
            Add an object ``field_identification_login`` to the main window layer.
        layout().addWidget(label_identification_login)
            Add an object ``label_identification_login`` to the main window layer.
        layout().addWidget(field_identification_password)
            Add an object ``field_identification_password`` to the main window layer.
        layout().addWidget(label_identification_password)
            Add an object ``label_identification_password`` to the main window layer.
        layout().addWidget(field_identification_status)
            Add an object ``field_identification_status`` to the main window layer.
        layout().addWidget(label_identification_status)
            Add an object ``label_identification_status`` to the main window layer.
        layout().addWidget(button_send)
            Add an object ``button_send`` to the main window layer.
        layout().addWidget(button_add_contact)
            Add an object ``button_add_contact`` to the main window layer.
        layout().addWidget(button_ident_login)
            Add an object ``button_ident_login`` to the main window layer.
        button_ident_login.clicked.connect(identification)
            Connect click event to the object ``button_ident_login`` for calls method ``identification``.
        list_contacts.double_clicked.connect(show_history)
            Connect double click event to the object ``list_contacts`` for calls method ``show_history``.
        button_add_contact.clicked.connect(add_contact)
            Connect click event to the object ``button_add_contact`` for calls method ``add_contact``.
        button_send.clicked.connect(send_message)
            Connect click event to the object ``button_send`` for calls method ``send_message``.
        setGeometry
            Set parameters main window in pixels: x:500, y:500, h:500, w:500.
        setWindowTitle('Chat')
            Set text 'Chat' to the title main window.
        show()
            Call method ``show`` for show main window.
        """
        label_contacts = QLabel('Contacts')
        label_history_messages = QLabel('History messages')
        label_identification_status = QLabel('Identification status')
        label_identification_login = QLabel('Enter your login')
        label_identification_password = QLabel('Enter your password')
        label_contacts.setGeometry(60, 5, 60, 15)
        self.list_contacts.setGeometry(5, 25, 150, 415)
        self.field_enter_contact.setGeometry(5, 445, 95, 50)
        label_history_messages.setGeometry(285, 125, 90, 15)
        self.list_history_messages.setGeometry(160, 145, 335, 295)
        self.field_enter_message.setGeometry(160, 445, 280, 50)
        self.field_identification_login.setGeometry(160, 25, 145, 30)
        label_identification_login.setGeometry(195, 5, 90, 15)
        self.field_identification_password.setGeometry(310, 25, 145, 30)
        label_identification_password.setGeometry(333, 5, 100, 15)
        self.field_identification_status.setGeometry(160, 85, 335, 30)
        label_identification_status.setGeometry(278, 65, 100, 15)
        self.button_send.setGeometry(445, 445, 50, 50)
        self.button_add_contact.setGeometry(105, 445, 50, 50)
        self.button_ident_login.setGeometry(460, 25, 35, 30)
        self.field_identification_status.setReadOnly(True)
        self.layout().addWidget(self.list_contacts)
        self.layout().addWidget(label_contacts)
        self.layout().addWidget(self.field_enter_contact)
        self.layout().addWidget(self.field_enter_message)
        self.layout().addWidget(self.list_history_messages)
        self.layout().addWidget(label_history_messages)
        self.layout().addWidget(self.field_identification_login)
        self.layout().addWidget(label_identification_login)
        self.layout().addWidget(self.field_identification_password)
        self.layout().addWidget(label_identification_password)
        self.layout().addWidget(self.field_identification_status)
        self.layout().addWidget(label_identification_status)
        self.layout().addWidget(self.button_send)
        self.layout().addWidget(self.button_add_contact)
        self.layout().addWidget(self.button_ident_login)
        self.button_ident_login.clicked.connect(self.identification)
        self.list_contacts.double_clicked.connect(self.show_history)
        self.button_add_contact.clicked.connect(self.add_contact)
        self.button_send.clicked.connect(self.send_message)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Chat')
        self.show()

    def identification(self):
        r"""
        This method do user authenticates via module client.py

        Parameters
        ----------
        login
            Text entered the object ``field_identification_login``.
        password
            Text entered the object ``field_identification_password``.
        run_client
            Run client.py module with parameters needs to authenticate.
        field_identification_status.setText
            Set text '\nUser does not exist or password wrong...' to the object ``field_identification_status``.
        model_contacts.setFilter('Error_filter')
            Set filter to the model ``model_contacts`` with text 'Error_filter'.
        model_history_messages.setFilter('Error_filter')
            Set filter to the model ``model_history_messages`` with text 'Error_filter'.
        model_contacts.setFilter(f'client="{self.login}"')
            Set filter to the model ``model_contacts`` with text ``f'client="{login}"'``.
        model_contacts.select()
            Fill data ``model_contacts`` model.
        field_identification_status.setText
            Set text 'User exist and password right...' to the object ``field_identification_status``.
        """
        self.login = self.field_identification_login.text()
        self.password = self.field_identification_password.text()
        run_client = subprocess.run(['python', '../client.py', '-n', f'{self.login}', '-s', f'{self.password}',
                                     '-d', f'{self.path_db}', '-r', 'graphic'], capture_output=True,
                                    universal_newlines=True).stdout
        if run_client == '\nUser does not exist or password wrong\n':
            self.field_identification_status.setText('\nUser does not exist or password wrong. '
                                                     'Identification not complete.')
            self.model_contacts.setFilter('Error_filter')
            self.model_history_messages.setFilter('Error_filter')
        else:
            self.model_contacts.setFilter(f'client="{self.login}"')
            self.model_contacts.select()
            self.field_identification_status.setText('User exist and password right. Identification complete.')

    def show_history(self, clicked_login):
        """
        This method fills and shows the message history in the field.

        Parameters
        ----------
        model_history_messages.setFilter
            Set filter to the model ``model_history_messages`` with text ``f'from_user in ("{clicked_login}", ...``.
        clicked_login
            Double-clicked login in field object ``list_contacts``.
        model_history_messages.select()
            Fill data ``model_history_messages`` model.
        """
        self.model_history_messages.setFilter(f'from_user in ("{clicked_login}", "{self.login}") and '
                                              f'whom_user in ("{clicked_login}", "{self.login}")')
        self.clicked_login = clicked_login
        self.model_history_messages.select()

    def add_contact(self):
        """
        This method adds contact in contact list via client.py module.

        Parameters
        ----------
        contact
            Text entered the object ``field_enter_contact``.
        run_client
            Run client.py module with the parameters needs to add a contact to the contact list.
        model_contacts.select()
            Fill data ``model_contacts`` model.

        Returns
        -------
        str
            Result works client.py module.
        """
        contact = self.field_enter_contact.text()
        run_client = subprocess.run(['python', '../client.py', '-n', f'{self.login}', '-s', f'{self.password}', '-d',
                                     f'{self.path_db}', '-r', 'graphic', '-c', f'{contact}'], capture_output=True,
                                    universal_newlines=True).stdout
        self.model_contacts.select()
        return run_client

    def send_message(self):
        """
        This method sends message addressee.

        Parameters
        ----------
        message
            Text entered the object ``field_enter_message``.
        run_client
            Run client.py module with the parameters needs to sends message addressee.
        model_history_messages.select()
            Fill data ``model_history_messages`` model.

        Returns
        -------
        str
            Result works client.py module.
        """
        message = self.field_enter_message.text()
        run_client = subprocess.run(['python', '../client.py', '-n', f'{self.login}', '-s', f'{self.password}', '-d',
                                     f'{self.path_db}', '-r', 'graphic', '-m', f'{message}', '-t',
                                     f'{self.clicked_login}'], capture_output=True, universal_newlines=True).stdout
        self.model_history_messages.select()
        return run_client


class ChatTableView(QTableView):
    """
    This class extend parent class ``QTableView`` new event signal.

    Methods
    -------
    get_clicked_login()
        Gets info about username through the clicked area.
    """

    double_clicked = pyqtSignal(str)  #: New signal.

    def __init__(self):
        """
        Constructor ``__init__`` extend parent and create new event signal.

        Parameters
        ----------
        doubleClicked.connect(get_clicked_login)
            Connect double-click event for calls method ``get_clicked_login``.
        """
        super(ChatTableView, self).__init__()
        self.doubleClicked.connect(self.get_clicked_login)

    def get_clicked_login(self, data):
        """
        This method gets info about username through the clicked area.

        Parameters
        ----------
        data
            Info about the clicked area.
        login
            Get username from the info about the clicked area.
        double_clicked.emit(login[0])
            Double-clicked event generation.
        """
        login = self.model().itemData(data)
        self.double_clicked.emit(login[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    adm = ClientChat()
    sys.exit(app.exec_())
