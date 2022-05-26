#
#Author : Emmanuel Buruvuru
#Catergorey1.py : for the version control of the assignment 
#Refrences: 
#

import string


class category: 

    def UppertoLower(string: str) : 
        
        a = string.upper()
        
        return a

    def LowertoUpper(string: str): 

        b = string.lower()
        
        return b

    def NumericsinStrings(string: str):

        res = True if next((chr for chr in string if chr.isdigit()), None) else False

        if res == True: 
            print("The string contains a numeric value :) ")

        else: 
            print("The string does not contain a numeric value :( ")
        

    def IsStringValid(string: str): 

        numeric = ["0","1","2","3","4","5","6","7","8","9"]

        for i in numeric:
            for j in string:  
                if i == j: 
                    print("The string is numneric value..")

                else:
                    
                    print("The string is  not  a numneric value..")

        return

    def valid_number(string: str):

        i = 0
        j = len(string) - 1
    
        while i<len(string) and string[i] == ' ':
            i += 1
        while j >= 0 and string[j] == ' ':
            j -= 1
    
        if i > j:
            return False

        if (i == j and not(string[i] >= '0' and 
                        string[i] <= '9')):
            return False
    
        # If the 1st char is not '+', '-', '.' or digit
        if (string[i] != '.' and string[i] != '+' and 
            string[i] != '-' and not(string[i] >= '0' and 
            string[i] <= '9')):
            return False
    
        flagDotOrE = False
    
        for i in range(j + 1):
            
            if (string[i] != 'e' and string[i] != '.' and 
                string[i] != '+' and string[i] != '-' and not
            (string[i] >= '0' and string[i] <= '9')):
                return False
    
            if string[i] == '.':
                
                if flagDotOrE:
                    return False
                if i + 1 > len(string):
                    return False
                if (not(string[i + 1] >= '0' and 
                        string[i + 1] <= '9')):
                    return False
            elif string[i] == 'e':
                
                flagDotOrE = True
    
                if (not(string[i - 1] >= '0' and 
                        string[i - 1] <= '9')):
                    return False

                if i + 1 > len(string):
                    return False
 
                if (string[i + 1] != '+' and string[i + 1] != '-' and 
                (string[i + 1] >= '0' and string[i] <= '9')):
                    return False
                    
        return True


    def remove_numeric(sting: str): 
  
        res = ''.join([i for i in string if not i.isdigit()])
        
        print("final string : ", res)

        a = str(input("Do you want to convert the string to (U)pper or (L)ower case: ")).upper() 

        if a == 'U':

            conversion = res.upper() 

        elif a == 'L': 

            conversion = res.lower() 

        else: 
            print("Enter U to convert to Upper\n Enter L to conver to Lower: ")

        return conversion 

if __name__ == '__main__': 
    string = input("Enter a String to convert: ")       
    a = category.valid_number(string)

    print("The string converted is -> ", a)  




  