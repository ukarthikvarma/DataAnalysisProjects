import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    new_year = []
    for i in range(2014,2050):
      new_year.append(i)
      i = i+1
    empty_array = np.empty((36,4))
    empty_array[:] = np.NaN
    new_array = np.column_stack((new_year,empty_array))

    new_df = pd.DataFrame(data=np.concatenate((df.values,new_array)),columns=df.columns)


    # Create scatter plot
    fig , ax = plt.subplots(figsize=(17,10))
    ax.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'],label='Original Data')


    # Create first line of best fit
    x = df['Year'].values
    y = df['CSIRO Adjusted Sea Level'].values
    slope , intercept, r_value, p_value, std_err = linregress(x,y)
    ax.plot(new_df['Year'],intercept+slope*(new_df['Year']),'r',label='Best Fit Line to 2050')
    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    new_x = df_2000['Year'].values
    new_y = df_2000['CSIRO Adjusted Sea Level'].values

    new_2000df = new_df[new_df['Year'] >= 2000]

    slope , intercept, r_value, p_value, std_err = linregress(new_x,new_y)
    ax.plot(new_2000df['Year'],intercept+slope*(new_2000df['Year']),'g',label='Best Fit line from 2000')



    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()