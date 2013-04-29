#!/usr/bin/python
# print "Content-type: text/html\n\n"
import cgi
query = cgi.FieldStorage()
from controllers.search_service import SearchService
searchService = SearchService()

print "Content-Type: text/html\n"


if 'page' in query and 'action' in query:
  page = query.getvalue('page')
  action = query.getvalue('action')
  searchTerm = query.getvalue('searchTerm')
else:
  page = 'home'
  action = 'search'
  searchTerm = 'Web Developer'

print ("PAGE : " + page)

if page == 'home':
  from controllers.home import Home
  Home().get(query)

elif page == 'user':
  from controllers.user import User
  user = User()

  if 'action' not in query:
    action = 'register'
  else:
    action = query.getvalue('action')

  print "ACTION : " + action

  if action == 'register':
    user.register()

  elif action == 'login':
    user.login(query)  

  elif action == 'addUser':
    # validation_data = user.addUser(query)
    user.addUser("A","A","1");
    # if validation_data['successful'] is True:
    #   user.show_success_page()
    # else:
    #   user.show_register_form(query, validation_data)

  else:
    print "Didn't recognize action " + action

elif page == 'search_service':
  if action == 'search':
    searchService.search(searchTerm)

else:
  # default if no page specified
  from controllers.home import Home
  Home().get(query)