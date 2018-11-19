
import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
#Woked with Lucas, Andrew

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
    
    
rawData, df = generateDataset('simpsons_paradox.csv')

print("Does gender correlate with admissions?")

m = df[(df['Gender'] == 'Male')]
f = df[(df['Gender'] == 'Female')]
runTTest(m, f, 'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)


#Ttest_indResult(statistic=5.332277756733584, pvalue=0.001774285663548817)

 #P value is less than 0.05, so I will reject the null hypothesis

#I would say the analysis is very bias, since the training data is very accurate

 #Also I don't think they are very correlated


























