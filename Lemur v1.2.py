from sys import *
import math

tokens = []
variables = {}
functions = ["echo","calculation_show","calculation_hide","assign_math","assign_string","math_echo", "increase_var", "decrease_var", "check", "returned_true", "input", "for", "breakfor", "echo_end_seperator", "end_echo", "seperator_echo", "end_seperator_echo"]

def lex(data):
    tokens = []
    tok = ""
    add = ""
    data = list(data)
    datalength = len(list(data))
    counter = 0
    for char in data:
        counter += 1
        tok += char
        if tok == "\n":
            tok = ""
        if "~" in tok:
            if not tok == "~":
                add = tok[0:len(tok)-1]
                tokens.append(add)
            tok = ""
        elif tok in functions:
            tokens.append(tok)
            tok = ""
        elif counter == len(data):
            tokens.append(tok)
    print(tokens)
    return tokens

def assignDATA(varname,varvalue):
    variables[varname] = varvalue

def assignDATASTRING(varname, string):
    variables[varname] = string

def increaseDATA(varname, increase):
    variables[varname] += increase

def decreaseDATA(varname, decrease):
    variables[varname] -= decrease

def getINPUT(text, varname):
    varvalue = input(text)
    variables[varname] = varvalue

def parse(data):
    input = ""
    i = 0
    sidea = 0
    sideb = 0
    istrue = ''
    repeatend = 999999999999999999999999999999999999999
    repeats = 0
    while (i < len(data)):
        if "echo" in data[i] and not "math" in data[i]:
            if "end" in data[i]:
                if "seperator" in data[i]:
                    if data[i+1][0] == "&":
                        print(str(variables[data[i+1][1:]]) + " ", end = '')
                    else:
                        print(str(data[i+1]) + " ", end = '')
                elif data[i+1][0] == "&":
                    print(str(variables[data[i+1][1:]]), end = '')
                else:
                    print(str(data[i+1]), end = '')
            elif "seperator" in data[i]:
                if data[i+1][0] == "&":
                    print(str(variables[data[i+1][1:]]) + " ", end = '')
                else:
                    print(str(data[i+1]) + " ", end = '')
            else:
                if data[i+1][0] == "&":
                    print(variables[data[i+1][1:]])
                else:
                    print(data[i+1])
            i+=2
        elif "calculate_show" in data[i]:
            print(eval(data[i+1]))
            calculation = eval(data[i+1])
            i+=2
        elif "calculate_hide" in data[i]:
            calculation = eval(data[i+1])
            i+=2
        elif "assign_math" in data[i]:
            assignDATA(data[i+1], eval(data[i+2]))
            i+=3
        elif "assign_string" in data[i]:
            assignDATASTRING(data[i+1], data[i+2])
            i+=3
        elif "increase_var" in data[i]:
            increaseDATA(data[i+1], eval(data[i+2]))
            i+=3
        elif "decrease_var" in data[i]:
            decreaseDATA(data[i+1], eval(data[i+2]))
            i+=3
        elif "math_echo" in data[i]:
            print(eval(data[i+1]))
            i+=2
        elif "else" in data[i]:
                if "break" in data:
                    while(data[i] != "break"):
                        i+=1
                else:
                    break
        elif "check"in data[i]:
            if data[i+1][0] == '&':
                sidea = int(eval(str(variables[data[i+1][1:]])))
            if data[i+3][0] == '&':
                sideb = int(eval(str(variables[data[i+3][1:]])))
            if data[i+1][0] != '&':
                sidea = int(eval(data[i+1]))
            if data[i+3][0] != '&':
                sideb = int(eval(data[i+3]))
            if int(sidea) == int(sideb) and data[i+2] == '=':
                istrue = "True"
            elif int(sidea) > int(sideb) and data[i+2] == '>':
                istrue = "True"
            elif int(sidea) < int(sideb) and data[i+2] == '<':
                istrue = "True"
            else:
                istrue = "False"
            if istrue == "False":
                if "break" in data:
                    while(data[i] != "break"):
                        i+=1
                else:
                    break
            else:
                i+=4
        elif data[i] == "for":
            repeatstart = i+2
            if data[i+1][0] == "&":
                repeats = variables[data[i+1][1:]]
            else:
                repeats = eval(data[i+1])
            tempi = i
            while("breakfor" not in data[tempi] or not tempi <= 999999999):
                tempi += 1
            repeatend = tempi
            sofar = 0
            i+=2
        elif i == repeatend:
            sofar += 1
            if not sofar >= repeats:
                i = repeatstart
        elif "break" in data[i]:
            i+=1
        
def run(command):
    data = lex(command)
    parse(data)

typeof = input("Use shell or import program? (write shell or program) > ")
if typeof == "shell":
    while True:
        run(input("lemur > "))
else:
    file = "/Users/kieranblackley/Downloads/Lemur Programming/LemurPrograms/" + input("Please specify a file name for your program: ")
    filecontent = open(file, "r").read()
    run(filecontent)
