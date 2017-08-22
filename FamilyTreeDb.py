# -*- coding: iso-8859-1 -*-

import cgi
import sqlite3

class FamilyTreeDb():
    """ Class containing the Family Tree Database. Communicates the database to the other files """
    
    def __init__(self): 
        """ Connects to Familytree.db """  
        self.conn = sqlite3.connect("Familytree.db")
        
    def close(self):
        """ Closes conection to db """
        self.conn.close()

    def createTables(self):
        """ Creates tables """
        try:
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE persons(personID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, birthDate TEXT, deathDate TEXT)")
            cursor.execute("CREATE TABLE relation(personID INTEGER, relationID INTEGER)")
          
            self.conn.commit()
        except:
            self.conn.rollback
           
            
    def insertPerson(self, name, birthDate, deathDate):
        try:          
            """ Insert a person into the persons-table """        
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO persons(name, birthDate, deathDate) VALUES(?, ?, ?)", (name, birthDate, deathDate))
                        
            self.conn.commit()
            return True
            
        except:
            self.conn.rollback()
            return None              

                
    def modifyPerson(self, name, newName, birthDate, deathDate):
        """ Modifies an existing person from the database. Based on their personID """
        
        personID = self.getPersonId(name)
        
        cursor = self.conn.cursor()
        cursor.execute("UPDATE persons SET name = ?, birthDate = ?, deathDate = ? WHERE personID = ?", (newName, birthDate, deathDate, personID))
        
        self.conn.commit()     


    def deletePerson(self, name):
        """ Deletes person from the database """

        personID = self.getPersonId(name)
        
        try:         
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM persons WHERE personID = ?", (personID, ))
            
            self.conn.commit()
            
        except:
            self.conn.rollback()
            return None
        
        
    def createRelationship(self, personName, parentName):
        """ Creates a relationship parent/children relationship between two persons by assigning parent to a person"""
        
        #Gets person ID from name.
        personID = self.getPersonId(personName)
        if personID == None:
            return False
        
        #Gets parent ID from name.
        parentID = self.getPersonId(parentName)
        
        if parentID == None:
            return False
        
        # Creates a connection between the two IDs
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO relation (personID, relationID) VALUES(?, ?)", (str(personID),str(parentID)))

            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            return False
    
    
    def getPersonId(self, name):
        """ Function that finds personID of a given forename, returns an integer or none """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT personID FROM persons WHERE name = ?", (name, ))
            self.conn.commit()
            personid = cursor.fetchone()
            return personid[0]
        
        except:
            self.conn.rollback()
            return None
        
    
    def getPersonInfo(self, name):
        """ Function that finds personID of a given forename, returns an integer or none """
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM persons WHERE name = ?", (name, ))
        self.conn.commit()
        return cursor.fetchone()
        
        
    def getPersonInfoFromID(self, personID):
        """ Retrieve information about a person from based on their personID. Returns a object from the Person class containing forename, surname, date of birth, date of death, fatherID, mother ID """ 
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT forename, surname, birthDate, deathDate, fatherID, motherID FROM persons WHERE personID = ?", (personID, ))
            self.conn.commit()
            
            (forename, surname, birthDate, deathDate, fatherID, motherID) = cursor.fetchone()
                    
        except:
            self.conn.rollback()
            return None
        
        
        
    def getParents(self, name):
        """ Returns the parents of a person based on their person object """

        personID = self.getPersonId(name)
        if personID == None:
            return None
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT persons.name FROM persons, relation WHERE relation.personID = ? AND persons.personID = relation.relationID", (personID, ))
        
        return self.deTuplifyList(cursor.fetchall()) 
    

    
    def getSiblings(self, name):
        """ Returns the siblings based on if they have the same parent """
            
        personID = self.getPersonId(name)
        if personID == None:
            return None
    
        cursor = self.conn.cursor()
        cursor.execute("SELECT persons.name FROM persons, relation WHERE persons.personID = relation.personID AND persons.personID != ? AND relation.relationID = (SELECT relation.relationID FROM relation WHERE relation.personID = ?)", (personID, personID))
           
        return self.deTuplifyList(cursor.fetchall())
             
    
    def getChildren(self, name):
        """ Returns the children of a person based on their person ID. Checks if the children has the person as a parent. """    
        personID = self.getPersonId(name)
        if personID == None:
            return None
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT persons.name FROM persons, relation WHERE persons.personID = relation.personID and relation.relationID = ?", (str(personID), ))
        
        return self.deTuplifyList(cursor.fetchall())       

 
    def getAllPersons(self):
        """ Returns a list of tuples of all the persons that the database contains """        
        try:
            cursor = self.conn.cursor()
            cursor.execute("select * FROM persons")
            self.conn.commit()
            persons = cursor.fetchall()  
            
            return persons
        
        except:
            self.conn.rollback()
            return None
        
        
    def getAllPersonNames(self):
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM persons")
            self.conn.commit()
            
            #Returns a list of tuples
            names = cursor.fetchall()                       
            #Creates a list of names
            names = self.deTuplifyList(names)   
            return names
        
        except:
            self.conn.rollback()
            return None    
                
        
    def deTuplifyList(self, listoftuples):
        result = []
        for tuple in listoftuples:
            result.append(tuple[0])
                          
        return result





