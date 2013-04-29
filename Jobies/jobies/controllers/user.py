#!/usr/bin/python

from models.view import View
from controllers.register import Register
from models.DBConnector import DBConnector

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
        view_model.get_view('header')
        view_model.get_view('login', data)
        view_model.get_view('footer')
        
    def register(self, form_data={}, validation_data={}):
        # register
        view_model = View()
        view_model.print_header()
        view_model.get_view('header')
        register = Register()
        #view_model.get_view('register', data)
        #view_model.get_view('register', form_data, validation_data)
        view_model.get_view('footer')

    def addUser(self, name='', password='', typeId=''):
        # from views.helpers.form_validator import FormValidator
        # form_validator = FormValidator()
        # validation_data = form_validator.validate(form_data)
        # return validation_data

        # DBConnector().update_user("Alyssa","Thomas")
        # DBConnector().delete_user(1182392)
        view_model = View()
        view_model.print_header()
        view_model.get_view('header')

        # DBConnector().addUser("A","A","1")

        db = DBConnector().getConnection()

        sql = "INSERT INTO Users (name,password,typeId) VALUES(%(name)s, %(password)s, %(typeId)s);"

        user_info = {
            'name': name,
            'password': password,
            'typeId': typeId
        }
    
        cursor = db.cursor()
        cursor.execute(sql, user_info)
        db.commit()
        print 'my sql : '+sql
        cursor.close()
        db.close()

    def show_success_page(self):
        print 'Registration Was A Success! And So Are You!'