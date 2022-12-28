import sqlite3
import requests
from bs4 import BeautifulSoup
from time import sleep

# Setup
requiredNumberOfApp = int(input("Waiting for the Required Number Of App:    "))
inquirys = []


# allAboutApps = [ [], [], [], [] ] #  Links, Downloads, NameGames, NameInquiry
allAboutInquirys = []


def OutputData():
    print(allAboutInquirys)


def AddDataOfInquiryInListInquiries(inquiryData):
    pass


# def FindOutTheNumberOfElementsInAColumnInAllAboutInquirys():
#def ReturnTheNumberOfElementsInAColumnOfATwodimensionalArray(int[][] TwodimensionalArray, int column):
 #   counter = 0
  #  for a in range(0, 3):
   #     for b in range(0, len(allAboutInquirys[0]) - 1):
    #        if(allAboutInquirys[a][b] != 0):
     #           counter += 1


def AddNameApp(soup):
    quotName = soup.find_all(itemprop='name')
    name = str(quotName)
    name = name.replace('<h1 class="AHFaub" itemprop="name"><span>', "")
    name = name.replace('</span></h1>', "")
    allAboutApps[2].append(name)


def AddInstallsApp(soup):
    installs = soup.find_all('span', class_='htlgb')
    allAboutApps[1].append(installs[4].text)  # 4 is number of installs


def AddInfoApp(appLinks):
    print("Data processing from Google Play ")
    for url in appLinks:
        l_response = requests.get(url)
        soup = BeautifulSoup(l_response.text, 'lxml')
        AddInstallsApp(soup)
        AddNameApp(soup)
        AddDataOfInquiryInListInquiries(allAboutApps)
        sleep(0.1)


def AddLinksApps(allLinks):
    for i in allLinks:

        if(("https://play.google.com" + i + "&hl=ru&gl=US") not in allAboutApps[0]):
            if(i.find("/store/apps/dev") == (-1)):
                if(i.startswith("https") == False):
                    if(i.find("/store/apps/d") != (-1)):
                        allAboutApps[0].append(
                            "https://play.google.com" + i + "&hl=ru&gl=US")


def IsStatusConnectionNormal(response):
    if response.status_code == 200:
        print("Status Connection Is Normal")
        return True
    elif response.status_code == 404:
        print("Status Connection Is not Normal. Status = 404. Error: Not Found")
        return False


def addInquiry(requestedName):

    allAboutInquirys.append([[] * requiredNumberOfApp])
    linkInquiry = "https://play.google.com/store/search?q=" + \
        requestedName + "&c=apps&hl=ru&gl=US"
    response = requests.get(linkInquiry)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    if(IsStatusConnectionNormal(response)):
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        AddLinksApps(links)
        AddInfoApp(allAboutApps[0])


while True:
    l_userCommand = str(input("Waiting for the command    "))
    if "anl" in l_userCommand:
        l_userCommand = l_userCommand.replace('anl', '')
        inquirys = l_userCommand.split('/')

        # добавление строк в двумерный массив
        for i in range(requiredNumberOfApp * len(inquirys)):
            allAboutInquirys.append([])

        for i in map(str, inquirys):
            addInquiry(i)

    elif "sea" in l_userCommand:
        pass

    elif "sec" in l_userCommand:
        pass

    else:
        print("Invalid command")
    OutputData()


links = []
if response.status_code == 200:
    print('Success!')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    AddLinkApp(links)
    AddInfoApp(allAboutApps[0])
    OutputData()
elif response.status_code == 404:
    print('Not Found.')
