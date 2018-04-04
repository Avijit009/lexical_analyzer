import re
import sys


#Reading from file
inputfile = 'input.txt'
code = open(inputfile)

#Defining output file
outputfile = open("output.txt", "w") 

#For removing comment
def remove_comment(line):
    def replacer(match):
        subs = match.group(0)
        if subs.startswith('/'):
            return " "
        else:
            return subs
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    
    return re.sub(pattern, replacer, line)

stringL = remove_comment(code.read())
#print (stringL)
#print('\n')
#outputfile.write("-------------------------------------------------------------\n")
outputfile.write("\t\t" "After Removing Comment""\t\t\t\t\t\n\n")
#outputfile.write("-------------------------------------------------------------\n")
outputfile.write(stringL)
outputfile.write('\n\n')

#For finding keyword
keywords = ['auto','break','case','char','const','continue','default',
          'do','double','else','enum','extern','float','for','goto',
          'if','int','long','register','return','short','signed',
          'sizeof','static','struct','switch','typedef','union',
         'unsigned','void','volatile','while']

def is_keyword(token):
    if token in keywords:
        return True
    else:
        return False
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#For finding symbol
symbol = {'@' : 'at the rate of', 
      '#' : 'Hash symbol',
      '$' : 'Dollar symbol',
      '%' : 'Percentage',
      '^' : 'Power symbol', 
      '(' : 'Parenthesis open',
      ')' : 'Parenthesis close',
      '<' : 'Less than',
      '>' : 'Greater than',
      '{' : 'Karli brace open',
      '{' : 'Karli brace close',
      '[' : 'Square bracket open',
      '[' : 'Square bracket close',
      '/' : 'Forward slash',
      '\\' : 'Backward slash',
      '&' : 'Ampersand',
      ';' : 'Semicolon',
      ',' : 'Comma'}

symbol_k = symbol.keys()
#print(symbol_k)

def is_symbol(token):
     if token in symbol_k:
         return True
     else:
         return False

#for finding operator      
operator = { '+' : 'Plus symbol',
             '-' : 'Minus',
             '*' : 'Multiplication',
             '=' : 'Assignment',
             '/' : 'Division',
             '!' : 'Not',
             '%' : 'Reminder'}
operator_k = operator.keys()
print(operator_k)

def is_operator(token):
     if token in operator_k:
         return True
     else:
         return False

listL = []


stringL = re.sub("include.*.h", "", stringL, flags=re.DOTALL)
stringL = re.sub("printf", "", stringL, flags=re.DOTALL)
stringL = re.sub("scanf", "", stringL, flags=re.DOTALL)
stringL = re.sub('".*?.%.?."', "", stringL, flags=re.DOTALL)


for line in stringL.split():
    #for word in line.split():
    listL.append(line)

#print("Lexemes" "\t\t" "Token Name" "\t" "Attribute Value\n")
#outputfile.write("-------------------------------------------------------------\n")
outputfile.write("\t Keyword,Variable,Special Symbol,Number \t\n\n")
#outputfile.write("-------------------------------------------------------------\n\n")

outputfile.write("-------------------------------------------------------------\n")
outputfile.write("Lexemes" "\t\t" "Token Name" "\t" "Attribute Value\n")


for token in listL:
    outputfile.write("-------------------------------------------------------------\n")
    if is_keyword(token):
        #print(token + '\t\t' + token +'\t\t'+ "-")
        #pass
        outputfile.write(token + '\t\t' + token +'\t\t'+ "-"+"\n")
        
    elif is_number(token):
        #print(token +"\t\t"+"number"+ "\t\tconstant")
        #pass
        outputfile.write(token +"\t\t"+"number"+ "\t\tconstant"+"\n")
        
    elif is_symbol(token):
        #print(token + '\t\tspecial symbol'  + "\t" + symbol[token])
        #pass
        outputfile.write(token + '\t\tspecial symbol'  + "\t" + symbol[token]+"\n")
        
    elif is_operator(token):
        #print(token + '\t\toperator'  + "\t" + operator[token])
        #pass
        outputfile.write(token + '\t\toperator'  + "\t" + operator[token]+"\n")
        
    else:
        if token == 'main':
            #print(token + '\t\t' + "id" +'\t\t'+ "-")
            outputfile.write(token + '\t\t' + "id" +'\t\t'+ "-"+"\n")
            
        else:
             #print(token + '\t\t' + "id" +'\t\t'+ "Pointer to symbol table entry")
             outputfile.write(token + '\t\t' + "id" +'\t\t'+ "Pointer to symbol table entry"+"\n")
outputfile.write("-------------------------------------------------------------\n")

outputfile.close()
