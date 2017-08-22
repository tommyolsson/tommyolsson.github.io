# -*- coding: iso-8859-1 -*- 

from WebPage import WebPage
from WebUtils import *
import cgitb
cgitb.enable()
import cgi
from FamilyTreeDb import FamilyTreeDb
import sys


class InfoPerson(WebPage):
    """ Prints out the information about a person regarding their name, date of birth, date of death, parents, siblings, children """
    
    def __init__(self):

        WebPage.__init__(self)
    
    
    def printBody(self):
                
        form = cgi.FieldStorage()
        
        # The first time this page is run no fields are filled in
        # Get data from fields
        
        name = form.getvalue('pdrop')
        
        #Prints information about the chosen person: InfoTable, parents, siblings and children
        if name:
            printHeader2("Information about " + name)
            
            db = FamilyTreeDb()
            person = db.getPersonInfo(name)
            
            db.close()
                       
            self.printPersonTable(person)
            verticalSpace(1)
            self.printParents(name)
            verticalSpace(1)
            self.printSiblings(name)
            verticalSpace(1)
            self.printChildren(name)
            verticalSpace(1)

            
            print("<hr>")            
        
                
        print('<form action="infoperson.cgi" method="post">')
        
     
        beginTable()
        printTableHeader(["Select person"])
 
        beginRow()
        beginCell()
        
        #Creates a droplist to choose user from      
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
        print("""<input type="submit" value="Show information about person">""")
        print("""</form>""")
        
        menuButton()


    def printPersonTable(self, person):       
        """ Prints table with the persons ID, Name, Date of birth and date of death """ 
        beginTable()
        printTableHeader(["ID", "Name", "Date of birth", "Date of death"])
        printTableRow([str(person[0]), str(person[1]), str(person[2]), str(person[3])])
        endTable()
        
        
    def printParents(self, person):      
        """ Prints out the parents of the person """
        db = FamilyTreeDb()
        parents = db.getParents(person)
        db.close()        
        
        printHeader3("Parents of " + person)

        if not parents:
            print("No known parents")
            return
        
        beginTable()
        
        for parent in parents:
            beginRow()
            beginCell()
            HTMLprint(str(parent))
            endCell()
            endRow()
            
        endTable()
    
    
    def printSiblings(self, person):
        """ Prints out the siblings of the person """
        db = FamilyTreeDb()
        siblings = db.getSiblings(person)
        db.close()        
        
        printHeader3("Siblings of " + person)
        
        if not siblings:
            print("No known siblings")
            return        
        
        beginTable()
        
        for sibling in siblings:
            beginRow()
            beginCell()
            HTMLprint(str(sibling))
            endCell()
            endRow()
            
        endTable()
        
        
    def printChildren(self, person):     
        """ Prints out the children of the person """ 
        db = FamilyTreeDb()
        children = db.getChildren(person)
        db.close()        
        
        printHeader3("Children of " + person)
        
        if not children:
            print("No known children")
            return        
        
        beginTable()

        for child in children:
            beginRow()
            beginCell()
            HTMLprint(str(child))
            endCell()
            endRow()
            
        endTable()
        
        
    def printTableOneColumn(self, header, elements):
        
        beginTable()
        
        printTableHeader([header])

        for element in elements:
            beginRow()
            beginCell()
            HTMLprint(str(element))
            endCell()
            endRow()
            
        endTable() 
        
        

    
        
        
        

