#!/usr/bin/python

import cgi

pairs = cgi.FieldStorage()

if 'controller' not in pairs:
    con = 'home'
else:
    con = pairs.getvalue('controller')

if con == 'home':
    from controllers.home import Home
    Home().get(pairs)
elif con == 'news':
    from controllers.news import News
    News().get(pairs)
elif con == 'user':
    from controllers.user import User
    User().get(pairs)
else:
    # default
    from controllers.home import Home
    Home().get(pairs)


