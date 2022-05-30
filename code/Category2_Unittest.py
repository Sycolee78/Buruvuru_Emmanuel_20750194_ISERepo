import unittest , sys , io ,os
import Category2 

class testCatergory2(unittest.TestCase): 

    def testflileinput(self):

        #setup  
        Hours = int(2) 
        Minutes = int(60) 
        Seconds = int(3600)
        filename = str('Correct_inputs.txt')
        Category2.saveData(filename, Hours, Minutes,Seconds)

        with open(filename) as outfile: 
            
            #Check the string in the file 
            self.assertEqual("Hours to minutes: 120\n" , outfile.readline()) 
            self.assertEqual("Minutes to Hours: 1.0\n" , outfile.readline()) 
            self.assertEqual("Seconds to minutes: 60.0\n" , outfile.readline()) 
            self.assertEqual("Minutes to seconds: 3600\n" , outfile.readline()) 


        #testing the modules with a range of negative numbers

        #setup  
        Hours = int(-2) 
        Minutes = int(-60) 
        Seconds = int(3600)
        filename = str('Negative_inputs.txt')
        Category2.saveData(filename, Hours, Minutes,Seconds)

        with open(filename) as outfile: 
            
            #Check the string in the file 
            self.assertEqual("Hours to minutes: input a positive int\n" , outfile.readline()) 
            self.assertEqual("Minutes to Hours: input a positive int\n" , outfile.readline()) 
            self.assertEqual("Seconds to minutes: 60.0\n" , outfile.readline()) 
            self.assertEqual("Minutes to seconds: input a positive int\n" , outfile.readline()) 


        #testing the modules using zero inputs 

        Hours = int(2) 
        Minutes = int(60) 
        Seconds = int(0)
        filename = str('Zero_input.txt')
        Category2.saveData(filename, Hours, Minutes,Seconds)

        with open(filename) as outfile: 
             
            #Check the strings in the file 
            self.assertEqual("Hours to minutes: 120\n" , outfile.readline()) 
            self.assertEqual("Minutes to Hours: 1.0\n" , outfile.readline()) 
            self.assertEqual("Seconds to minutes: Number should not be zero\n" , outfile.readline()) 
            self.assertEqual("Minutes to seconds: 3600\n" , outfile.readline()) 