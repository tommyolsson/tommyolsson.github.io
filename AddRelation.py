#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

from WebPage import WebPage
from WebUtils import *
from FamilyTreeDb import FamilyTreeDb
import cgi
import cgitb
cgitb.enable()
import sys


class AddRelation(WebPage):
    """Creates a parent/child relation between two persons"""

    def __init__(self):
        WebPage.__init__(self)
    
    def printBody(self):
        """Prints the body content of the page """
        form = cgi.FieldStorage()
        
        person = form.getvalue('persondrop')
        father = form.getvalue('fatherdrop')
        mother = form.getvalue('motherdrop')
        
        if person and father:
            db = FamilyTreeDb()
            db.createRelationship(person, father)
            db.close()
        
        if person and mother:
            db = FamilyTreeDb()
            db.createRelationship(person, mother)
            db.close()

            HTMLprint("<p> " + person + " have been assigned the father " + father + " and the mother " + mother)
               
        printHeader2("Assign parents to a person")
        
        print('<form action="addrelation.cgi" method="post">')
        
        db = FamilyTreeDb()
        persons = db.getAllPersonNames()
        parents = db.getAllPersonNames()
        db.close()
        
        beginTable()
        
        print("<tr>")
        

        print("<th>")
        print("Person")
        print("</th>")
        
        print("<th>")
        print("Father")
        print("</th>")
        
        print("<th>")
        print("Mother")
        print("</th>")        
        
        print("</tr>")
        
        print("<tr>")
        print("<td>")
        
        #Droplist for person
        beginDropDown("persondrop")
        
        for name in persons:
            printOption(name, name)
        endDropDown()
        print("</td>")
       
        print("<td>")
        
        #Droplist for parent
        beginDropDown("fatherdrop")
        
        for name in parents:
            printOption(name, name)
            
        endDropDown()
        
        print("</td>")
        
        print("<td>")     
        #Droplist for parent
        beginDropDown("motherdrop")
        
        for name in parents:
            printOption(name, name)
            
        endDropDown()
        
        print("</td>")        
        
        print("</tr>")
        endTable()
        
        print("""<br/>""")
        print("""<input type="submit" value="Confirm parents">""")
        print("""</form>""")
        
        menuButton()