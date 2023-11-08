from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import BytesIO
import base64
from GooglePlayStoreApp.models import App
import seaborn as sns
import matplotlib.ticker as mtick
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def plot(request):
    apps = App.objects.all()
    prices = [app.Price for app in apps]
    ratings = [app.Rating for app in apps]
    #trendline
    coefficients = np.polyfit(prices, ratings, 1) #o dreapta
    p = np.poly1d(coefficients)
    #ploturile
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.scatter(prices, ratings)
    ax.set_xlabel('Price')
    ax.set_ylabel('Rating')
    ax.set_ylim([2, 5.1])
    plt.plot(prices, p(prices), "r-")

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    buffer.close()
    grafic = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'plot.html', {'grafic': grafic})

@cache_page(60 * 15)
def plot1(request):
    apps = App.objects.all()
    categories = [app.Category for app in apps]
    installs = [app.MaximumInstalls for app in apps]
    data = {'Category': categories, 'Installs': installs}
    df = pd.DataFrame(data)
    df = df.groupby(['Category']).agg({'Installs': 'max'}).reset_index()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax = sns.barplot(y='Installs', x='Category', data=df)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f'))
    ax.set_ylabel('Installations')
    ax.set_xlabel('Category', rotation=0, ha='center')
    plt.xticks(rotation=90)

    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic1 = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'plot1.html', {'grafic': grafic1})

@cache_page(60 * 15)
def plot2(request):
    #grafic 1
    apps = App.objects.all()
    categories = [app.Category for app in apps]
    prices = [app.Price for app in apps]
    data = {'Category': categories, 'Prices': prices}
    df = pd.DataFrame(data)
    df = df.groupby(['Category']).agg({'Prices': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax = sns.barplot(y='Prices', x='Category', data=df)
    ax.set_ylabel("Prices's Sum")
    ax.set_xlabel('Category')
    plt.xticks(rotation=90)
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic1 = base64.b64encode(image_png).decode('utf-8')
    #grafic2
    df2 = pd.DataFrame(data)
    df2 = df2.groupby(['Category']).agg({'Prices': 'max'}).reset_index()
    fig2, ax2=plt.subplots(figsize=(8, 5))
    ax2=sns.barplot(y='Prices', x='Category', data=df2)
    ax2.set_ylabel('Prices Max')
    ax2.set_xlabel('Category')
    plt.xticks(rotation=90)
    buffer2 = BytesIO()
    fig2.savefig(buffer2, format='png', bbox_inches='tight')
    buffer2.seek(0)
    image_png = buffer2.getvalue()
    buffer2.close()
    grafic2 = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'plot2.html', {'grafic1': grafic1, 'grafic2' : grafic2})

@cache_page(60 * 15)
def plot3(request):
    apps = App.objects.all()
    ratings = [app.Rating for app in apps]
    years = [app.Released.year for app in apps]
    data = {'Years': years, 'Ratings': ratings}
    df = pd.DataFrame(data)
    df = df.groupby(['Years']).agg({'Ratings': 'mean'}).reset_index()
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='pink')
    ax=sns.lineplot(data=df, x='Years', y="Ratings", color='green', linestyle='solid')
    ax.set_ylabel("Ratings's mean")
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'plot3.html', {'grafic':grafic})

@cache_page(60 * 15)
def plot4(request):
    apps = App.objects.filter(Released__year__in=[2019])
    categories = [app.Category for app in apps]
    data = {'Category': categories}
    df = pd.DataFrame(data)
    df = df['Category'].value_counts().reset_index(name='Count').rename(columns={'index': 'Category'})
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='pink')
    ax = sns.barplot(data=df, x='Category', y='Count', palette='rocket')
    ax.set_ylabel("Number of Apps Released in 2019")
    ax.set_xlabel("Category")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic1 = base64.b64encode(image_png).decode('utf-8')
    # grafic 2
    apps = App.objects.filter(Released__year__in=[2020])
    categories = [app.Category for app in apps]
    data = {'Category': categories}
    df = pd.DataFrame(data)
    df = df['Category'].value_counts().reset_index(name='Count').rename(columns={'index': 'Category'})
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='pink')
    ax = sns.barplot(data=df, x='Category', y='Count', palette='rocket')
    ax.set_ylabel("Number of Apps Released in 2020")
    ax.set_xlabel("Category")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic2 = base64.b64encode(image_png).decode('utf-8')
    #grafic 3
    apps = App.objects.filter(Released__year__in=[2021])
    categories = [app.Category for app in apps]
    data = {'Category': categories}
    df = pd.DataFrame(data)
    df = df['Category'].value_counts().reset_index(name='Count').rename(columns={'index': 'Category'})
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='pink')
    ax = sns.barplot(data=df, x='Category', y='Count', palette='rocket')
    ax.set_ylabel("Number of Apps Released in 2021")
    ax.set_xlabel("Category")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    grafic3 = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'plot4.html', {'grafic1': grafic1, 'grafic2': grafic2, 'grafic3': grafic3})


