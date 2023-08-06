# function for plots
import numpy as np
import pandas as pd
#import seaborn as sns 
from unimortal import PACKAGEDIR
import matplotlib.pyplot as plt

def comp_sex(df,filetype): 
    '''This function shows a graphical representation of the mortality rate for males and females
    using a bar plot (double bar plot).
    
    The function takes two parameters, 'df' and 'filetype', where the first one is a dataset of interest
    and the second one takes either number 1 (for infants) or number 2 (for children aged 1 to 4 years).
    
    Pivoting is useful when the dataset needs to be reorganised according to one attribute.

    In this case we are interested in how mortality changes for different sex according to various years.

    A pivoted dataset, that was in 'long' format, was obtained by using 'pivot_table()' method.
    
    'iloc' is used to slice the dataset where 'iloc[:,:-1]' shows the dataset without the last column, 'Total',
    only 'Male' and 'Female'are selected.
    
    In this way the extracted dataset is presented graphically as a bar plot using 'plot()' method.
    '''
    
    if filetype == 1:  #infants
        plot1 = df.pivot_table(index='year', columns='sex').iloc[:,:-1].plot(kind='bar',
                                                      y='Mor_rate', 
                                                      title='Infants',
                                                      ylabel='Mortality Rate',
                                                      xlabel='Year',
                                                      color=('magenta','blue'))
    elif filetype == 2:  #children aged 1 to 4 
        plot1 = df.pivot_table(index='year', columns='sex').iloc[:,:-1].plot(kind='bar',
                                                      y='Mor_rate', 
                                                      title='Children aged 1 to 4',
                                                      ylabel='Mortality Rate',
                                                      xlabel='Year', 
                                                      color=('magenta','blue'))
        
    return plot1


    
def see_total(df,filetype): 
    '''This function shows a graphical representation of the mortality rate for males and females
    together ('Total') using a horizontal bar plot.
    
    The function takes two parameters, 'df' and 'filetype', where the first one is a dataset of interest
    and the second one takes either number 1 (for infants) or number 2 (for children aged 1 to 4 years).
    
    A pivoted dataset, that was in 'long' format, was obtained by using 'pivot_table()' method.
    
    'iloc' is used to slice the dataset where 'iloc[:,-1:]' slices the dataset in such way that 
    only the last column is selected, 'Total'.
    
    In this way the extracted dataset is presented graphically as a bar plot using 'plot()' method
    where "kind='barh'" indicates that this is a horizontal bar plot.
    '''
    if filetype == 1:  # infants
        #df = df_long_1
        plot2 = df.pivot_table(index='year', columns='sex').iloc[:,-1:].plot(kind='barh',
                                                      y='Mor_rate', 
                                                      #title=string,
                                                      title='Infants',                   
                                                      ylabel='Mortality Rate',
                                                      xlabel='Year',
                                                      color=('red'))
    elif filetype == 2:  # children aged 1 to 4 
        plot2 = df.pivot_table(index='year', columns='sex').iloc[:,-1:].plot(kind='barh',
                                                      y='Mor_rate', 
                                                      title='Children aged 1 to 4',
                                                      ylabel='Mortality Rate',
                                                      xlabel='Year', 
                                                      color=('red'))
    return plot2