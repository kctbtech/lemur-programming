from sys import *
import math
import random

tokens = []
variables = {}
functions = ["echo","calculation_show","calculation_hide","assign_math","assign_string","math_echo", "var_increase", "var_decrease", "if", "returned_true", "input", "for", "breakfor", "echo_end_seperator", "end_echo", "seperator_echo", "end_seperator_echo", "task", "breaktask", "2for", "break2for", "get_num_input", "get_string_input", "get_random", "get_letter", "return_letter", "to", "assign_substring", "assign_replacement", "in", "with", "replace", "join", "and", "assign_join", "breakif", "loop_forever", "&&"]
defines = {}
define_end = {}
varnames = []

def lex(data):
    tokens = []
    tok = ""
    add = ""
    data = list(data)
    datalength = len(list(data))
    counter = 0
    isSeperator = 1
    for char in data:
        counter += 1
        tok += char
        if "\n" in tok:
            tok = tok.replace("\n", "")
            tokens.append(tok.replace("\"", ""))
            tok = ""
        if tok == "\"":
            if isSeperator == 1:
                isSeperator = 0
            else:
                isSeperator = 1
        elif isSeperator == 0:
            if tok[len(tok)-1] == "\"":
                isSeperator = 1
        if " " in tok and isSeperator == 1:
            if not tok == " ":
                add = tok[0:len(tok)-1]
                add = add.replace("\"", "")
                tokens.append(add)
            tok = ""
        elif tok in functions:
            tokens.append(tok)
            tok = ""
        elif counter == len(data):
            tokens.append(tok)
    return tokens

def calculate(calc):
    final = str(calc)
    for item in varnames:
        final = final.replace(str(item), str(variables[item[1:]]))
    return int(eval(str(final)))

def assignDATA(varname,varvalue):
    variables[varname[1:]] = varvalue
    varnames.append(varname)

def assignDATASTRING(varname, string):
    variables[varname[1:]] = string
    varnames.append(varname)

def increaseDATA(varname, increase):
    variables[varname] += int(increase)
    varnames.append(varname)

def decreaseDATA(varname, decrease):
    variables[varname] -= decrease
    varnames.append(varname)

def getINPUT(text, varname):
    varvalue = input(text)
    variables[varname] = varvalue
    varnames.append(varname)

def parse(data):
    inputted = ""
    i = 0
    leftside = 0
    rightside = 0
    istrue = ''
    repeatend = 999999999999999999999999999999999999999
    repeats = 0
    newi = 0
    oldi = 0
    substring = ""
    string = ""
    randomnum = 0
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
            print(calculate(data[i+1]))
            calculation = calculate(data[i+1])
            i+=2
        elif "calculate_hide" in data[i]:
            calculation = calculate(data[i+1])
            i+=2
        elif "assign_math" in data[i]:
            assignDATA(data[i+1], calculate(data[i+2]))
            i+=3
        elif "assign_string" in data[i]:
            assignDATASTRING(data[i+1], data[i+2])
            i+=3
        elif "assign_num_var" in data[i]:
            assignDATA(data[i+1], int(variables[data[i+2][1:]]))
            i+=3
        elif "assign_string_var" in data[i]:
            assignDATASTRING(data[i+1], str(variables[data[i+2][1:]]))
            i+=3
        elif "assign_substring" in data[i]:
            assignDATASTRING(data[i+1], substring)
            i+=2
        elif "assign_replacement" in data[i]:
            assignDATASTRING(data[i+1], replacement)
            i+=2
        elif "assign_join" in data[i]:
            assignDATASTRING(data[i+1], outcome)
            i+=2
        elif data[i] == "return_join":
            print(outcome)
            i+=1
        elif data[i] == "return_replacement":
            print(replacement)
            i+=1
        elif data[i] == "return_substring":
            print(substring)
            i+=1
        elif data[i] == "join":
            if data[i+1][0] == "&":
                a = str(variables[data[i+1][1:]])
            else:
                a = str(data[i+1])
            if data[i+3][0] == "&":
                b = str(variables[data[i+3][1:]])
            else:
                b = str(data[i+3])
            outcome = a + b
            i+=4
        elif data[i] == "replace":
            if data[i+3][0] == "&":
                string = variables[data[i+3][1:]]
            else:
                string = str(data[i+3])
            if data[i+1][0] == "&":
                toreplace = variables[data[i+1][1:]]
            else:
                toreplace = str(data[i+1])
            if data[i+5][0] == "&":
                replacewith = variables[data[i+5][1:]]
            else:
                replacewith = str(data[i+5])
            string = string.replace(str(toreplace), str(replacewith))
            if data[i+3][0] == "&":
                assignDATASTRING(data[i+3][1:], string)
            else:
                print(string)
            replacement = string
            i+=6
        elif "var_increase" in data[i]:
            if data[i+2][0] == "&":
                increaseDATA(data[i+1][1:], variables[data[i+2][1:]])
            else:
                increaseDATA(data[i+1][1:], calculate(data[i+2]))
            i+=3
        elif "var_decrease" in data[i]:
            if data[i+2][0] == "&":
                decreaseDATA(data[i+1][1:], variables[data[i+2][1:]])
            else:
                decreaseDATA(data[i+1][1:], calculate(data[i+2]))
            i+=3
        elif "math_echo" in data[i]:
            print(calculate(data[i+1]))
            i+=2
        elif "else" in data[i]:
                if "breakif" in data:
                    while(data[i] != "breakif"):
                        i+=1
                else:
                    break
        elif data[i] == "if" and not "breakif" in data[i]:
            count = 0
            while data[i] != 'then':
                old = istrue
                if data[i+1][0] == '&':
                    leftside = int(calculate(variables[data[i+1][1:]]))
                if data[i+3][0] == '&':
                    rightside = int(calculate(variables[data[i+3][1:]]))
                if data[i+1][0] != '&':
                    leftside = int(calculate(data[i+1]))
                if data[i+3][0] != '&':
                    rightside = int(calculate(data[i+3]))
                if int(leftside) == int(rightside) and data[i+2] == '=':
                    istrue = "True"
                elif int(leftside) != int(rightside) and data[i+2] == '!=':
                    istrue = "True"
                elif int(leftside) > int(rightside) and data[i+2] == '>':
                    istrue = "True"
                elif int(leftside) < int(rightside) and data[i+2] == '<':
                    istrue = "True"
                else:
                    istrue = "False"
                    break
                if old != istrue and count != 0:
                    break
                count += 1
                i+=4
            i-=4
            if istrue == "False":
                if "breakif" in data:
                    while(data[i] != "breakif"):
                        i+=1
                else:
                    break
            else:
                i+=5
        elif "else" in data[i]:
                if "breakif" in data:
                    while(data[i] != "breakif"):
                        i+=1
                else:
                    break
        elif data[i] == "sif" and not "breaksif" in data[i]:
            count = 0
            while data[i] != 'then':
                old = istrue
                if data[i+1][0] == '&':
                    leftside = str(variables[data[i+1][1:]])
                if data[i+3][0] == '&':
                    rightside = str(variables[data[i+3][1:]])
                if data[i+1][0] != '&':
                    leftside = str(data[i+1])
                if data[i+3][0] != '&':
                    rightside = str(data[i+3])
                if str(leftside) == str(rightside) and data[i+2] == '=':
                    istrue = "True"
                elif str(leftside) != str(rightside) and data[i+2] == '!=':
                    istrue = "True"
                elif str(leftside) > str(rightside) and data[i+2] == '>':
                    istrue = "True"
                elif str(leftside) < str(rightside) and data[i+2] == '<':
                    istrue = "True"
                else:
                    istrue = "False"
                    break
                if old != istrue and count != 0:
                    break
                count += 1
                i+=4
            i-=4
            if istrue == "False":
                if "breakif" in data:
                    while(data[i] != "breakif"):
                        i+=1
                else:
                    break
            else:
                i+=5
        elif "get_random" in data[i]:
            randomnum = random.randint(int(data[i+1]), int(data[i+3]))
            assignDATA(data[i+4], randomnum)
            i+=4
        elif data[i] == "for":
            repeatstart = i+2
            if data[i+1][0] == "&":
                repeats = variables[data[i+1][1:]]
            else:
                repeats = calculate(data[i+1])
            tempi = i
            while("breakfor" not in data[tempi] or not tempi <= 999999999):
                tempi += 1
            repeatend = tempi
            sofar = 0
            i+=2
        elif data[i] == "breakfor":
            sofar += 1
            if not sofar >= int(repeats):
                i = repeatstart
            else:
                i+=1
                sofar = 0
        elif data[i] == "loop_forever":
            foreverstart = i+1
            i+=1
        elif data[i] == "break":
            i = foreverstart
        elif data[i] == "get_substring":
            if data[i+1][0] == "&":
                string = str(variables[data[i+1][1:]])
            else:
                string = str(data[i+1])
            if data[i+3] == "to":
                if data[i+4][0] == "&":
                    string = str(variables[data[i+4][1:]])
                else:
                    string = str(data[i+1])
            if data[i+4][0] == "&":
                end = variables[data[i+4][1:]]
            else:
                end = data[i+4]
            if data[i+2][0] == "&":
                start = variables[data[i+2][1:]]
            else:
                start = data[i+2]
            if data[i+3] == "to":
                substring = str(string[int(calculate(str(start))):int(calculate(str(end)))])
                i+=2
            else:
                substring = str(string[calculate(str(start))])
            i+=3
        elif data[i] == "return_letter":
            print(letter)
            i+=1
        elif data[i] == "2for":
            irepeatstart = i+2
            if data[i+1][0] == "&":
                irepeats = variables[data[i+1][1:]]
            else:
                irepeats = calculate(data[i+1])
            itempi = i
            while("breakfor" not in data[itempi] or not itempi <= 999999999):
                itempi += 1
            irepeatend = itempi
            isofar = 0
            i+=2
        elif data[i] == "break2for":
            isofar += 1
            if not isofar >= int(irepeats):
                i = irepeatstart
            else:
                i+=1
                isofar = 0
        elif data[i] == "3for":
            iirepeatstart = i+2
            if data[i+1][0] == "&":
                iirepeats = variables[data[i+1][1:]]
            else:
                iirepeats = calculate(data[i+1])
            iitempi = i
            while("breakfor" not in data[iitempi] or not iitempi <= 999999999):
                iitempi += 1
            iirepeatend = iitempi
            iisofar = 0
            i+=2
        elif data[i] == "break3for":
            iisofar += 1
            if not iisofar >= int(iirepeats):
                i = iirepeatstart
            else:
                i+=1
                iisofar = 0
        elif data[i] == "task":
            defines[data[i+1]] = i+2
            tempi = i+2
            while (data[i] != "breaktask"):
                i+=1
            define_end[tempi] = i
            i+=1
        elif data[i][1:] in defines:
            if data[i][0] != "$":
                print("WRONG INDICATOR. USE \"$\".")
            newi = defines[data[i][1:]]
            oldi = i
            i = newi
        elif "get_num_input" in data[i]:
            inputted = input(data[i+1])
            assignDATA(data[i+2], int(inputted))
            i+=3
        elif "get_string_input" in data[i]:
            inputted = input(data[i+1])
            assignDATA(data[i+2], str(inputted))
            i+=3
        elif i == len(data):
            print("Finishing.")
        elif "breaktask" in data[i]:
            i = oldi
            i+=1
        elif "breakfor" in data[i]:
            i+=1
        elif "breakif" in data[i]:
            i+=1
        elif "breaksif" in data[i]:
            i+=1
        elif data[i] == "":
            i+=1
def run(command):
    data = lex(command)
    parse(data)
    print("Run task complete.")
    print(defines)

typeof = input("Use shell or import program? (write shell or program) > ")
if typeof == "shell":
    while True:
        run(input("lemur > "))
else:
    file = "/Users/kieranblackley/Downloads/Lemur Programming/LemurPrograms/" + input("Please specify a file name for your program: ")
    filecontent = open(file, "r").read()
    run(filecontent)
