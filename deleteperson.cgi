#!/usr/bin/python3
# -*- coding: utf-8 -*-

from DeletePerson import DeletePerson

import cgi
import cgitb
cgitb.enable()

#Renders DeletePerson-page

page = DeletePerson()
page.renderPage()