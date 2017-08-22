#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ListPersons import ListPersons
import cgi
import cgitb
cgitb.enable()
import sys

""" Creates a menu page. WebPage prints out the menu, 	renderPage is inherited from WebPage """
page = ListPersons()
page.renderPage()