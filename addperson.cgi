#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()
from AddPerson import AddPerson

#Creates a menu page
page = AddPerson()

#Webpage prints menu
#renderPage is inherited from webpage
page.renderPage()