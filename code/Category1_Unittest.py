
import unittest , sys , io ,os
import Category1

class testCategory1(unittest.TestCase): 

    def testLowertoUpper(self):

        string = "BURUVURU" 
        string2 = "emmanuel buruvuru"
        string3 = "0194"
        string4 = "Doctor Strange"
        
        assert "BURUVURU" == Category1.LowertoUpper(string)
        assert "EMMANUEL BURUVURU" == Category1.LowertoUpper(string2) 
        assert "0194" == Category1.LowertoUpper(string3) 
        assert "DOCTOR STRANGE" == Category1.LowertoUpper(string4) 


    def testUppertoLower(self): 
       
        string1 = "BURUVURU" 
        string2 = "emmanuel buruvuru"
        string3 = "0194"
        string4 = "Doctor Strange"
        
        assert "buruvuru" == Category1.UppertoLower(string1)
        assert "emmanuel buruvuru" == Category1.UppertoLower(string2)
        assert "0194" == Category1.UppertoLower(string3)
        assert "doctor strange" == Category1.UppertoLower(string4)
 

    def testifstringcontainsnumerics(self):

        string1 = "BURUVURU" 
        string2 = "emmanuel buruvuru"
        string3 = "0194"
        string4 = "Doctor Strange2"

        assert "False" == Category1.NumericsinStrings(string1)
        assert "False" == Category1.NumericsinStrings(string2)
        assert "True" == Category1.NumericsinStrings(string3)
        assert "True" == Category1.NumericsinStrings(string4)
 
    def testNumericsinstring(self): 

        #testing with a valid number 
        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("25")
        Category1.IsStringValid_number("25")
        self.assertEqual("String is a valid number..\n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        #testing with a string 
        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("emmanuel buruvuru")
        Category1.IsStringValid_number("emmanuel buruvuru")
        self.assertEqual("String is not a valid number..\n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        #testing with a valid number that containds letters 
        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("10.e")
        Category1.IsStringValid_number("10.e")
        self.assertEqual("String is a valid number..\n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__


    def testRemovenumricsfromstring(self): 

        #string without numerics
        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("emmanuel buruvuru")
        Category1.remove_numeric("emmanuel buruvuru")
        self.assertEqual("final string: EMMANUEL BURUVURU\n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        # testing with a string that has numeric values
        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("Doctor strange2")
        Category1.remove_numeric("Doctor Strange2")
        self.assertEqual("final string: DOCTOR STRANGE\n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        #testing with numeric values only 

        captureOut = io.StringIO()
        sys.stdout = captureOut
        sys.stdin = io.StringIO("0194")
        Category1.remove_numeric("0194")
        self.assertEqual("final string: \n",captureOut.getvalue())
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

       
if __name__ == '__main__': 
    testCategory1() 