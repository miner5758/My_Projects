import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import sys
import textwrap
import math


def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)

def rates():
    df = pd.read_csv("college_rates.csv")
    print(df)

    df = df[["Race/ethnicity",'2010',"2021"]]
    df = df[df['Race/ethnicity'] != "Total"]
    df_melted = df.melt('Race/ethnicity', var_name='Year', value_name='value')
    print(df)
    


    sns.set_theme(style='whitegrid', rc={'figure.dpi': 147},              
                font_scale=0.9)
    sns.color_palette("Paired")


    fig, ax = plt.subplots(figsize=(6, 5))

    sns.barplot(x='Race/ethnicity', y='value', hue='Year', data=df_melted,)

    # Customize labels and title
    plt.xlabel("Race/ethnicity")
    plt.ylabel("College Enrollment Rate(Percent)")
    plt.title("College enrollment rates of 18- to 24-year-olds, by race/ethnicity: 2010 and 2021")

    # Rotate x-axis labels if necessary
    #plt.xticks(rotation=45 if len(df['Race/ethnicity']) > 5 else 0)
    wrap_labels(ax, 10)
    # Improve layout
    plt.tight_layout()

    plt.show()



def earnings():
    df = pd.read_csv("earnings.csv")
    df = df[['Year',"High school completion/1/","Associate's degree","Bachelor's degree"]]
    sns.set_theme(style='whitegrid', rc={'figure.dpi': 147},font_scale=0.9)
    sns.color_palette("Paired")
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df['Year'], df['High school completion/1/'], color="blue", label="High School Degree", linestyle="-")
    ax.plot(df['Year'], df["Associate's degree"], color="red", label="Associate's Degree", linestyle="-")
    ax.plot(df['Year'], df["Bachelor's degree"], color="green", label="Bachelor's Degree", linestyle="-")

    plt.xticks(df['Year'])

    plt.xlabel("Year")
    plt.ylabel("Median Annual Earnings")
    plt.title("Median annual earnings of full-time, year-round workers ages 25–34, by educational attainment: 2010 through 2021")
    plt.xlim(2010)


    ax.legend()
    # Improve layout
    plt.tight_layout()
    plt.show()
    
    
    """
    ten = df[df['Year'] == 2010]
    twent = df[df['Year'] == 2021]
    start = int(ten["Bachelor's degree"].values)
    final = int(twent["Bachelor's degree"].values)
    change_percent = ((float(final)-start)/start)*100
    print(round(change_percent,1))
    """

    """
    avghigh = df["High school completion/1/"].mean(axis=0)
    avgasso = df["Associate's degree"].mean(axis=0)
    avgbach = df["Bachelor's degree"].mean(axis=0)
    start = avghigh
    final = avgasso
    change_percent = ((float(final)-start)/start)*100
    print(round(change_percent,1))
    """

def income():
    df = pd.read_csv("incomedata.csv")
    
    df = df[["Year","White, non-Hispanic",'Black',"Hispanic (any race)","Asian","American Indian and Alaska Native"]]
    df = df[df['Year'] >= 2010]
    df_melted = df.melt('Year', var_name='Race/ethnicity', value_name='income')
    df_melted['income'] = df_melted['income'].str.replace(',', '')
    df_melted["income"] = pd.to_numeric(df_melted["income"])
    
    sns.set_theme(style='whitegrid', rc={'figure.dpi': 147},font_scale=0.9)
    sns.color_palette("Paired")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.lineplot(x='Year', y='income', hue='Race/ethnicity', data=df_melted)

    plt.xticks(df['Year'])
    plt.xlabel("Year")
    plt.ylabel("Median Household Earnings")
    plt.title("Median household income in the United States, by race and ethnicity from 2010 to 2022 (in 2022 U.S. dollars)")
    ax.set_xlim(2010, 2022)
    
    


    ax.legend()
    # Improve layout
    #plt.tight_layout()
    #plt.show()

    avgwhite = df_melted[df_melted['Race/ethnicity'] == "White, non-Hispanic"]
    avgwhite = avgwhite['income'].mean(axis=0)

    avgasian = df_melted[df_melted['Race/ethnicity'] == "Asian"]
    avgasian = avgasian['income'].mean(axis=0)

    avgblack = df_melted[df_melted['Race/ethnicity'] == "Black"]
    avgblack = avgblack['income'].mean(axis=0)

    avghisp = df_melted[df_melted['Race/ethnicity'] == "Hispanic (any race)"]
    avghisp = avghisp['income'].mean(axis=0)

    start = avghisp
    final = avgwhite
    change_percent = ((float(final)-start)/start)*100
    print(round(change_percent,1))

rates()