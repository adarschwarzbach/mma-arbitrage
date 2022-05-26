# imports - will need to add to dependencies list
import json
from bs4 import BeautifulSoup
import requests
import json

# global variables
#list of matchups
fights=[]

#odds lists
oddsShark=[]
bovada=[]
betOnline=[]
everyGameSportsbook=[]
sportsBetting=[]
betUs = []

#bs4 variables
page = requests.get("https://www.oddsshark.com/ufc/odds")
soup = BeautifulSoup(page.content, 'html.parser')

def createJSON():
    dictionary={}
    dictionary['fights']=getFights()
    dictionary['oddsShark'] = getOddsShark()
    dictionary['bovada'] = getBovada()
    dictionary['betOnline'] = getBetOnline()
    dictionary['everGameSportsbook'] = getEveryGameSportsbook()
    dictionary['sportsBetting'] = getSportsBetting()
    dictionary['betUs'] = getBetUs()
    return dictionary

def getFights():
    namesHTML = soup.find_all("span", class_= "sm-hide")
    names=[x.text for x in namesHTML]
    names=names[1:]
    finalN=[]
    for x in names:
        if(x!="Matchup"):
            isNum = False
            chars = [y for y in x]
            for character in chars:
                if(character.isdigit()):
                    isNum=True
            if(isNum==False):
                finalN.append(x)
    allMatchups=[]
    for x in range(0,len(finalN),2):
        allMatchups.append([finalN[x],finalN[x+1]])  
    rowsList=[]
    rowsHTML = soup.find_all("div", class_= "op-block__row")
    rowsList=[x.text for x in rowsHTML]
    for x in range(0,len(allMatchups)):
        if(rowsList[x]!='No available odds'):
            fights.append(allMatchups[x])
    return(fights)

def getOddsShark():
    # OddsShark away
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1815 op-spread op-away")
    oddsSharkA=[]
    for x in oddsHTML:
        if (x.text!=''):
            oddsSharkA.append(x.text)
        else:
            oddsSharkA.append('')

    # OddShark home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1815 op-spread op-home")
    oddsSharkH=[]
    for x in oddsHTML:
        if (x.text!=''):
            oddsSharkH.append(x.text)
        else:
            oddsSharkH.append('')

    for x in range(len(oddsSharkH)):
        hold=[oddsSharkA[x],oddsSharkH[x]]
        oddsShark.append(hold)
    return oddsShark

def getBovada():
    # Bovada away
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__8026 op-spread op-away")
    bovadaA=[]
    for x in oddsHTML:
        if (x.text!=''):
            bovadaA.append(x.text)
        else:
            bovadaA.append('')

    # Bovada home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__8026 op-spread op-home")
    bovadaH=[]
    for x in oddsHTML:
        if (x.text!=''):
            bovadaH.append(x.text)
        else:
            bovadaH.append('')

    for x in range(len(bovadaH)):
        hold=[bovadaA[x],bovadaH[x]]
        bovada.append(hold)
    return bovada

def getBetOnline():
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1821 op-spread op-away")
    betOnlineA=[]
    for x in oddsHTML:
        if (x.text!=''):
            betOnlineA.append(x.text)
        else:
            betOnlineA.append('')
            
    # BetOnline home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1821 op-spread op-home")
    betOnlineH=[]
    for x in oddsHTML:
        if (x.text!=''):
            betOnlineH.append(x.text)
        else:
            betOnlineH.append('')

    for x in range(len(betOnlineH)):
        hold=[betOnlineA[x],betOnlineH[x]]
        betOnline.append(hold)
    return betOnline

def getEveryGameSportsbook():
    # everyGameSportsbook away
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__2579 op-spread op-away")
    everyGameSportsbookA=[]
    for x in oddsHTML:
        if (x.text!=''):
            everyGameSportsbookA.append(x.text)
        else:
            everyGameSportsbookA.append('')

    # BetOnline home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__2579 op-spread op-home")
    everyGameSportsbookH=[]
    for x in oddsHTML:
        if (x.text!=''):
            everyGameSportsbookH.append(x.text)
        else:
            everyGameSportsbookH.append('')

    for x in range(len(everyGameSportsbookH)):
        hold=[everyGameSportsbookA[x],everyGameSportsbookH[x]]
        everyGameSportsbook.append(hold)
    return everyGameSportsbook

def getSportsBetting():
    # sportsBetting away
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1944 op-spread op-away")
    sportsBettingA=[]
    for x in oddsHTML:
        if (x.text!=''):
            sportsBettingA.append(x.text)
        else:
            sportsBettingA.append('')

    # BetOnline home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__1944 op-spread op-home")
    sportsBettingH=[]
    for x in oddsHTML:
        if (x.text!=''):
            sportsBettingH.append(x.text)
        else:
            sportsBettingH.append('')

    for x in range(len(sportsBettingH)):
        hold=[sportsBettingA[x],sportsBettingH[x]]
        sportsBetting.append(hold)
    return sportsBetting

def getBetUs():
    # betUs away
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__8371 op-spread op-away")
    betUsA=[]
    for x in oddsHTML:
        if (x.text!=''):
            betUsA.append(x.text)
        else:
            betUsA.append('')

    # BetOnline home
    oddsHTML = soup.find_all("div", class_="op-block__cell-item op-block__cell-item--spread op-block__8371 op-spread op-home")
    betUsH=[]
    for x in oddsHTML:
        if (x.text!=''):
            betUsH.append(x.text)
        else:
            betUsH.append('')

    for x in range(len(betUsH)):
        hold=[betUsA[x],betUsH[x]]
        betUs.append(hold)
    return betUs


if __name__ == "__main__":
    print(len(getFights()))
