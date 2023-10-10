"""

Code Name: Create_Task.py

Citations:
    Code:
        .) Code inside the function called "bmi" was found from https://www.sololearn.com/Discuss/2686226/bmi-calculator-python-beginner-project, I modified and added onto it for my use
        .) Some of the code inside the functions called "getsa" and "construct_pdf" was found from https://stackoverflow.com/ and was modified and added for use in my code
        .) The list that is created on line 41 called "states" was gotten from https://python-forum.io/thread-3105.html
            .) I added two values to the list, they were "Washington DC" and "Puerto Rico"
    Datasets:
        .) I have all of the datasets that i use in the "getdat" function and i call them throughout the program
            .) Kaggle:
                .) The data that was loaded on lines 61 and 254 were downloaded from https://www.kaggle.com/datasets
            .) The data that was loaded on line 173 is from https://meric.mo.gov/
            .) The data that was loaded on line 217 is from http://www.higheredinfo.org/
    Images:
        .) Some images that are used in this program(loaded on line 110 and used on line 487) are taken from https://www.united-states-flag.com/state.html
        .) Some images that are used in this program are generated/loaded by using https://logo.clearbit.com/, to use this API you attach a website to the end of the API (ex. https://logo.clearbit.com/https://www.google.com/) and it then returns an image that I download using the Pillow library, I get the websites from the datasets that I used.
            .) https://logo.clearbit.com is used on lines 547 and 593
"""

import math
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.styles import (getSampleStyleSheet,ParagraphStyle)
from reportlab.platypus import Paragraph, PageBreak
import PIL
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from multiprocessing.pool import ThreadPool

pool = ThreadPool(processes=1)
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming","Washington DC","Puerto Rico"]

def getdat(Type):
    if Type == "Companies":
        data = pd.read_csv("companies_sorted.csv",engine="pyarrow")
    elif Type == "Living":
        data = pd.read_html('https://meric.mo.gov/data/cost-living-data-series')
    elif Type == "Diploma":
        data = pd.read_html('http://www.higheredinfo.org/dbrowser/?level=nation&mode=data&state=0&submeasure=368')
    elif Type == "Top":
        data = pd.read_csv("top_colleges_2022.csv")
    return data

salar = pool.apply_async(getdat, args = ("Companies",))

def sear():
    global salar
    salar = salar.get()
    cato = salar['name'].tolist()
    found = False

    while not found:
        sear = input("Please insert the name of a company you want to work at: ")
        resu = []
        resudic = {}
        for i in cato:
            if sear.lower() in i.lower():
                resu.append(i)
        count = 1
        for i in resu:
            resudic[str(count)] = i
            count+=1
        val = False
        amount = 10
        old = 0
        while not val:
            if amount >= len(resudic.keys()):
                s = amount - len(resudic.keys())
                amount = amount - s
            if amount <= 10:
                for i in range(1,amount+1):
                    print("{0}.) {1}".format(i,resudic[str(i)]))
            else:
                for i in range(old,amount+1):
                    print("{0}.) {1}".format(str(i),resudic[str(i)]))
            user = input("Out of all these results, please enter the corresponding number of the company you want to work at, if the one your looking is not here please type: retry, if you want to see the next page type: next ").lower()
            if user == "retry":
                val = True
            elif user == "next":
                if amount == len(resudic.keys()):
                    print("This is the last page!\n")
                else:
                    for i in range(3):
                        print("\n")
                    old = amount
                    amount +=10
            elif user not in resudic.keys():
                print("that is not a valid answer")
            else:
                return (resudic[user])
def statee(stat):
    imthi = []
    page = urllib.request.urlopen('https://www.united-states-flag.com/state.html')
    soup = BeautifulSoup(page,features="lxml")
    images = soup.findAll('img',alt=True)
    for image in images:
        lol = ''
        if "State" in image['alt']:
            lol = (image['alt'].rsplit(' ',2)[0]) 
        else:
            lol = (image['alt'].rsplit(' ',1)[0])
        if lol in states:
            imthi.append(image)
    for i in imthi:
        if stat in i['alt']:
            return i['src']

def bmi():
    height = input("What is your height in feet?(Ex. 5'9): ")
    weight = int(input("What is your weight in pounds?(Ex. 220): "))
    height = height.split("'")
    inches = (int(height[0]) * 12) + int(height[1])
    meter = inches / 39.37  
    meter = inches  * 0.0254
    

    kilo = int(weight) * 0.453592

    bmi= kilo/(meter)**2

    if bmi<18.5:
        return("Underweight")
    elif bmi>=18.5 and bmi<25:
        return("Normal")
    elif bmi>=25 and bmi<30:
        return("Overweight")
    else:
        return("Obese")


def piechart_on_food():
    nut = ["protein","fruits and vegetables","dairy","carbs","foods high in sugar or fat"]
    things = []
    notdone = True
    while notdone:
        for i in nut:
            print("How much percentage is left: {0}".format(100 - sum(things)))
            inl = int(input("Think about this carfully, how much {0} do you eat a day?(In percentage): ".format(i)))
            things.append(inl)
        if(sum(things) > 100):
            print("Thats more than 100%!")
            things = []
        elif(sum(things) < 100):
            print("Thats less than 100%!")
            things = []
        else:
            notdone = False
    newnuts = []
    for i in range(len(nut)):
        newnuts.append(nut[i] + "\n({0}%)".format(things[i]))
    
    y = np.array(things)
    return[y,newnuts,things,nut]

def col():
    table_MN = getdat("Living")
    df = table_MN[0]
    constu = []

    for i, d in enumerate(df):
        gh = list(d)
        tit = gh.pop(0)
        r = pd.DataFrame(list(gh),columns=[tit])
        constu.append(r)

    data = pd.concat(constu,axis=1,join='inner')

    after = ''
    loop = True
    while loop == True:
        after = input("After you graduate, do you plan to go straight into the workforce or do you intend to go to university? ").lower()
        if after == "workforce" or after == "university":
            loop = False
        else:
            print("answer can be either workforce or university!")
    
    if after == 'workforce':
        live = ""
        loop = True
        while loop == True:
            live = input("What state do you live in/intend to live in? ")
            if " " in live:
                live = live.lower().split()
                emp = ''
                for i in live:
                    if i == live[0]:
                        emp = emp + i.capitalize() + ' '
                    elif i == live[-1]:
                        emp = emp + i.capitalize()
                    else:
                        emp = emp + i + ' '
                live = emp
            else:
                live = live.capitalize()
            if live not in states:
                print("That is not a state, Please enter a valid one!")
            else:
                loop = False
        your = data[data['State'] == live]
        table_MNd = getdat("Diploma")
        data2 = table_MNd[2]
        data2.columns = data2.iloc[0]
        data2 = table_MNd[2].drop(data2.index[0])
        data2.rename(columns={'Download as: Tab-Delimited TextMS Excel':'State'}, inplace=True)
        data2 = data2[['State','Median Income Estimate, Just High School Diploma ($)','Median Income Estimate, Just Bachelors Degree ($)','Median Income Estimate, Just Masters Degree ($)']]
        also = data2[data2['State'] == live]
        if float(list(your['Index'])[0]) <= 94.9:
            return["Good",your,after,also]
        elif float(list(your['Index'])[0]) >= 95.0 and float(list(your['Index'])[0]) <= 104.9:
            return["Normal",your,after,also]
        elif float(list(your['Index'])[0]) >= 105.0 and float(list(your['Index'])[0]) <= 114.9:
            return["Bad",your,after,also]
        else:
            return["Horrible",your,after,also]
    elif after == 'university':
        live = ""
        loop = True
        while loop == True:
            live = input("What state do you live in/intend to live in? ")
            if " " in live:
                live = live.lower().split()
                emp = ''
                for i in live:
                    if i == live[0]:
                        emp = emp + i.capitalize() + ' '
                    elif i == live[-1]:
                        emp = emp + i.capitalize()
                    else:
                        emp = emp + i + ' '
                live = emp
            else:
                live = live.capitalize()
            if live not in states:
                print("That is not a state, Please enter a valid one!")
            else:
                loop = False
        collddata = getdat("Top")
        collddata = collddata[["rank",'organizationName','state.1','studentPopulation','collegeType','totalGrantAid','percentOfStudentsGrant','website']]
        collddata = collddata[collddata['state.1'] == live]

        priv = collddata[collddata['collegeType'] == 'Private not-for-profit']
        pub = collddata[collddata['collegeType'] == 'Public']

        bestover = pub.nsmallest(1,['rank'])
        bestpriv = priv.nsmallest(1,['rank'])
        cheapover = pub.nlargest(1,['totalGrantAid','percentOfStudentsGrant'])
        cheappriv = priv.nlargest(1,['totalGrantAid','percentOfStudentsGrant'])

        return ["Pla",live,after,bestover,bestpriv,cheapover,cheappriv]

def getsa(com):
    com = com.lower()
    try:
        if "&" in com:
            url = 'https://www.salary.com/research/search?keyword={0}&page=1&type=company'.format(com.replace("&","%26").lower())
        else:
            url = 'https://www.salary.com/research/search?keyword={0}&page=1&type=company'.format(com.lower())
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        soup = soup.find_all("div", {"class": "margin-bottom5 font-semibold"})
        result = ''
        for tag in soup:
            tdTags = tag.find("a", {"class": "a-color"})
            s = tdTags.text.lower()
            firstclean = re.sub("&",' and ', s )
            cleanString = re.sub(r'[^&a-zA-Z0-9- ]','', firstclean )
            finalclean = re.sub(' +', ' ', cleanString)
            
            firstclean1 = re.sub("&",' and ', com )
            cleanString1 = re.sub(r'[^&a-zA-Z0-9- ]','', firstclean1 )
            neih = re.sub(' +', ' ', cleanString1)
            if neih.lower() in finalclean.lower():
                result = tdTags
                break
        link = ("https://www.salary.com"+result['href'])
        
        reqs1 = requests.get(link)
        soup1 = BeautifulSoup(reqs1.text, 'html.parser')
        if soup1.find("a", {"class": "text-capitalize"}) is None:
            soup1 = soup1.findAll("div", {"class": "row font-semibold margin-bottom5"})
            dif = {}
            for tag in soup1:
                tdTags = tag.find("a")
                dif[tdTags.text.lower()] = tdTags['href']
                count = 1
            cho = True

            select = ''
            while cho:
                for key,values in dif.items():
                    print("{0}.) {1}".format(count,key))
                    count+=1
                user = input("Enter a title here:")
                if user.lower() not in dif.keys():
                    print("That is not a valid option!")
                    count = 1
                else:
                    select = dif[user.lower()]
                    cho = False
            link2 = "https://www.salary.com"+select
            reqs2 = requests.get(link2)
            soup2 = BeautifulSoup(reqs2.text, 'html.parser')
            soup2 = soup2.find_all("span", {"class": "font-semibold"})
            fin = ''
            for tag in soup2:
                if "$" in tag.text:
                    fin = (tag.text)
                    break
            return [user.lower(),fin+"/year"]
    
        else:
            reqs1 = requests.get(link)
            soup1 = BeautifulSoup(reqs1.text, 'html.parser')
            soup1 = soup1.find("a", {"class": "text-capitalize"})
            link2 = (soup1['href'])
        
            reqs2 = requests.get(link2)
            soup2 = BeautifulSoup(reqs2.text, 'html.parser')
            soup2 = soup2.find("div", {"class": "sa-salry"}).text
            soup2 = soup2.split()
            soup2 = [x for x in soup2 if("/year" in x)]
            return soup2[0]
    except TypeError as e:
        return "Cant be found"

def construct_pdf():
    name = input("What is your name? ") 
    work = ''
    loop = True
    while loop == True:
        work = input("Do you work out a lot? ").lower()
        if work == "yes" or work == "no":
            loop = False
        else:
            print("answer can be either yes or no!")
    flowables = []
    sample_style_sheet = getSampleStyleSheet()
    sample_style_sheet.list()
    my_doc = SimpleDocTemplate("{0}'s Ultimate Life Report.pdf".format(name.capitalize()))
    
    paragraph_1 = Paragraph("{0}'s Ultimate Life Report\n".format(name.capitalize()), ParagraphStyle('Title',
                           fontName="Helvetica-Bold",
                           fontSize=35,
                           leading = 25 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=24))
    flowables.append(paragraph_1)

    paragraph_2 = Paragraph("Made by Paul Incorporated", ParagraphStyle('Title',
                           fontSize=15,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=38))
    flowables.append(paragraph_2)

    pie = piechart_on_food()
    result = bmi()

    paragraph_3 = Paragraph("You are {0}".format(result), ParagraphStyle('Title',
                           fontName="Helvetica-Bold",
                           fontSize=30,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=20))
    flowables.append(paragraph_3)

    balance = [14,24,21,19,22]
    if result == 'Underweight':
        text = "Being underweight can be a serious health issue, if you're underweight, likely, you're not eating a healthy, balanced diet, which can lead to you lacking nutrients that your body needs to work properly. Calcium, for example, is important for the maintenance of strong and healthy bones. If you do not get enough calcium, you risk developing osteoporosis (fragile bone disease). If you do not get enough iron, you may develop anemia, which can make you feel drained. Some of these might be the reason for you being underweight: "
        if pie[2] != balance:
            text+="as you can see in the pie chart below, your nutritional intake is not at the recommended level The recommended nutritional intake required to be healthy is 14% protein, 24%" + " fruits and vegetables, 21%" + " dairy, 19%" + " carbs, and 22%" + " of foods high in sugar or fat. You should work on getting your food pie chart to meet these standards. "
        if work == "no":
            text+= "The fact that you don't work out a lot is probably also to blame, Regular physical activity is one of the most important things you can do for your health. Being physically active can improve your brain health, help manage weight, reduce the risk of disease, strengthen bones and muscles, and improve your ability to do everyday activities. keeping yourself active will do wonders for your overall being and is a habit you should slowly begin to pick up! "
        elif work == "yes" and pie[2] == balance:
            text+= "Both your pie chart and your answer to the working out question contradict your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        else:
            text+= "Your answer to the working out question contradicts your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        paragraph_4 = Paragraph(text, ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
        flowables.append(paragraph_4)

    elif result == 'Normal':
        text = "Good job! This means that you have taken great care of yourself, A healthy weight is a number that is associated with a low risk of weight-related diseases and health issues and this will lead you to live a long and comfortable life! here are some of the things that might be responsible for your success!: "
        per = 0
        for i in range(len(pie[2])):
            if math.isclose(pie[2][i],balance[i],abs_tol=4):
                per+=1
        
        if pie[2] == balance or per >= 3:
            text+= "As you can see in the pie chart below, your pie chart is perfect! This is likely a big contributor to your good condition and should be a habit you never break. "
        if work == "Yes":
            text+= "The fact that you work out a lot is probably also playing a huge role, Regular physical activity is one of the most important things you can do for your health. Being physically active can improve your brain health, help manage weight, reduce the risk of disease, strengthen bones and muscles, and improve your ability to do everyday activities, make sure to keep this up for as long as you can. "
        elif work == "no" and pie[2] == balance or per >= 3:
            text+= "Your answer to the working out question contradicts your good health, every person is different so this may be because of your metabolism. If your metabolism is high, you will burn more calories at rest and during activity, this may be the reason behind your good health."
        else:
            text+= "Both your pie chart and your answer to the working out question contradict your good health, every person is different so this may be because of your metabolism. If your metabolism is high, you will burn more calories at rest and during activity, this may be the reason behind your good health."
        paragraph_4 = Paragraph(text, ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
        flowables.append(paragraph_4)
    elif result == 'Overweight':
        text = "It's ok, being overweight is not a horrible thing that you must divert all your attention to but its something that you should strive to improve, when you are overweight you may have to struggle with things like being more susceptible to diseases as well as fatigue, some things you can do to improve this are: "
        if pie[2] != balance:
            text+="as you can see in the pie chart below, your nutritional intake is not at the recommended level The recommended nutritional intake required to be healthy is 14% protein, 24%" + " fruits and vegetables, 21%" + " dairy, 19%" + " carbs, and 22%" + " of foods high in sugar or fat. You should work on getting your food pie chart to meet these standards. "
        if work == "no":
            text+= "The fact that you don't work out a lot is probably also to blame, Regular physical activity is one of the most important things you can do for your health. Being physically active can improve your brain health, help manage weight, reduce the risk of disease, strengthen bones and muscles, and improve your ability to do everyday activities. keeping yourself active will do wonders for your overall being and is a habit you should slowly begin to pick up! "
        elif work == "yes" and pie[2] == balance:
            text+= "Both your pie chart and your answer to the working out question contradict your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        else:
            text+= "Your answer to the working out question contradicts your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        paragraph_4 = Paragraph(text, ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
        flowables.append(paragraph_4)
    elif result == 'Obese':
        text = "Being obese is a serious issue for you and your future, obesity increases the risk of several debilitating, and deadly diseases, including diabetes, heart disease, and some cancers. It does this through a variety of pathways, some as straightforward as the mechanical stress of carrying extra pounds and some involving complex changes in hormones and metabolism. Obesity decreases the quality and length of life and increases individual, national, and global healthcare costs. Here are some things you can do to fix this issue: "
        if pie[2] != balance:
            text+="as you can see in the pie chart below, your nutritional intake is not at the recommended level The recommended nutritional intake required to be healthy is 14% protein, 24%" + " fruits and vegetables, 21%" + " dairy, 19%" + " carbs, and 22%" + " of foods high in sugar or fat. You should work on getting your food pie chart to meet these standards. "
        if work == "no":
            text+= "The fact that you don't work out a lot is probably also to blame, Regular physical activity is one of the most important things you can do for your health. Being physically active can improve your brain health, help manage weight, reduce the risk of disease, strengthen bones and muscles, and improve your ability to do everyday activities. keeping yourself active will do wonders for your overall being and is a habit you should slowly begin to pick up! "
        elif work == "yes" and pie[2] == balance:
            text+= "Both your pie chart and your answer to the working out question contradict your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        else:
            text+= "Your answer to the working out question contradicts your health, every person is different so this may be because of your metabolism. If your metabolism is slow, you will burn fewer calories at rest and during activity, this may be why the reason behind your health."
        paragraph_4 = Paragraph(text, ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
        flowables.append(paragraph_4)
    
    plt.pie(pie[0],labels=pie[1],shadow=True)
    plt.savefig('chart.png')
    flowables.append(Image("chart.png"))
    flowables.append(PageBreak())

    paragraph_5 = Paragraph("Now time for your actual life! ", ParagraphStyle('Title',
                           fontName="Helvetica-Bold",
                           fontSize=35,
                           leading = 25 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=24))
    flowables.append(paragraph_5)

    decisions = col()

    if decisions[2] == 'workforce':
        paragraph_6 = Paragraph("Going into the workforce is a very risky path to choose but can bear many advantages to the university root as it can help you avoid crippling debt and gives you overall more control and power over your life, but you have to plan out this route carefully if you hope to succeed.", ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
        flowables.append(paragraph_6)

        img = statee(list(decisions[1]['State'])[0])
        try:
            response2 = requests.get(img)
            PIL.Image.open(BytesIO(response2.content)).convert('RGB').save("geekss.jpg")
            flowables.append(Image("geekss.jpg"))
        except PIL.UnidentifiedImageError:
            response2 = requests.get("https://cdn.iconscout.com/icon/premium/png-256-thumb/image-missing-1178918.png")
            PIL.Image.open(BytesIO(response2.content)).convert('RGB').save("geekss.jpg")
            flowables.append(Image("geekss.jpg"))
        sal = list(decisions[3]['Median Income Estimate, Just High School Diploma ($)'])[0]
        if len(sal) == 5:
            sal = "$" + sal[:2] + ',' + sal[2:]
        elif len(sal) == 6:
            sal = "$" + sal[:3] + ',' + sal[3:]
        if decisions[0] == "Good" or decisions[0] == "Normal":
            paragraph_7 = Paragraph("Cost of living is the amount of money needed to sustain a certain standard of living by affording expenses such as housing, food, taxes, and healthcare. Thankfully, {0} is considered to have a {1} cost of living, this means that it is very affordable to live in the state and that you won't have to aim for such a high income to be able to live comfortably in this state. this states average income for those without a high school diploma is {2}.".format(list(decisions[1]['State'])[0],decisions[0],sal), ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
            flowables.append(paragraph_7)
        elif  decisions[0] == "Bad" or decisions[0] == "Horrible":
            sal2 = list(decisions[3]['Median Income Estimate, Just Bachelors Degree ($)'])[0]
            if len(sal2) == 5:
                sal2 = "$" + sal2[:2] + ',' + sal2[2:]
            elif len(sal2) == 6:
                sal2 = "$" + sal2[:3] + ',' + sal2[3:]
            paragraph_7 = Paragraph("Cost of living is the amount of money needed to sustain a certain standard of living by affording expenses such as housing, food, taxes, and healthcare. Unfortunately, {0} is considered to have a {1} cost of living, this means that it is very unaffordable to live in the state and that you may struggle to live in this state if you don't get a college education because the salaries of people who go to uni are on average high than those who don't, this states average income for those without a high school diploma is {2} while for people with a bachelors degree, it is {3}, you may consider going to a different state or at least keeping this in mind as you go forward.".format(list(decisions[1]['State'])[0],decisions[0],sal,sal2), ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
            flowables.append(paragraph_7)
    elif decisions[2] == 'university':
        
        paragraph_7 = Paragraph("Going into university after high school is always a great choice, if you chose the right major and make the right decisions you can be ensured a salary that is almost double the one of those who don't go to uni and a generally stable job. Planning out the university you want to go can be difficult but here are all the different types for you in the state you typed in: ", ParagraphStyle('Title',
                        fontSize=13,
                        leading = 20 * 1.2,
                        parent=sample_style_sheet['BodyText'],
                        alignment=1,
                        spaceAfter=10))
        flowables.append(paragraph_7)
        namew = 0
        li = ["The best public school in","The best private school in","The cheapest public school in","The cheapest private school in"]
        for i in decisions:
            if isinstance(i, pd.DataFrame) == False:
                pass
            elif i.empty:
                pass
            else:
                paragraph_thi = Paragraph("{0} {1} is...".format(li.pop(0),decisions[1]), ParagraphStyle('Title',
                        fontSize=25,
                        leading = 20 * 1.2,
                        parent=sample_style_sheet['BodyText'],
                        alignment=1,
                        spaceAfter=40))
                flowables.append(paragraph_thi)
                try:
                    response2 = requests.get("https://logo.clearbit.com/{0}".format(list(i['website'])[0]))
                    PIL.Image.open(BytesIO(response2.content)).convert('RGB').save("geekss{0}.jpg".format(namew))
                    flowables.append(Image("geekss{0}.jpg".format(namew)))
                except PIL.UnidentifiedImageError:
                    response2 = requests.get("https://cdn.iconscout.com/icon/premium/png-256-thumb/image-missing-1178918.png")
                    PIL.Image.open(BytesIO(response2.content)).convert('RGB').save("geekss{0}.jpg".format(namew))
                    flowables.append(Image("geekss{0}.jpg".format(namew)))
                paragraph_thi2 = Paragraph(list(i['organizationName'])[0], ParagraphStyle('Title',
                        fontName="Helvetica-Bold",
                        spaceBefore = 22,
                        fontSize=35,
                        leading = 25 * 1.2,
                        parent=sample_style_sheet['BodyText'],
                        alignment=1,
                        spaceAfter=10))
                flowables.append(paragraph_thi2)
                paragraph_thi3 = Paragraph("Ranked {0} out of 498 in the US".format(list(i['rank'])[0]), ParagraphStyle('Title',
                        fontName="Helvetica-Bold",
                        fontSize=15,
                        leading = 25 * 1.2,
                        parent=sample_style_sheet['BodyText'],
                        alignment=1,
                        spaceAfter=4))
                flowables.append(paragraph_thi3)
                paragraph_thi4 = Paragraph("Website: {0}".format(list(i['website'])[0]), ParagraphStyle('Title',
                        fontName="Helvetica-Bold",
                        fontSize=10,
                        leading = 25 * 1.2,
                        parent=sample_style_sheet['BodyText'],
                        alignment=1,
                        spaceAfter=45))
                flowables.append(paragraph_thi4)
                namew+=1
    flowables.append(PageBreak())
    paragraph_5 = Paragraph("Now Lastly, its time to find info on the company you want to work at", ParagraphStyle('Title',
                           fontName="Helvetica-Bold",
                           fontSize=35,
                           leading = 25 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=24))
    flowables.append(paragraph_5)
    coms = sear()
    time = getsa(coms)
    uniqdat = salar[salar['name'] == coms]
    try:
        response = requests.get("https://logo.clearbit.com/{0}".format(list(uniqdat['domain'])[0]))
        PIL.Image.open(BytesIO(response.content)).convert('RGB').save("help.jpg")
        flowables.append(Image("help.jpg"))
    except PIL.UnidentifiedImageError:
        response1 = requests.get("https://cdn.iconscout.com/icon/premium/png-256-thumb/image-missing-1178918.png")
        PIL.Image.open(BytesIO(response1.content)).convert('RGB').save("help.jpg")
        flowables.append(Image("help.jpg"))
    paragraph_new1 = Paragraph(list(uniqdat['name'])[0].capitalize(), ParagraphStyle('Title',
                           fontName="Helvetica-Bold",
                           spaceBefore = 22,
                           fontSize=35,
                           leading = 25 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=30))
    flowables.append(paragraph_new1)
    ghtext = ''
    ghtext += "{0} is a {1} company,".format(list(uniqdat['name'])[0].capitalize(),list(uniqdat['industry'])[0])
    if math.isnan(list(uniqdat['year founded'])[0]) == False:
        ghtext += " {0} as a company was founded in {1}.".format(list(uniqdat['name'])[0].capitalize(),int(list(uniqdat['year founded'])[0]))
    if str(list(uniqdat['locality'])[0]) != 'nan' and str(list(uniqdat['country'])[0]) != 'nan':
        ghtext += " It's headquaters is located in {0}.".format(list(uniqdat['locality'])[0])
    
    if time != "Cant be found":
        if type(time) == list:
            ghtext+= " Its total employee number is estimated to be around {0} people and the average salary for a {1} is {2}.".format(list(uniqdat['total employee estimate'])[0],time[0],time[1])
        else:
            ghtext+= " Its total employee number is estimated to be around {0} people and the average salary for a {1} employee is {2}.".format(list(uniqdat['total employee estimate'])[0],list(uniqdat['name'])[0].capitalize(),time)
    else:
        ghtext = " Its total employee number is estimated to be around {0} people and unfortunately, we weren't able to find any salary information on {0}.".format(list(uniqdat['name'])[0].capitalize())
    ghtext += " If you want more information on this organization go here: {0}".format(list(uniqdat['domain'])[0])
    paragraph_new2 = Paragraph(ghtext, ParagraphStyle('Title',
                           fontSize=13,
                           leading = 20 * 1.2,
                           parent=sample_style_sheet['BodyText'],
                           alignment=1,
                           spaceAfter=10))
    flowables.append(paragraph_new2)
        
    my_doc.build(flowables)
    os.remove("chart.png")
    os.remove("help.jpg")
    try:
        os.remove("geekss.jpg")
    except:
        pass

    try:
        for i in range(namew):
            os.remove("geekss{0}.jpg".format(i))
    except:
        pass
    os.startfile("{0}'s Ultimate Life Report.pdf".format(name.capitalize()))

construct_pdf()