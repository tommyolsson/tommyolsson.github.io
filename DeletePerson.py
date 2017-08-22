#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

from WebPage import WebPage
from WebUtils import *
from FamilyTreeDb import FamilyTreeDb
import cgi
import cgitb
cgitb.enable()
import sys


class DeletePerson(WebPage):
    """ Deletes a person from the database by using FamilyTreeDb that updates the database and webpage. """
    
    def __init__(self):
        WebPage.__init__(self)
    
    
    def printBody(self):     
        
        form = cgi.FieldStorage()    
        name = form.getvalue('pdrop')
        
        if name:
            db = FamilyTreeDb()
            db.deletePerson(name)
            db.close()
            
            HTMLprint("<p>" + name + " have been deleted from the database.</p>")
        
        #Create droplist of users that can be removed.     
        print("""<form action="deleteperson.cgi" method="post">""")
        
        beginTable()
        printTableHeader(["Select person for deletion"])
 
        beginRow()
        beginCell()
        
        beginDropDown("pdrop")
        
        db = FamilyTreeDb()
        names = db.getAllPersonNames()
        db.close()
                      
        for name in names:
            printOption(name, name)
                                      
        endDropDown()

        endCell()
        endRow()

        endTable()
        
        print("""<br />""")
        print("""<input type="submit" value="Delete person">""")
        print("""</form>""")
        
        menuButton()