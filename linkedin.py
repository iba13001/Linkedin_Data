# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:37:41 2019

@author: Ibrahim
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# GET DATA BEFORE from csv
#raw_data=pd.read_csv("temp_datalab_records_linkedin_company.csv")
# Sort data by date
sorted_data=raw_data.sort_values(by ='as_of_date' )
# View data for only United Technologies
UTC_group=sorted_data.loc[(sorted_data['company_name']=='United Technologies')]

fig1=plt.plot(UTC_group['as_of_date'],UTC_group['employees_on_platform'],label='Employees')
fig1=plt.plot(UTC_group['as_of_date'],UTC_group['followers_count'],label='Linkedin Followers')
plt.xlabel('Date')
plt.ylabel('Counts')
plt.xticks(np.arange(0, 1015, step=100),rotation=45)
plt.savefig('fig1.png')
plt.legend()
plt.show()
