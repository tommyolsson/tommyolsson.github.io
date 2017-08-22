#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

from WebPage import WebPage
from WebUtils import *
from FamilyTreeDb import FamilyTreeDb
import cgitb
cgitb.enable()
import cgi
import sys


class ModifyPerson(WebPage):
    """ Imports user input and modifies a person then FamilyTreeDb gets that information and updates the database and webpage with it """ 
    
    def __init__(self):
        WebPage.__init__(self)
        
    def printBody(self):
        
        form = cgi.FieldStorage()
        name = form.getvalue('pdrop')
        
        if "newName" in form and "birthDate" in form and "deathDate" in form:
            newName = form.getfirst("newName")
            birthDate = form.getfirst("birthDate")
            deathDate = form.getfirst("deathDate")
             
            db = FamilyTreeDb()
            db.modifyPerson(name, newName, birthDate, deathDate)
            
            HTMLprint("<p>A person have been modified with the following information: Name: " + newName + " Date of birth: " + birthDate + " Date of death: " + deathDate)
            
            
        #Create droplist of users that can be modified. 
        print("""<form name="modify" action="modifyperson.cgi" method="post">""")
        
        beginTable()
        printTableHeader(["Select person for modification"])
 
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
        print("""<table style="width:25%">""")
        
        print("<tr>")

        print("<th>")
        print("Name")
        print("</th>")
        
        print("<th>")
        print("Date of birth")
        print("</th>")
        
        print("<th>")
        print("Date of death")
        print("</th>")
        
        print("</tr>")
        
        
        print("<tr>")
        print("<td>")
        print("""<input type="text" name="newName"><br />""")
        print("</td>")
       
        print("<td>")
        print("""<input type="text" name="birthDate", value = "YYYY-MM-DD"><br />""")
        print("</td>")
       
        print("<td>")        
        print("""<input type="text" name="deathDate", value = "YYYY-MM-DD"><br />""")
        print("</td>")     
        
        print("</tr>")
        print("</table>")
        
        print("""<br/>""")
        print("""<input type="submit" value="Modify the person">""")
        print("""</form>""")
        
        menuButton()