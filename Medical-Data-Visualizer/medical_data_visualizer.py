import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# First converting height to meters and add BMI column
df['height'] = df['height']/100
df['BMI'] = np.round(df['weight']/(df['height']**2),1)


# Add 'overweight' column
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df.drop('BMI',axis=1,inplace=True)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x<=1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x<=1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio','variable','value'])['value'].count())
    df_cat.rename(columns={'value':'total'},inplace=True)
    df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(x='variable', y='total', hue='value',data=df_cat,kind='bar',col='cardio')

    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])]
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025))]
    df_heat = df_heat[(df_heat['height'] <= df_heat['height'].quantile(0.975))]
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025))]
    df_heat = df_heat[(df_heat['weight'] <= df_heat['weight'].quantile(0.975))]
    #df_heat.reset_index(inplace=True,drop=True)
   
    # Calculate the correlation matrix
    corr = np.round(df_heat.corr(),1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype(np.bool)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,mask=mask,annot=True,cmap='summer_r')
    


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
