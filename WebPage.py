#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

import cgitb
cgitb.enable()
import cgi
import sys
import WebUtils

class WebPage():
    """Class that represents a empty webpage to be used as a template. 
       printBody may be overridden in subclasses to generate
       pages with content """
    
    def __init__(self):
        pass
    
    def renderPage(self):
        """ Prinss the entire page content from the other methods """
        self.printHeader()
        self.printBody()
        self.printFooter()
        
    def printHeader(self):
        """ Prints the header part of the page with HTML5 """
        print ('Content-type:text/html;charset=iso-8859-1;\r\n\r\n')
        print ('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html>
        <head> 
    
        <title>Family Tree</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />   
        
        <header class=" w3-opacity" style="padding:16px">
        
         
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        body,h1 {font-family: "Raleway", Arial, sans-serif}
        h1 {letter-spacing: 6px}
        .w3-row-padding img {margin-bottom: 12px}
        
        </style>

        </head>
        <body>''')
        
    def printBody(self):
        """ Prints the body part of the webpage. Could be overridden in subclass with content """
        pass
    
    def printFooter(self):
        """ Prints the footer page of the webpage """
        print ('''</body></html>''')       
    