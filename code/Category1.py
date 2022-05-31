#
#Author : Emmanuel Buruvuru
#Catergorey1.py : for String conversion and manipulation.
#Refrences: 
#


def LowertoUpper(string: str): 
    
    a = string.upper()
    
    return a

def UppertoLower(string: str): 

    b = string.lower()
    
    return b

def NumericsinStrings(string: str):

    res = True if next((chr for chr in string if chr.isdigit()), None) else False 

    if res == True: 
        return "True"

    else: 
        return "False"
    

def IsStringValid_number(string: str):

    i = 0
    j = len(string) - 1

    if (i == j and not(string[i] >= '0' and 
                    string[i] <= '9')):
        return False

    # If the 1st char is not '+', '-', '.' or digit
    if (string[i] != '.' and string[i] != '+' and 
        string[i] != '-' and not(string[i] >= '0' and 
        string[i] <= '9')):
        return print("String is not a valid number..")

    DotorE = False

    for i in range(j + 1):
        
        if (string[i] != 'e' and string[i] != '.' and 
            string[i] != '+' and string[i] != '-' and not
        (string[i] >= '0' and string[i] <= '9')):
            return print("String is not a valid number..")

        if string[i] == '.':
            
            if DotorE or i + 1 > len(string) or (not(string[i + 1] >= '0' and string[i + 1] <= '9')):
                return print("String is a valid number..")
        elif string[i] == 'e':
            
            DotorE = True

            if (not(string[i - 1] >= '0' and 
                    string[i - 1] <= '9')):
                return False

            if i + 1 > len(string):
                return False

            if (string[i + 1] != '+' and string[i + 1] != '-' and 
            (string[i + 1] >= '0' and string[i] <= '9')):
                return False
                
    return print("String is a valid number..")


def remove_numeric(string: str): 

    res = ''.join([i for i in string if not i.isdigit()])
    

    return print("final string:", res.upper())






  