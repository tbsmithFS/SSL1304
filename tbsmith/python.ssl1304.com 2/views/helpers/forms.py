#!/usr/bin/python

class Helper():

    def login_form(self):

        return '''

<form action="/user/perform-login"
      enctype="multipart/form-data"
      method="post">

      Username: <input name="username"><br/>
      Password: <input type="password" name="password"><br/>
        <br/>
      <input type="submit">

</form>

'''


