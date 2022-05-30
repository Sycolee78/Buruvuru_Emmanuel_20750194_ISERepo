#
#Author : Emmanuel Buruvuru
#Catergorey2.py : Module for time conversion of assignment two.  
#Refrences: 
#


class category2: 

    def HrsToMinMinToSec(time: int):   #Sub-module to mutiplying time to given conversion.

        if time < 0: 
            conversion = "input a positive int" 

        elif time == 0: 
            conversion = "Number should not be zero"

        else: 
            conversion = time * 60

        return conversion 

    def MinToHrsSecToMin(time: int):  #Sub-module that deals with divinding time  to a given conversion and returns a float

        if time < 0: 
            conversion = "input a positive int" 

        elif time == 0: 
            conversion = "Number should not be zero"
            
        else: 

            conversion = time / 60

        return conversion

def saveData(filename, Hours, Minutes, Seconds):
    success = True 

    a = category2.MinToHrsSecToMin(Minutes) 
    b = category2.HrsToMinMinToSec(Minutes)
    c = category2.MinToHrsSecToMin(Seconds)
    d = category2.HrsToMinMinToSec(Hours)

    
    try:
        with open(filename, mode = "w") as writer: 
            writer.write("Hours to minutes: " + str(d) + "\n")
            writer.write("Minutes to Hours: " + str(a) + "\n")
            writer.write("Seconds to minutes: " + str(c) + "\n")
            writer.write("Minutes to seconds: " + str(b) + "\n")
                    
    except OSError:       # Raises OSError
        success = False
        
    return success

if __name__ == "__main__": 
    Hours = int(input("Enter Hours: ")) 
    Minutes = int(input('Enter minutes: ')) 
    Seconds = int(input('Enter seconds: '))
    filename = str('SavedData.txt')

    saveData(filename,Hours, Minutes, Seconds) 





