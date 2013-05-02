#!/usr/bin/python

from models.view import View

class User():

    def get(self, query, data={}):
        if 'action' not in query:
            action == 'home'

        action = query.getvalue('action')
        if action == 'home':
            self.home(data)
        elif action == 'login':
            self.login(data)
        elif action == 'register':
            self.register(data)
        else:
            self.get_user_home(data)
        
    def login(self, data):
        # login
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'} 
        view_model.get_view('header', data)
        view_model.get_view('login', data)
        view_model.get_view('footer', data)
        
    def register(self, data):
        # register
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'} 
        view_model.get_view('header', data)
        view_model.get_view('register', data)
        view_model.get_view('footer', data)