#!/usr/bin/python3
# -*- coding: utf-8 -*-

from AddRelation import AddRelation
import cgi
import cgitb
cgitb.enable()
import sys


page = AddRelation()
page.renderPage()