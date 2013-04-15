#!/usr/bin/python

from models.view import View

class Home():
    def get(self, pairs, data={}):

        if 'action' not in pairs:
            action = 'home'
        else:
            action = pairs.getvalue('action')

        view_model = View()
        view_model.print_header()
        view_model.get_view("header", data)
        view_model.get_view("navbar", data)

        if action == 'home':
            view_model.get_view('home', data)
        elif action == 'contact':
            view_model.get_view('contact', data)
        elif action == 'faqs':
            view_model.get_view('faqs', data)
        elif action == 'errors':
            view_model.get_view('errors', data)


        view_model.get_view("footer", data)


