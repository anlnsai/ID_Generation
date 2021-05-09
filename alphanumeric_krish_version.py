# -*- coding: utf-8 -*-

import re

def getID(num, d=6):
    str_num = str(num)
    num_length = len(str_num)
    string = re.findall(r'[A-Z]+',str_num)
    string = (string[0]) if (len(string)>0) else ""
    
    if(num_length > d or str_num == "ZZZZZZ"):
        return ""
    
    if(str_num.count('9') == d):
        return 'A'+'0'*(d-1)
    
    if(string != ""):
        number = re.findall(r'\d+',str_num)
        number = number[0] if (len(number)>0) else ''
        if(number != ''):
            number = getID(number, d)   
            number = number[len(string):]
        if(number == '' or int(number) == 0):
            if(string[-1] != 'Z'):
                return string[:-1] + chr(ord(string[-1]) + 1) + number
            else:
                return  string + 'A' + number[:-1]                
        else:
            return string + number 
    elif(str_num.count('9') == num_length):
        str_num = str_num.replace("9", "0")
        return '{0:0{1}}'.format(int(str_num), d) 
    else:
        num = int(num) + 1
        return '{0:0{1}}'.format(num, d)
    


#i = 999999
#i = 'A00000'
#i = 'A00001'
#i = 'A99999'
#i = 'Z99999'
#i = 'ZA9999'
#i = 'ZZZZZ9'
#i = 'A00009'
#i = 'ZZZZA9'
#i = 'ZZZZZ9'
#i = 'A00000000'
#i = 'ZZZZZ9'
#i = 'ZZZZZA'
#i = 'ZZZZZC'
#alphanum = getID(i, 6)
#print(alphanum)


i = '0'

while(i != ""):
    alphanum = getID(i, 6)
    i = str(alphanum)
    print(alphanum)
