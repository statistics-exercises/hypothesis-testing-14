import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        for n in range(1,21) :
            mu, sigma = -10 +n, 0.1*n
            samples = np.random.normal(mu, sigma, size=20*n )
            stat = ( sum(samples) / (20*n) - mu ) / ( sigma / np.sqrt(n*20) )
            self.assertTrue( np.abs( stat - testStatistic( samples, mu, sigma) )<1e-7, "your funciton for calculating the test statistic is not working correctly")
            
    def test_twoTailTest(self) :
        self.assertTrue( inspect.getsource(twoTailTest).find("if")>0, "your function for the two tail test does not contain an if statement" )
        samples = np.random.normal(0,1,size=50)
        m1 = twoTailTest( samples, 0, 1 )
        self.assertTrue( m1=="there is insufficient evidence to reject the null hypothesis", "your function for the two tail test is not working correctly")
        m2 = twoTailTest( [-4], 0, 1 )
        self.assertTrue( m2=="the null hypothesis is rejected in favour of the alternative", "your function for the two tail test is not working correctly" )
        m3 = twoTailTest( [4], 0, 1 )
        self.assertTrue( m3=="the null hypothesis is rejected in favour of the alternative", "your function for the two tail test is not working correctly" )
        
   def test_meanLessThan(self) : 
       self.assertTrue( inspect.getsource(meanLessTest).find("if")>0, "your function for testing if the mean is less than does not contain an if statement"  )
       samples = np.random.normal(0,1,size=50)
       m1 = twoTailTest( samples, 0, 1 )
       self.assertTrue( m1=="there is insufficient evidence to reject the null hypothesis", "your function for testing if the mean is less than is not working correctly")
       m2 = twoTailTest( [-4], 0, 1 )
       self.assertTrue( m2=="the null hypothesis is rejected in favour of the alternative", "your function for testing if the mean is less than is not working correctly" )
       
   def test_meanMoreThan(self) : 
       self.assertTrue( inspect.getsource(meanMoreTest).find("if")>0, "your function for testing if the mean is more than does not contain an if statement" )
       samples = np.random.normal(0,1,size=50)
       m1 = twoTailTest( samples, 0, 1 )
       self.assertTrue( m1=="there is insufficient evidence to reject the null hypothesis", "your function for testing if the mean is more than is not working correctly")
       m3 = twoTailTest( [4], 0, 1 )
       self.assertTrue( m3=="the null hypothesis is rejected in favour of the alternative", "your function for testing if the mean is more than is not working correctly" )
