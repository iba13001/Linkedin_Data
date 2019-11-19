# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:37:41 2019

@author: Ibrahim
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# GET DATA BEFORE from csv
#raw_data=pd.read_csv("temp_datalab_records_linkedin_company.csv")
# Sort data by date
#sorted_data=raw_data.sort_values(by ='as_of_date' )
# View data for only United Technologies
#UTC_group=sorted_data.loc[(sorted_data['company_name']=='United Technologies')]

#fig1=plt.plot(UTC_group['as_of_date'],UTC_group['employees_on_platform'],label='Employees')
#fig1=plt.plot(UTC_group['as_of_date'],UTC_group['followers_count'],label='Linkedin Followers')
#plt.xlabel('Date')
#plt.ylabel('Counts')
#plt.xticks(np.arange(0, 1015, step=100),rotation=45)
#plt.savefig('fig1.png')
#plt.legend()
#plt.show()

########################
#
# sort data by date
#sorted_data = raw_data.sort_values(by ='as_of_date' )
#set 'as_of_date'as index
#indexed_data=sorted_data.set_index('as_of_date')
# get data for 2017 only
#data2017=indexed_data.truncate(after='2017-12-31',before='2017-01-01')
# group by company name
#companies=data2017.groupby('company_name')
# show the last entries of each company and get the top 5 companies with 
# the higest number of followers by the end of 2017
#companies_start_2017=companies.first()
#companies_end_2017=companies.last()
# from visualizing the data frame the companies are:
#google, microsoft,apple,ibm and amazon 
# get the change in the number of employees and followers in 2017
#delta_followers=companies_end_2017['followers_count']-companies_start_2017['followers_count']
#delta_employee=companies_end_2017['employees_on_platform']-companies_start_2017['employees_on_platform']
# get delta followers and delta employess for the top 5 companies (follower wise)
#top_5_delta_followers=np.array([delta_followers['Google'],delta_followers['Microsoft'],
#                       delta_followers['Apple'],delta_followers['IBM'],
#                       delta_followers['Amazon']])
#top_5_delta_employee=np.array([delta_employee['Google'],delta_employee['Microsoft'],
#                       delta_employee['Apple'],delta_employee['IBM'],
#                       delta_employee['Amazon']])
#followers_employee_ratio=top_5_delta_employee/top_5_delta_followers
#top5_companies=['google', 'microsoft','apple','ibm', 'amazon']
#fig2=plt.bar(top5_companies,followers_employee_ratio)
#plt.xlabel('Top 5 Companies with Linkedin Followers')
#plt.ylabel('Employee:Followers Ratio in 2017')
#plt.show()

#######################################################
# sort data by date
#sorted_data = raw_data.sort_values(by ='as_of_date' )
#set 'as_of_date'as index
#indexed_data=sorted_data.set_index('as_of_date')


#group by (company name)
#companies=sorted_data.groupby(['company_name'])
# get the last entry for each company
comp_last=pd.DataFrame(companies.last())
# get the average number of followeres for each industry at the the last date
# the data is collected
industries_avg_fol=comp_last.groupby('industry')['followers_count'].mean()
# convert the series to dataframe
industries_avg_fol=pd.DataFrame(industries_avg_fol)
# reset the index of industries_avg_fol
industries_avg_fol=industries_avg_fol.reset_index()         
# round the number of followers to the smallest integer
industries_avg_fol=industries_avg_fol.astype({'followers_count':int})
# get the z score for the averages   
zscores=np.array(stats.zscore(industries_avg_fol['followers_count'])) 
# get the total number of followers in all industries
industries_sum_fol=pd.DataFrame(comp_last.groupby('industry')['followers_count'].sum())
# reset the index of industries_max_fol
industries_sum_fol=industries_sum_fol.reset_index()                    
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 

















