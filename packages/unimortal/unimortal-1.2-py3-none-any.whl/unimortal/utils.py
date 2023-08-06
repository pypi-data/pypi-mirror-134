# function for utilities
import numpy as np
import pandas as pd
from pathlib import Path, PurePath
from unimortal import PACKAGEDIR
import warnings


def load_dataset(filetype):
    
    """
    This function is used to load the dataset. This will be the first and compulsory function to execute when using the package.
    
    This function reads the dataset that is in 'xlsx' format in excel by using 'pd.read_excel()'
    and changes it to 'Comma Separated Values' (CSV) format by using 'read_file.to_csv()', that is 
    a plain text format in which values are separated by commas. 
    
    The final dataset in CSV format is given a variable name 'df'.
    
    An 'if' statement is used as the user may choose one of two types of datasets where 
    number 1 represents the dataset with infants' mortality ratio and number 2 represents the dataset
    with mortality of children aged 1 to 4 years. 
    
    The user's choice must be typed in the place of 'filetype' in 'load_dataset(filetype)' function.
    
    After reading the dataset according to the user's choice the dataset, 'df', is cleaned by 
    using the function 'clean_dataset()' and then returned in the cleaned form.

    Parameters:

    filetype - parameter accepts numeric value 1 or 2, where 1 indicates Infant mortality rate dataset and  
    2 indicates Child mortality rate (aged 1-4 years) dataset
    """
     
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")    
    
    if filetype == 1:  #infant
        file_name = dirname + '/package_data/GLOBAL_DATAFLOW_infant_2009-2019.xlsx'    
        new_file_name = dirname + '/package_data/csv_infant_2009-2019.csv'   
        read_file = pd.read_excel (file_name)
        read_file.to_csv (new_file_name, index = None, header=True)
        df = pd.read_csv (new_file_name)
    
    elif filetype == 3: # age 1 to 4
        
        file_name = dirname + '/package_data/GLOBAL_DATAFLOW_5to14_2009-2019.xlsx'    
        new_file_name = dirname + '/package_data/csv_5to14_2009-2019.csv'   
        read_file = pd.read_excel (file_name)
        read_file.to_csv (new_file_name, index = None, header=True)
        df = pd.read_csv (new_file_name)
        
    elif filetype == 2: # age 5 to 14
        
        file_name = dirname + '/package_data/GLOBAL_DATAFLOW_under5_2009-2019.xlsx'    
        new_file_name = dirname + '/package_data/csv_under5_2009-2019.csv'   
        read_file = pd.read_excel (file_name)
        read_file.to_csv (new_file_name, index = None, header=True)
        df = pd.read_csv (new_file_name)
    
    df = clean_dataset(df,filetype)    
    return df
    
def clean_dataset(df,filetype):
    
    """
    This function is used to clean the dataset. This will be invoked from with in load_dataset function.
    
    This function is cleaning the dataset by removing unwanted first two rows at the top 
    of the dataset and the last six rows at the bottom of the dataset by using 'drop()' method
    in which 'axis=0' indicates that it is removing rows not columns and the 'index' shows the 
    lists of the removed rows.
    
    Also, three columns needed to be renamed, by using 'rename()' method, either by changing 
    the name ('Time period' was changed for 'country') or added a name if they were unnamed 
    originaly (i.e. 'sex' and 'type').

    Parameters:
    The df parameter accepts pandas dataframe which is downloaded by invoking load_dataset(filetype)
    
    The filetype parameter accepts numeric value 1 or 2, where 1 indicates Infant mortality rate dataset and  
    2 indicates Child mortality rate (aged 1-4 years) dataset.
    """
    
    df = df.drop(index=[0,1],axis=0)
    df = df.drop(index=[695,696,697,698,699,700],axis=0)
    df.rename(columns = {'Time period':'country'}, inplace = True)
    df.rename(columns = {'Unnamed: 2':'sex'}, inplace = True)
    df.rename(columns = {'Unnamed: 1':'type'}, inplace = True)    
    #df = df[(df > 0).all(1)]
    return df

def extract_dataset(country, df,  sex='A'):
    
    """
    This function is used to extract the subset of interest from the main dataset.
    
    This will be the second and compulsory function to execute when using the package.
    
    This function can extract part of the dataset that the user wants to analyse by 
    providing the name of the country of interest, the type of the dataset (infants or 
    childrean aged 1 to 4 year) and the sex (Female or Male). 
    
    Firstly, it checkes whether the provided country exists in the 'country' column of 
    the dataset by using 'isin()' method.

    Parameters:

    The country parameter accepts a list with country names e.g. cntry=['Poland','India']
    
    All country names should be written with first capital letter. 
    
    Maximum two countries can be given in the list.

    The df parameter accepts a pandas data frame which is loaded from invoking load_dataset(n) function.

    Sex - This parameter accepts a single character- 'F','M','A' 
    F- Female (extract only Female data)
    M- Male (extract only Male data)
    A- All( this is default option)

    Function will return the subset of main dataset i.e. having data for the selected country and sex.
    """
    
    df = df[df.country.isin(country)]
    
            
    if sex == 'F':
        df = df[df.sex == 'Female']   
    elif sex == 'M':
        df = df[df.sex == 'Male'] 
    return df

def merge_dataset(df1, df2):
    
    """
    This function merges the two dataset
    An user might be interested in looking at dataset for both age groups 
    infant and children aged 1 to 4 years for a country of interest.  
    
    The merge_dataset() function joins two datasets, df1 and sf2, by using concat() method.
    
    By default 'axis=0' concatenate df1 and df2 vertically.  

    Parameters:

    df1 - This parameter accepts a pandas data frame. The first dataframe of interest can be passed

    df2 - This parameter accepts a pandas data frame. The first dataframe of interest can be passed

    Function will return the concatenated dataset.
    """
    
    df=pd.concat([df1,df2])
    return df
    
def wide_to_long(df1):
    
    """
    This function displays the data in long format.
    
    Firstly, this function makes a copy of provided dataset, 'df1', by using copy() method
    and assigns the copied dataset to a variable called 'dfx'.
    
    Secondly, the columns in the copied dataset are being renamed by using 'rename()' method 
    in such way that all the years from 2009 to 2019 have new names which contain also 
    'Mor_rate-' in front of each year.
    
    Finally, the dataset is converted  from a 'wide' format to a 'long' format
    by using a 'wide_to_long()' method provided by 'pandas' where 'Mor_rate' variable 
    starts the 'long' format,'country' and 'sex' are the columns used as id variables 
    and 'year' is a sub-observation variable.
    
    The 'long' format is assigned to a variable called 'long_df'.

    Parameters:

    The df parameter accepts a pandas data frame which is received from invoking 
    extract_dataset(country, df, sex).
    """
    
    dfx=df1.copy()   
    dfx.rename(columns = {'2009':'Mor_rate-2009'}, inplace = True)
    dfx.rename(columns = {'2010':'Mor_rate-2010'}, inplace = True)
    dfx.rename(columns = {'2011':'Mor_rate-2011'}, inplace = True)
    dfx.rename(columns = {'2012':'Mor_rate-2012'}, inplace = True)
    dfx.rename(columns = {'2013':'Mor_rate-2013'}, inplace = True)
    dfx.rename(columns = {'2014':'Mor_rate-2014'}, inplace = True)
    dfx.rename(columns = {'2015':'Mor_rate-2015'}, inplace = True)
    dfx.rename(columns = {'2016':'Mor_rate-2016'}, inplace = True)
    dfx.rename(columns = {'2017':'Mor_rate-2017'}, inplace = True)
    dfx.rename(columns = {'2018':'Mor_rate-2018'}, inplace = True)
    dfx.rename(columns = {'2019':'Mor_rate-2019'}, inplace = True)

    long_df = ( 
                pd.wide_to_long(dfx, stubnames='Mor_rate', 
                                i=['country','sex'], j='year',sep='-')
                
                )
    return long_df

def summary(df):
    
    """
    This function returns summarised information of the subset of interest from the main dataset.

    Parameters:

    The df parameter accepts a pandas data frame which is received from invoking 
    extract_dataset(country, df, sex).

    Function will return the summary of dataset i.e min/max/mean for each sex for the given country.
    """
    
    count = 0
    country_list = []
    type_list = []
    sex_list = []
    summarized_output=''
    #summarized_output='The dataframe illustriates the summary for country '
    warnings.filterwarnings("ignore")
    for i in df.country:        
        if i in country_list:
            pass
        else:
            country_list.append(i)
            
    
    #summarized_output=summarized_output+'\nFor'
    
    for i in df.type:        
        if i in type_list:
            pass
        else:
            type_list.append(i)
            
    for i in df.sex:        
        if i in sex_list:
            pass
        else:
            sex_list.append(i)
            
    for i in country_list:
        summarized_output=summarized_output+'\nSummary for '+ str(i)
        
        for j in type_list:
            summarized_output = summarized_output+'\nDetails for '+ str(j)
            row1 = df[df.country == i]
            row1=row1[row1.type == j]
            if 'Female' in sex_list:
                row1F = row1[row1.sex == 'Female']
                
                female_mean = row1F.mean(axis = 1)
                female_max  = row1F.max(axis = 1)
                female_min  = row1F.min(axis = 1)
                
                summarized_output = summarized_output+'\nFemale:'
                summarized_output = summarized_output+'\nmean = '+ str(female_mean.iat[0])
                summarized_output = summarized_output+'\nmax = '+ str(female_max.iat[0])
                summarized_output = summarized_output+'\nmin = '+ str(female_max.iat[0])
            
            if 'Male' in sex_list:
                row1M = row1[row1.sex == 'Male']
                
                male_mean = row1M.mean(axis = 1,numeric_only = True)
                male_max  = row1M.max(axis = 1)
                male_min  = row1M.min(axis = 1)
                
                summarized_output = summarized_output+'\nMale:'
                summarized_output = summarized_output+'\nmean = '+str(male_mean.iat[0])
                summarized_output = summarized_output+'\nmax = '+ str(male_max.iat[0])
                summarized_output = summarized_output+'\nmin = '+ str(male_min.iat[0])
            
            if 'Total' in sex_list:
                row1T = row1[row1.sex == 'Total']
                
                summarized_output = summarized_output+'\nTotal:'
                Total_mean = row1T.mean(axis = 1,numeric_only = True)
                Total_max  = row1T.max(axis = 1)
                Total_min  = row1T.min(axis = 1)
                
                summarized_output = summarized_output+'\nmean = '+str(Total_mean.iat[0])
                summarized_output = summarized_output+'\nmax = '+ str(Total_max.iat[0])
                summarized_output = summarized_output+'\nmin = '+ str(Total_min.iat[0])

    return summarized_output