# Standardizing

If you understood the last exercise you are doing really well as the analysis of __statistical power__ is really quite difficult.   It is important, however, because although we fix the probability for a type I error when we set the significance level there can still be type II errors.  The likelihood of a type II error decreases when you perform the hypothesis test using a greater number of data points.  Our intuition that we can have more certainty in our results if we perform experiments more times is thus correct.  

Over the last few tasks, we have established that working with these probabilities directly is hard.  We can avoid these difficulties, however, by standardizing the methods that we use when we do these tests.  If these methods are standardized quantities such as the statistical power can then be tabulated for us to look up.  With that in mind lets now think about how we can standardize the functions we have used to perform the following three  hypothesis tests:

![](https://render.githubusercontent.com/render/math?math=H_0:\mu=\mu_0\quad\H_0:\mu=\mu_0\quad\H_0:\mu=\mu_0)

![](https://render.githubusercontent.com/render/math?math=H_1:\mu\ne\mu_0\quad\H_1:\mu>\mu_0\quad\H_1:\mu<\mu_0)

In writing this we have introduced the symbols ![](https://render.githubusercontent.com/render/math?math=H_0) and ![](https://render.githubusercontent.com/render/math?math=H_1) for the null and alternative hypotheses respectively.  ![](https://render.githubusercontent.com/render/math?math=\mu_0), meanwhile, is the value of the expectation that we were given in the statement of the problem.  In these expressions, ![](https://render.githubusercontent.com/render/math?math=\mu) is the sample mean that has been computed in the usual way.  Now instead of using the sample mean as the test statistic, we are going to use:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^{n}(X_i-\mu_0))

where ![](https://render.githubusercontent.com/render/math?math=\sigma) is the square root of the variance for the random variable.  You should add code in the function `testStatistic` to make it compute and return this quantity.  Three variables are passed to this function:

1. `data` is a numpy array that contains `n` normal random variables 
2. `mu0` is the value of the expectation for the distribution that is assumed under the null hypothesis
3. `sigma` is the square root of the variance for the distribution that is assumed under the null hypothesis

Notice that in calculating T we have performed a standardizing transformation on the sample mean that we have been computing in the previous exercises.  Under the assumption of the null hypothesis the sample mean is a sample from the following normal distribution:

![](https://render.githubusercontent.com/render/math?math=\mu=N\left(\mu_0,\frac{\sigma}{\sqrt{n}}\right))

If we subtract ![](https://render.githubusercontent.com/render/math?math=\mu_0) and divide by ![](https://render.githubusercontent.com/render/math?math=\sigma/\sqrt{N}) as we have done in the calculation of T above we thus have a sample from a standard normal distribution with expectation 0 and variance 1.

__In addition to completing the function to calculate the `testStatistic` you must then call this function within each of the three functions for performing hypothesis tests.__  Each of these functions tasks four arguments:

1. `data` is a NumPy array that contains N normal random variables 
2. `mu0` is the value of the expectation for the distribution that is assumed under the null hypothesis
3. `sigma` is the square root of the variance for the distribution that is assumed under the null hypothesis
4. `sig` is the significance level you would like to use for the test.

The functions should then return a string that tells you whether the null hypothesis is rejected or not for a test at a 5% significance level.  For all three functions, the null hypothesis is that data is a set of samples from a normal distribution with expectation ![](https://render.githubusercontent.com/render/math?math=\mu_0) and standard deviation ![](https://render.githubusercontent.com/render/math?math=\sigma). The alternative hypotheses are then:

1. `twoTailTest` - that the expectation is not equal to ![](https://render.githubusercontent.com/render/math?math=\mu_0)
2. `meanLessTest` - that the expectation is less than ![](https://render.githubusercontent.com/render/math?math=\mu_0)
3. `meanMoreTest` - that the expectation is greater than ![](https://render.githubusercontent.com/render/math?math=\mu_0)
