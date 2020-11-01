import numpy as np
import scipy.stats

def testStatistic( data, mu0, sigma ) : 
  # Your code to compute the testStatistic that is described
  # in the text on the right should be calculated here
  
def twoTailTest( data, mu0, sigma ) :
  T = testStatistic( data, mu0, sigma )
  # Your code to perform the two tail test goes here
  
  
def meanLessTest( data, mu0, sigma  ) :
  T = testStatistic( data, mu0, sigma )
  # Your code to perform the less than test goes here
  
  
def meanMoreTest( data, mu0, sigma ) :
  T = testStatistic( data, mu0, sigma )
  # Your code to perform the more than test goes here
  
# The null hypothesis should not be rejected for all the tests below
samples = np.random.normal(0,1,size=50)
print( twoTailTest(samples, 0, 1) )
print( meanLessTest(samples, 0, 1) )
print( meanMoreTest(samples, 0, 1) )
