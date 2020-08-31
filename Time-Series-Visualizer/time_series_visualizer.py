import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
df.set_index('date',inplace=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025))]
df = df[(df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig , ax = plt.subplots(figsize=(17,10))
    
    ax = sns.lineplot(x=df.index, y=df['value'],data=df)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['month'] = df_bar['date'].dt.strftime('%b')
    df_bar['year'] = df_bar['date'].dt.year
    df_bar = df_bar.groupby(['year','month']).mean()
    df_bar.reset_index(inplace=True)
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(17,10))
    mylabels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax = sns.barplot(x='year',y='value',hue='month',hue_order=month_order,data=df_bar,edgecolor='black')
    ax.set_xlabel('Years')
    ax.set_xticklabels(labels=[2016,2017,2018,2019],rotation=90)
    ax.set_ylabel('Average Page Views')
    current_handles , current_labels = plt.gca().get_legend_handles_labels()
    ax.legend(loc='upper left',title='Months',labels=mylabels,handles=current_handles)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(17,10))

    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.subplot(1,2,1)
    sns.boxplot(x='year',y='value',data=df_box)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    plt.subplot(1,2,2)
    sns.boxplot(x='month',y='value',data=df_box,order=month_order)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)') 

   
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
