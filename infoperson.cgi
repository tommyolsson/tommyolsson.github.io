#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()
import sys
from InfoPerson import InfoPerson

page = InfoPerson()
page.renderPage()