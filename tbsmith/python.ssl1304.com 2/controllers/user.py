#!/usr/bin/python

from models.view import View

class User():

    def get(self, pairs, data={}):

        if 'action' not in pairs:
            get_user_home()
        else:
            action = pairs.getvalue('action')
            if action == 'home':
                self.get_user_home(data)
            elif action == 'start-edit':
                self.start_edit(data)
            elif action == 'perform-edit':
                self.perform_edit(data)
            elif action == 'login':
                self.login(data)
            elif action == 'register':
                self.register(data)
            else:
                self.get_user_home(data)
                

    def get_user_home(self, data):

        view_model = View()
        view_model.print_header()
        view_model.get_view('header', data)
        view_model.get_view('navbar', data)

        data = {'username': 'tbsmith'} 
        view_model.get_view('user_home', data)

        view_model.get_view('footer', data)

    def start_edit(self, data):

        pass
        # show edit input fields

    def perform_edit(self, data):

        pass
        # change user data

        # show notification of successful update

        self.get_user_home(data)
        
    def login(self, data):
        # login
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'} 
        view_model.get_view('header', data)
        view_model.get_view('navbar', data)
        view_model.get_view('login', data)
        view_model.get_view('footer', data)
        
    def register(self, data):
        # register
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'} 
        view_model.get_view('header', data)
        view_model.get_view('navbar', data)
        view_model.get_view('register', data)
        view_model.get_view('footer', data)
