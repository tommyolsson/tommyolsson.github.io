from WebPage import WebPage
from WebUtils import *

import cgitb
cgitb.enable()
import cgi
from FamilyTreeDb import FamilyTreeDb
import sys

class ListPersons(WebPage):
    """ Prints out a list of all persons in the database. Prints buttons to navigate to the sites other pages"""
    
    def __init__(self):
        WebPage.__init__(self)
        
    def printBody(self):
        
        db = FamilyTreeDb()
        persons = db.getAllPersons()
        db.close()
            
        print("<h1>List of all persons in the family tree</h1>")

        print("""<table style="width:25%">""")
        
        print("<tr>")

        print("<th>")
        print("ID: ")
        print("</th>")

        print("<th>")
        print("Name: ")
        print("</th>")
        
        print("<th>")
        print("Date of birth: ")
        print("</th>")        
        
        print("<th>")
        print("Date of death: ")
        print("</th>")              
        
        print("</tr>")

        for person in persons:
            print("<tr>")
            
            print("<td>")
            HTMLprint(str(person[0]))
            print("</td>")
           
            print("<td>")        
            HTMLprint(str(person[1]))
            print("</td>")
            
            print("<td>")        
            HTMLprint(str(person[2]))
            print("</td>")      
            
            print("<td>")        
            HTMLprint(str(person[3]))
            print("</td>")                   
        
            print("</tr>")
            
        print("</table>")
        
        
        self.printButtons()  

        print("""<p>""")  
        print("""<form name="menu" action="index.cgi" method="post">""")
        print("""<input type="submit" value="Return to startpage">""")
        print("""</form>""")           


    def printButtons(self):

        print("""<table style="width:10%">""")
        print("<tr>")
        
        print("<th>")        
        print("""<p>""")     
        print("""<form name="infoperson" action="infoperson.cgi" method="post">""")
        print("""<input type="submit" value="Info about person">""")
        print("""</form>""")   
        print("</th>") 
        
        print("<th>")    
        
        print("""<p>""")
        print("""<form name="addperson" action="addperson.cgi" method="post">""")
        print("""<input type="submit" value="Add a new person">""")
        print("""</form>""")
        print("</th>")        
        
        print("<th>")        
        print("""<p>""")
        print("""<form name="menu" action="addrelation.cgi" method="post">""")
        print("""<input type="submit" value="Assign parents">""")
        print("""</form>""")         
        print("</th>")        

        print("<th>")        
        print("""<p>""")
        print("""<form name="menu" action="modifyperson.cgi" method="post">""")
        print("""<input type="submit" value="Modify person">""")
        print("""</form>""")         
        print("</th>")
        
        print("<th>")    
        print("""<p>""")
        print("""<form name="menu" action="deleteperson.cgi" method="post">""")
        print("""<input type="submit" value="Delete person">""")
        print("""</form>""")                   
        print("</th>")
        print("</tr>")

        print("</table>")
