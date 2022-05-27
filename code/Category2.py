#
#Author : Emmanuel Buruvuru
#Catergorey2.py : for the version control of the assignment 
#Refrences: 
#


class category2: 

    def HrsToMinMinToSec(time: int):   #mutiplying time 

        conversion = time * 60

        return conversion 

    def MinToHrsSecToMin(time: int):  #divinding time 

        conversion = time / 60

        return conversion

def saveData(filename, Hours, Minutes, Seconds):
    success = True 

    a = category2.MinToHrsSecToMin(Minutes) 
    b = category2.HrsToMinMinToSec(Minutes)
    c = category2.MinToHrsSecToMin(Seconds)
    d = category2.HrsToMinMinToSec(Hours)

    
    try:
        with open(filename, mode = "w") as writer: # Raises OSError
            writer.write("Hours to minutes: " + str(d) + "\n")
            writer.write("Minutes to Hours: " + str(a) + "\n")
            writer.write("Seconds to minutes: " + str(c) + "\n")
            writer.write("Minutes to seconds: " + str(b) + "\n")
                    
    except OSError:
        success = False
        
    return success

if __name__ == "__main__": 
    Hours = int(input("Enter Hours: ")) 
    Minutes = int(input('Enter minutes: ')) 
    Seconds = int(input('Enter seconds: '))
    filename = str('SavedData.txt')

    saveData(filename,Hours, Minutes, Seconds) 





