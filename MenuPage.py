from WebPage import WebPage
from WebUtils import *


class MenuPage(WebPage):
    """ Builds the main page of the website where the user can navigate from """
    
    def __init__(self):
        WebPage.__init__(self)
        
    def printBody(self):
        printHeader1("Family Tree") 
        
        print("""<table style="width:10%">""")
                
        print("<tr>")

        print("<th>")          
        print("""<form name="listpersons" action="listpersons.cgi" method="post">""")
        print("""<input type="submit" value="Click button to show family tree">""")
        print("""</form>""") 
        print("</th>")
        

        print("</tr>")

        print("</table>")              

    