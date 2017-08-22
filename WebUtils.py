import sys

def enc_print(string='', encoding='utf8'):
    sys.stdout.flush() 
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

def HTMLprint(string):
    string2 = str(string.encode('ascii', 'xmlcharrefreplace'))
    string2 = string2[2:len(string2)-1]
    print(string2)
    
def verticalSpace(lines):
    for line in range(lines):
        print("<br>")
        
def printHeader1(string):
    HTMLprint("<h1>" + string + "</h1>")
    
def printHeader2(string):
    HTMLprint("<h2>" + string + "</h2>") 
    
def printHeader3(string):
    HTMLprint("<h3>" + string + "</h3>")     
    
def beginTable():
    print("""<table style="width:25%">""")
    
def endTable():
    print("</table>")
    
def beginRow():
    print("<tr>")

def endRow():
    print("</tr>")
    
def beginCell():
    print("<td>")
        
def endCell():
    print("</td>")    
    
def printTableHeader(list):
    print("<tr>")
    for colheader in list:
        print("<th>")
        HTMLprint(colheader)
        print("</th>")
    print("</tr>")

def printTableRow(list):
    print("<tr>")
    for cell in list:
        print("<td>")
        HTMLprint(cell)
        print("</td>")
    print("</tr>")
    
def beginDropDown(name):
    HTMLprint("<select name = " + name + ">")
    
def endDropDown():
    print("</select>")
    
def printOption(value, text):
    HTMLprint("<option value = '" + value + "'>" + text + "</option>")
           
def menuButton():
    print("""<p>""")
    print("""<form name="listpersons" action="listpersons.cgi" method="post">""")
    print("""<input type="submit" value="Return to menu">""")
    print("""</form>""") 