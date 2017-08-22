#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi, cgitb
cgitb.enable()
import sys
from ModifyPerson import ModifyPerson
    
page = ModifyPerson()
page.renderPage()
