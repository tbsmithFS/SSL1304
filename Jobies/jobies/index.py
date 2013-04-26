#!/usr/bin/python
print "Content-type: text/html\n\n"

import cgi
query = cgi.FieldStorage()
from controllers.word_service import SearchService

# More comprehensive traceback formatting for Python scripts
import cgitb
cgitb.enable()

ws = SearchService()

if 'page' in query and 'action' in query:
    page = query.getvalue('page')
    action = query.getvalue('action')
    searchTerm = query.getvalue('searchTerm')
else:
    page = 'home'
    action = 'search'
    searchTerm = 'Web Developer'

# if page is home do home stuff
if page == 'home':
  from controllers.home import Home
  Home().get(query)

# else if page is user do user stuff
elif page == 'user':
  from controllers.user import User
  user = User()
  # if no action in query set action default
  if 'action' not in query:
      action = 'show_register_form'
  # else set action var to action
  else:
      action = query.getvalue('action')

  # if action is show register form do that
  if action == 'show_register_form':
      user.show_register_form()

  # else if action is perfom register do that
  elif action == 'addUser':

  # else if action is perfom register do that
    validation_data = user.addUser(query)
    if validation_data['successful'] is True:
      user.show_success_page()
    else:
      user.show_register_form(query, validation_data)

  # else tell me what went wrong
  else:
    print "Didn't recognize action " + action

elif page == 'word_service':
  # page = 'home'
  if action == 'search':
    ws.search(searchTerm)

  # else default page to home (figure out a way to fix)
  # this is redundant
else:
  # default
  from controllers.home import Home
  Home().get(query)
