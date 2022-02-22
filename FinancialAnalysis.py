# Housing Cost Analysis
## Import dependencies 

import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

## Transform data

### read MapBox Api
load_dotenv()
map_box_api = os.getenv("map_box") 

### Load data 
#### Pull data from the directory it is stored in and convert CSV to pandas 
sfo_census_data_csv = Path("./Resources/neighborhoods_coordinates.csv") 
sfo_census_data_df = pd.read_csv(sfo_csv, index_col="year") 

## Create dataframes and plot data

### Housing units DataFrame
#### Calculate average housing units
housing_unit_average = sfo_census_data_df['housing_units'].groupby('year').mean()
housing_unit_average.to_csv('./Resources/housing_unit_average.csv') 
#### Assign a minimum and Maximum value for Y axis
min_y_axis_hu = sfo_census_data_df['housing_units'].min()
max_y_axis_hu = sfo_census_data_df['housing_units'].max()
#### Plot a bar graph for Housing Units 
bar_graph_HUPY = sfo_census_data_df.plot.bar(ylim=(min_y_axis - 1000, max_y_axis + 1000), title='Housing Unit Per Year (San Francisco)', figsize=(10,5))

### Average Price P/Sq.Foot DataFrame 
#### Calculate the average(mean) sales price 
sale_price_average = sfo_census_data_df['sale_price_sqr_foot'].groupby('year').mean 
#### Assign a minimun and maximum value for Y axis
min_y_axis_spsf = sfo_census_data_df['sale_price_average'].min()
max_y_axis_spsf = sfo_census_data_df['sale_price_average'].max()
#### Plot a line graph for Average Sale Price Per Square Foot
line_graph_ASPSF = sale_price_average.plot.line(ylim=(min_y_axis_spsf - 300, max_y_axis_spsf + 300), color='red', title='Average Sale Price Per Square Feet(San Francisco)', figsize=(10,5)) 

### Average Monthly Rent DataFrame
monthly_rent_average = sfo_census_data_df['gross_rent'].groupby('year').mean 
#### Assign a minimum and maximum value for X axis
min_y_axis_gr = sfo_census_data_df['monthly_rent_average'].min()
max_y_axis_gr = sfo_census_data_df['monthly_rent_average'].max()
#### Plot a line graph for Average Gross Rent
line_graph_GR = monthly_rent_average.plot.line(ylim=(min_y_axis_spsf - 1000, max_y_axis_spsf + 1000), color='blue', title='Average Gross Rent(San Franncisco)', figsize=(10,5)) 




