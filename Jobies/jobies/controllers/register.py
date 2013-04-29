#!/usr/bin/python

from views.helpers.form_builder import FormBuilder

class Register():

    def __init__(self, form_data={}, validation_data={}):
        self.form_data = form_data
        self.validation_data = validation_data
        print '<body> <h2>Register Page!<h2>'

        # form = FormBuilder(self.validation_data, self.form_data)
        # form.formHeader('/user/register')
        # form.textInput('name')
        # form.textInput('email')
        # form.textInput('verifyemail')
        # form.textInput('password', True)
        # form.submit()
        # form.formCloser()

        form = FormBuilder(self.validation_data, self.form_data)
        form.formHeader('/user/register')
        form.textInput('userName')
        form.textInput('type','1,2,3')
        form.textInput('verifyemail')
        form.textInput('password', True)
        form.submit()
        form.formCloser()

        print '</body> </html>'