#!/usr/bin/python

import settings.db

from models.view import View

view_model = View()

view_model.print_header()

data = {"site_title" : "Stockini.com",
        "logo_title" : "Stockini"
        }

view_model.get_view("header", data)
view_model.get_view("navbar", data)
view_model.get_view("home", data)
view_model.get_view("footer", data)


