import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
#Woked with Lucas, Andrew, Anastasia, Steve

#1. What statistical test would you use for the following scenarios? 

#(a) Does a student's current year (e.g., freshman, sophomore, etc.) effect their GPA?

    #Independent variable: Current Year - Categorical 
    #Dependent variable: GPA - Continous  
    #Statistical Test: T-Test
    

#(b) Has the amount of snowfall in the mountains changed over time? 

    #Independent variable: Amount of snowfall - Continous 
    #Dependent variable: Time - Continous  
    #Statistical Test: Generalized Regression

#(c) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer? 
    #Independent variable: Season - Categorical 
    #Dependent variable: Average Hikers - Continous  
    #Statistical Test: T-test

#(d) Does a student's home state predict their highest degree level?
    #Independent variable: Home state - Categorical 
    #Dependent variable: Degree Level - Categorical   
    #Statistical Test: Chi-Squred test

def generateDataset(filename):
    data = pd.read_csv(filename)
    df = data[0:]
    df = df.dropna()
    return data, df
    
def runTTest(ivA, ivB, dv):
    ttest = scipy.stats.ttest_ind(ivA[dv], ivB[dv])
    print(ttest)
    
    
def runAnova(data, formula):
    model = ols(formula, data).fit()
    aov_table= sm.stats.anova_lm(model, typ=2)
    print(aov_table)
    
def percentage(df):
    df['Total'] = df['Admitted'] + df['Rejected']
    df['Acceptance_R'] = df['Admitted']/df['Total']
    df['Rejection_R'] = df['Rejected']/df['Total']
    return df
    
    
rawData, df = generateDataset('simpsons_paradox.csv')

print("Does gender correlate with admissions?")

m = df[(df['Gender'] == 'Male')]
f = df[(df['Gender'] == 'Female')]
runTTest(m, f, 'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)

print("Do gender AND department correlate with admissions?")
moreComplex = 'Admitted ~ C(Department) + C(Gender)'
runAnova(rawData, moreComplex)


#Does gender correlate with admissions?
#Ttest_indResult(statistic=5.332277756733584, #pvalue=0.001774285663548817)
#Does department correlate with admissions?
                  #sum_sq   df         F    PR(>F)
#C(Department)   92266.75  5.0  0.737438  0.622205
#Residual       150141.50  6.0       NaN       NaN
#Do gender AND department correlate with admissions?
                      #sum_sq   df          F    PR(>F)
#C(Department)   41153.333333  5.0   7.515304  0.036670
#C(Gender)      145760.750000  2.0  66.546025  0.000851

# Based on the p_value (lower than 0.05), I'd conclude that the reuslt was not very bias. Additionally, I think "gender"  appear to contribute most heavily to admissions.

#Problem 3:
#Answer: The data quality issue was that the test was analysing "Admit", and "reject" separately. We will have to combine the total number of "admit" and "reject". then use that combined rate to check the acceptance rate. Total/adimitted. They are similar in the results of "Does department correlate with admission". On the other hand the p-value was different.




























