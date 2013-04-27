#!/usr/bin/python

from models.view import View

class User():

    def get(self, query, data = {}):
        if 'action' not in query:
            action = 'home'
        else:
            action = query.getvalue('action')

        if action == 'home':
            self.home()
        elif action == 'login':
            self.login(data)
        elif action == 'register':
            self.register(data)
        
    def login(self, data):
        # login
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'}
        view_model.get_view('header', data)
        view_model.get_view('login', data)
        view_model.get_view('footer', data)
        
    def register(self, form_data={}, validation_data={}):
        # register
        view_model = View()
        view_model.print_header()
        data = {'username': 'tbsmith'} 
        view_model.get_view('header', data)
        view_model.get_view('register', form_data, validation_data)
        view_model.get_view('footer', data)

    def addUser(self, form_data={}):
        from views.helpers.form_validator import FormValidator
        form_validator = FormValidator()
        validation_data = form_validator.validate(form_data)
        return validation_data

    def show_success_page(self):
        print 'Registration Was A Success! And So Are You!'