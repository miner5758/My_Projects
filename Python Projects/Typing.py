import pandas as pd
import matplotlib.pyplot as plt

# example put into use: plot_data(r"Daily Typing Tests.csv",'bar','Date','WPM','Typing Test average','A')
def plot_data(data,Type,Xlabel,Ylabel,Title,AMR): #AMR means average, median, Max
    data = pd.read_csv(data,parse_dates=True)
    if AMR == ('A') and Type == ('bar'):
        io = data.mean(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.bar(ax=axs)
    elif AMR == ('A') and Type == ('line'):
        io = data.mean(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot(ax=axs)
    elif AMR == ('A') and Type == ('barh'):
        io = data.mean(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.barh(ax=axs)
    elif AMR == ('A') and Type == ('box'):
        io = data.mean(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.box()
    elif AMR == ('M') and Type == ('bar'):
        io = data.median(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.bar(ax=axs)
    elif AMR == ('M') and Type == ('line'):
        io = data.median(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot(ax=axs)
    elif AMR == ('M') and Type == ('barh'):
        io = data.median(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.barh(ax=axs)
    elif AMR == ('M') and Type == ('box'):
        io = data.median(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.box(ax=axs)
        io.plot.box(ax=axs)
    elif AMR == ('MA') and Type == ('bar'):
        io = data.max(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.bar(ax=axs)
    elif AMR == ('MA') and Type == ('line'):
        io = data.max(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot(ax=axs)
    elif AMR == ('MA') and Type == ('barh'):
        io = data.max(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.barh(ax=axs)
    elif AMR == ('MA') and Type == ('box'):
        io = data.max(axis=0)
        io = pd.DataFrame(io)
        io.columns = ['Average']
        fig,axs = plt.subplots(figsize=(14,6))
        plt.xlabel(Xlabel, fontsize=14)
        plt.ylabel(Ylabel, fontsize=14)
        plt.title(Title)
        io.plot.box(ax=axs)
