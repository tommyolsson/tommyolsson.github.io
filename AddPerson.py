#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

from WebPage import WebPage
from WebUtils import *
from FamilyTreeDb import FamilyTreeDb
import cgi
import cgitb
cgitb.enable()
import sys


class AddPerson(WebPage):
    """ Imports user input and creates a person, FamilyTreeDb gets that information and updates the database webpage with it """ 
    
    def __init__(self):
        WebPage.__init__(self)
        
    def printBody(self):
        
        form = cgi.FieldStorage()
        
        #The first time this page is run no fields are filled in
        if "name" in form and "birthDate" in form and "deathDate" in form:
            name = form.getfirst("name")
            birthDate = form.getfirst("birthDate")
            deathDate = form.getfirst("deathDate")
            
            db = FamilyTreeDb()
            db.insertPerson(name, birthDate, deathDate)
            db.close()
            
            HTMLprint("<p>A person have been added with the following information:<p> Name: " + name + "<p>  Date of birth: " + birthDate + "<p> Date of death: " + deathDate)           
               
        print("<h1>Add a new person</h1>")

        print("""<form name="addperson" action="addperson.cgi" method="post">""")
        
        print("""<table style="width:25%">""")
        
        print("<tr>")

        print("<th>")
        print("Full name")
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
        print("""<input type="text" name="name"><br />""")
        print("</td>")
       
        print("<td>")
        print("""<input type="text" name="birthDate", value = "YYYY-MM-DD"><br />""")
        print("</td>")
       
        print("<td>")        
        print("""<input type="text" name="deathDate", value = "YYYY-MM-DD"><br />""")
        print("</td>")
               
                
        print("</td>")            
        
        print("</tr>")
        print("</table>")
        
        print("""<br />""")
        print("""<input type="submit" value="Add the person">""")
        print("""</form>""")
        
        menuButton()
