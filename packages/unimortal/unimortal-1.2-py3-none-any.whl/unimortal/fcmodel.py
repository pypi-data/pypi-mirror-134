# function for Forecast models
import numpy as np
import pandas as pd
from pathlib import Path, PurePath
from unimortal import PACKAGEDIR
from unimortal import utils
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import warnings

def time_series(df,xaxs):
    
    """
    This is an internal function to plot time series from with in the prediction models
    It plots graph with year on x axis and Mortatlity rate y axis
    
    This function is not available for user to invoke directly.
    """
    
    # values on x-axis
    y = df['Mor_rate']
    y=y.iloc[::-1] 
    # values on y-axis
    x =xaxs[3:]
    x.reverse()  
    

    # naming the x and y axis
    plt.xlabel('Year')
    plt.ylabel('Mortality Rate')

    # plotting a line plot with it's default size
    
    plt.plot(x, y)
    plt.show()
    
def autoreg(df, country, tp, sex, lg):
    
    """
    This function predicts the mortality rate for years 2020 to 2024 
    using autoregression modeling, AutoReg model - 'AutoReg(data,lg)'.
    
    The 'years' in dataset ('wide' format) are extracted by using 'list(row1F.iloc[0,3:14])'.
    
    In order to have the 'years' in ascending order, not descending order 
    as it is in the original dataset, they are read in reverse order by using 'data[::-1]'.
    
    As the dataset contains 11 years (from 2009 to 2019), so the predicted years (up to 
    2024) are put in order from 12 to 16, 'ARmodel_fit.predict(12,16)'
    
    Parameters: 
    df - This parameter accepts a pandas data frame. 
    The data frame which is received from invoking extract_dataset(country, df, sex) function should be passed here.

    country - This parameter accepts a country name, for which the user is interested in looking at predictions. 
    Country name should be written with first capital letter.

    tp parameter specifies the filetype that accepts numeric value 1 or 2, where 
    1 indicates Infant mortality rate dataset and  
    2 indicates Child mortality rate (aged 1-4 years) dataset 

    Sex - This parameter accepts a single character- 'F','M','A' 
    F- Female (extract only Female data)
    M- Male (extract only Male data)
    A- All (Total)

    lg - This parameter indicates lag for the AR model. It accepts a single integer number.
    """
    row1 = df[df.country == country]
    
    if tp == 1:
        age_type='Infant mortality rate'
    elif tp == 2:
        age_type='Child mortality rate (aged 1-4 years)'
    else:
        print('Invalid type')
        return 'Invalid type'
        
    if sex == 'F':
        sex_type='Female'
    elif tp == 2:
        sex_type='Male'
    else:
        sex_type='Total'
        
    row1 = row1[row1.type == age_type]  
    row1F = row1[row1.sex == sex_type]
    
    xaxs=list(row1F.columns)
    df_long_t=utils.wide_to_long(row1F)
    time_series(df_long_t,xaxs)
    
    warnings.filterwarnings("ignore") 
    try:
        
        data = list(row1F.iloc[0,3:14])
        data = data[::-1]
        ARmodel = AutoReg(data,lg)
        ARmodel_fit = ARmodel.fit()
        y_predict = ARmodel_fit.predict(12,16)
        print('aic= ', ARmodel_fit.aic, 'bic= ', ARmodel_fit.bic, 'hqic= ', ARmodel_fit.hqic)
        return 'The Predicted Estimate of '+age_type+' for '+sex_type+' from year 2020 to 2024 is '+ str(y_predict)
    
    except ValueError:
        print('Error in parameters')
    else:
        print('Error in execution of model')
        
def movavg(df, country, tp, sex, ord):
    
    """
    This function predicts the mortality rate for years 2020 to 2024 using 
    the Autoregressive Moving Average, ARMA model - 'ARMA(data,order=ord)'.
    
    The procedure of this function is similar to the procedure in the 'autoreg()' function,
    the difference is in using 'ARMA(data,order=ord))' function instead of 'AutoReg(data,lg)'.
    
    The predicted years (2020 to 2024) are put in order from 12 to 16, 'MAmodel_fit.predict(12,16)'.
    
    Parameters: 
    df - This parameter accepts a pandas data frame. 
    The data frame which is received from invoking extract_dataset(country, df, sex) function should be passed here.

    country - This parameter accepts a country name, for which the user is interested in looking at predictions. 
    Country name should be written with first capital letter.


    tp parameter specifies the filetype that accepts numeric value 1 or 2, where 
    1 indicates Infant mortality rate dataset and  
    2 indicates Child mortality rate (aged 1-4 years) dataset 
    

    Sex - This parameter accepts a single character- 'F','M','A' 
    F- Female (extract only Female data)
    M- Male (extract only Male data)
    A- All (Total)

    ord - This parameter indicates order for the moving average model. It accepts a tuple of two values, e.g. (0,1)
    
    In ARMA(p,q) model p is the order of the autoregressive polynomial,
    and q is the order of the moving average polynomial.
    """
    
    row1 = df[df.country == country]
    if tp == 1:
        age_type='Infant mortality rate'
    elif tp == 2:
        age_type='Child mortality rate (aged 1-4 years)'
    else:
        print('Invalid type')
        return 'Invalid type'
    
    
    if sex == 'F':
        sex_type='Female'
    elif tp == 2:
        sex_type='Male'
    else:
        sex_type='Total'
        
    
    row1 = row1[row1.type == age_type]  
    row1F = row1[row1.sex == sex_type]
    xaxs=list(row1F.columns)
    df_long_t=utils.wide_to_long(row1F)
    time_series(df_long_t,xaxs)
    
    warnings.filterwarnings("ignore")    
    try:
        data = list(row1F.iloc[0,3:14])
        data = data[::-1]
        MAmodel = ARMA(data,order=ord)
        MAmodel_fit = MAmodel.fit()
        y_predict = MAmodel_fit.predict(12,16)
        print('aic= ', MAmodel_fit.aic, 'bic= ', MAmodel_fit.bic, 'hqic= ', MAmodel_fit.hqic)
        return 'The Predicted Estimate of '+age_type+' for '+sex_type+' from year 2020 to 2024 is '+ str(y_predict)
    except ValueError:
        print('Error in parameters')
    except NotImplementedError: 
        print('''The ARMA version might have been deprecated in current statsmodels version on this system. 
              This will be handled in our future releases''')   
    else:
        print('Error in execution of model')
        

def movavgintg(df, country, tp, sex,ord):
    
    """
    This function predics the mortality rate for years 2020 to 2024 using 
    the Autoregressive Integrated Moving Average (ARIMA model) - 'ARIMA(data,order=ord)'.
    
    The procedure of this function is similar to the procedure in the 'autoreg()' function,
    the difference is in using 'ARIMA(data,order=ord)' instead of 'AutoReg(data,lg)'.
    
    The predicted years (2020 to 2024) are put in order from 12 to 16, 'MAmodel_fit.predict(12,16)'.
    
    Parameters: 
    df - This parameter accepts a pandas data frame which is received from invoking 
    'extract_dataset(country, df, sex)'.

    country - This parameter accepts a country name, for which the user is interested in looking at predictions. 
    Country name should be written with first capital letter.
    
    tp parameter specifies the filetype that accepts numeric value 1 or 2, where 
    1 indicates Infant mortality rate dataset and  
    2 indicates Child mortality rate (aged 1-4 years) dataset 
    
    Sex - This parameter accepts a single character- 'F','M','A' 
    F- Female (extract only Female data)
    M- Male (extract only Male data)
    A- All (Total)

    ord - This parameter indicates order for the moving average model. It accepts a tuple of three values, e.g. (0,1,1)
    
    In ARIMA(p,d,q) p is the order of the autoregressive model (number of time lags), d is 
    the degree of differencing (the number of times the data have had past values subtracted),
    and q is the order of the moving-average model.
    
    """
    row1 = df[df.country == country]
    
    if tp == 1:
        age_type='Infant mortality rate'
    elif tp == 2:
        age_type='Child mortality rate (aged 1-4 years)'
    else:
        print('Invalid type')
        return 'Invalid type'
    
    if sex == 'F':
        sex_type='Female'
    elif tp == 2:
        sex_type='Male'
    else:
        sex_type='Total'
        
    row1 = row1[row1.type == age_type]  
    row1F = row1[row1.sex == sex_type]
    
    xaxs=list(row1F.columns)
    df_long_t=utils.wide_to_long(row1F)
    time_series(df_long_t,xaxs)
    
    warnings.filterwarnings("ignore")
    try:
        data = list(row1F.iloc[0,3:14])
        data = data[::-1]
        MAmodel = ARIMA(data,order=ord)
        MAmodel_fit = MAmodel.fit()
        y_predict = MAmodel_fit.predict(12,16)
        print('aic= ', MAmodel_fit.aic, 'bic= ', MAmodel_fit.bic, 'hqic= ', MAmodel_fit.hqic)
        return 'The Predicted Estimate of '+age_type+' for '+sex_type+' from year 2020 to 2024 is '+ str(y_predict)
    except ValueError:
        print('Error in parameters')
    else:
        print('Error in execution of model')