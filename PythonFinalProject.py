from numpy import true_divide
import numpy as np
import library
import matplotlib.pyplot as plt
import statistics as stat

dataSalary = library.loadList("salaryData.csv")
dataRPM = library.loadList("RPMData.csv")
dataMinutes = library.loadList("Minutes.csv")

positions = [0, 1, 2, 3, 4] #position on the bar graph
name = 1 #the column of player's names in the data set
salary = 2 #the column for player's salary in the data set
RPM = 7 #the column for player's RPM in the dataset
gamesPlayed = 3 #The column for player's games played in the data set
minutes = 4 #The column for player's minutes per game played in the data set
List = [] #List where the IPD and player names are appended to
names = [] #the list of player's names or team abbreviations, x-values of bar graphs
IPDlist = [] #the list of player's IPD or team average IPD, y-values of bar graphs
IPD = 0.0 #defines IPD as a float
x=0 #used for a counter in a while loop
medianList =[] #The list of IPD values used to find the median
TeamList = [] #the list where team's abbreviations and team average IPD are appended
TeamIPD = 0.0 #defines Team average IPD as a float
Counter = 0 #used to solve for averages, counts how many items have been processed
total = 0 #used similarly to counter but for the pie charts
under5 = 0 #The amount of players who have IPD values of under 5
between5and15 = 0 #The amount of players who have IPD values of between 5 and 15
between15and25 = 0 #The amount of players who have IPD values of between 15 and 25
over25 = 0 #The amount of players who have IPD over 25

dictSalary = {} #Holds the salary of all players
for n in range(0,len(dataSalary)):
    dictSalary[dataSalary[n][name]] = dataSalary[n][salary]

dictRPM = {} #Holds the RPM of all players
for n in range(0, len(dataRPM)):
    dictRPM[dataRPM[n][name]] = dataRPM[n][RPM]

dictAbbrev = {} #Holds the abbreviation of the team each player plays for
for n in range(0, len(dataRPM)):
    dictAbbrev[dataRPM[n][name]] = dataRPM[n][2]

dictGames = {} #Holds how many games each player played
for n in range(0, len(dataMinutes)):
    dictGames[dataMinutes[n][name]] = dataMinutes[n][gamesPlayed]

dictMinutes = {} #Holds how many minutes pergame each player played
for n in range(0, len(dataMinutes)):
    dictMinutes[dataMinutes[n][name]] = dataMinutes[n][minutes]

for n in range(0, len(dataSalary)): #Creates the median list
    if dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000: #Conditions to see if the player fits certain criteria and exists in certain dictionaries, this repeats multiple times throughout the code
        adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
        IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
        medianList += [IPD]
    
dictIPD = {} #Holds the IPD values of each player
for n in range (0, len(dataSalary)):
        if dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000:
            adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
            IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
            dictIPD[dataSalary[n][name]] = [IPD]

dictIPDFloat = {} #Holds the IPD values of each player as a float
for n in range (0, len(dataSalary)):
        if dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000:
            adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
            IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
            dictIPDFloat[dataSalary[n][name]] = IPD

dictTeam = {} #Holds the sum of the IPD values of all players who play for each team
for n in range (0, len(dataRPM)):
    if dataRPM[n][name] in dictMinutes and dataRPM[n][name] in dictIPD:
        if dataRPM[n][2] in dictTeam:
            dictTeam[dataRPM[n][2]] += dictIPD[dataRPM[n][name]]
        else:
            dictTeam[dataRPM[n][2]] = dictIPD[dataRPM[n][name]]

question = input("Type '1' for team IPD, Type '2' for player IPD: ")

if question == "3": #Players with the worst impact per dollar graph
    for n in range (0, len(dataSalary)):
        if dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000:
            adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
            IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
            List += [[IPD, dataSalary[n][name]]]
            List.sort()

    median = stat.median(medianList)

    for n in range(0,5):
        names += [List[n][1]]

    for n in range(0,5):
        IPDlist += [List[n][0]]

    fig = plt.figure(figsize=(10,5))

    plt.bar(positions, IPDlist, width=0.5, color="blue")
    plt.xticks(positions, names)
    plt.axhline(y=median,linewidth=1, color='red')
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.ylabel('Impact Per Dollar (IPD)')
    plt.title('Players With the Worst Impact Per Dollar')
    plt.legend(['Median'])
    plt.show()

if question == "4": #Players with the best impact per dollar graph
    for n in range (0, len(dataSalary)):
        if dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000:
            adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
            IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
            List += [[IPD, dataSalary[n][name]]]
            List.sort(reverse=True)

    median = stat.median(medianList)

    for n in range(0,5):
        names += [List[n][1]]

    for n in range(0,5):
        IPDlist += [List[n][0]]

    fig = plt.figure(figsize=(10,5))

    plt.bar(positions, IPDlist, width=0.5, color="blue")
    plt.xticks(positions, names)
    plt.axhline(y=median,linewidth=1, color='red')
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.ylabel('Impact Per Dollar (IPD)')
    plt.title('Players With the Best Impact Per Dollar')
    plt.legend(['Median'])
    plt.show()


if question == "2": #Interactive bar graph for player's IPD
    while x < 5:
        userInput = input("Enter a Player's Name: ")
        if userInput in dictRPM and userInput in dictSalary and userInput in dictMinutes and int(dictGames[userInput]) > 10 and float(dictMinutes[userInput]) > 20 and int(dictSalary[userInput]) > 900000:
            adjustRPM = float(dictRPM[userInput]) + 5
            IPD = round(((float(adjustRPM)/float(dictSalary[userInput])) * 1e7), 2)
            List += [[IPD, userInput]]
            x += 1
        else:
            print("Are you sure you spelled that right? Remember capitols!")

    List.sort()

    median = stat.median(medianList)

    for n in range(0,5):
        names += [List[n][1]]

    for n in range(0,5):
        IPDlist += [List[n][0]]

    fig = plt.figure(figsize=(10,5))

    plt.bar(positions, IPDlist, width=0.5, color="blue")
    plt.xticks(positions, names)
    plt.axhline(y=median,linewidth=1, color='red')
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.ylabel('Impact Per Dollar (IPD)')
    plt.title('Players VS. Impact Per Dollar')
    plt.legend(['Median'])
    plt.show()


if question == "1": #Interactive bar graph for team average IPD
    for n in range(0,5):
        userInput = input("Enter a team's abbreviation: ")
        for n in range(len(dataSalary)):
            if  dictAbbrev[dataSalary[n][name]] == userInput and dataSalary[n][name]in dictRPM and dataSalary[n][name] in dictSalary and dataSalary[n][name] in dictMinutes and int(dictGames[dataSalary[n][name]]) > 10 and float(dictMinutes[dataSalary[n][name]]) > 20 and int(dictSalary[dataSalary[n][name]]) > 900000:
                adjustRPM = float(dictRPM[dataSalary[n][name]]) + 5
                IPD = round(((float(adjustRPM)/float(dictSalary[dataSalary[n][name]])) * 1e7), 2)
                Counter += 1
                TeamIPD += IPD
        TeamAvg = TeamIPD/Counter
        TeamList += [[round(TeamAvg, 2), userInput]]
        TeamIPD = 0
        Counter = 0

    for n in range(0,5):
        names += [TeamList[n][1]]

    for n in range(0,5):
        IPDlist += [TeamList[n][0]]

    fig = plt.figure(figsize=(10,5))

    plt.bar(positions, IPDlist, width=0.5, color="red")
    plt.xticks(positions, names)
    plt.axhline(y=7.57,linewidth=1, color='blue')
    plt.ylabel('Team Average Impact Per Dollar (IPD)')
    plt.title("Team Abbreviation VS. Team's Average Impact Per Dollar")
    plt.legend(['Median'])
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.show()

if question == "5": #Teams with the worst average IPD graph

    TeamAbvList = ["TOR", "ATL", "BKN", "UTA", "MEM", "OKC", "ORL", "BOS", "WAS", "PHI", "CLE", "SAS", "SAC", "LAL", "LAC", "POR", "MIL", "HOU", "IND", "NYK", "CHI", "DEN", "CHA", "MIA", "DET", "GSW", "DAL", "IND", "PHX", "NOP"]
    
    for element in TeamAbvList:
        average = 0
        counter = 0
        sum = 0
        for i in dictTeam[element]:
            sum += i
            counter += 1 
            average = round(sum/counter, 2)
        TeamList += [[average, element]]
    
    TeamList.sort()

    for n in range(0,5):
        names += [TeamList[n][1]]

    for n in range(0,5):
        IPDlist += [TeamList[n][0]]

    fig = plt.figure(figsize=(10,5))
    plt.bar(positions, IPDlist, width=0.5, color="red")
    plt.xticks(positions, names)
    plt.axhline(y=7.57,linewidth=1, color='blue')
    plt.ylabel('Team Average Impact Per Dollar (IPD)')
    plt.title('Teams With the Worst Average Impact Per Dollar')
    plt.legend(['Median'])
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.show()

if question == "6": #Teams with the best average IPD graph

    TeamAbvList = ["TOR", "ATL", "BKN", "UTA", "MEM", "OKC", "ORL", "BOS", "WAS", "PHI", "CLE", "SAS", "SAC", "LAL", "LAC", "POR", "MIL", "HOU", "IND", "NYK", "CHI", "DEN", "CHA", "MIA", "DET", "GSW", "DAL", "IND", "PHX", "NOP"]
    
    TeamList = []
    for element in TeamAbvList:
        average = 0
        counter = 0
        sum = 0
        for i in dictTeam[element]:
            sum += i
            counter += 1 
            average = round(sum/counter, 2)
        TeamList += [[average, element]]
    
    TeamList.sort(reverse=True)

    for n in range(0,5):
        names += [TeamList[n][1]]

    for n in range(0,5):
        IPDlist += [TeamList[n][0]]

    fig = plt.figure(figsize=(10,5))
    plt.bar(positions, IPDlist, width=0.5, color="red")
    plt.xticks(positions, names)
    plt.axhline(y=7.57,linewidth=1, color='blue')
    plt.ylabel('Team Average Impact Per Dollar (IPD)')
    plt.title("Teams With the Best Average Impact Per Dollar")
    plt.legend(['Median'])
    for n in range(0,5):
        plt.text(n,IPDlist[n], IPDlist[n], ha="center", va="bottom")
    plt.show()

if question == "7": #Percentage spread across the entire NBA pie chart
    for n in range(0, len(dataMinutes)):
        if dictIPDFloat[dataMinutes[n][name]] <  5:
            under5 += 1
            total += 1
        elif dictIPDFloat[dataMinutes[n][name]]  >= 5 and dictIPDFloat[dataMinutes[n][name]] < 15:
            between5and15 += 1
            total += 1
        elif dictIPDFloat[dataMinutes[n][name]]  >= 15 and dictIPDFloat[dataMinutes[n][name]] < 25:
            between15and25 += 1
            total += 1
        elif dictIPDFloat[dataMinutes[n][name]]  >= 25:
            over25 += 1
            total += 1

    under5Percent = (100*under5)/total
    between5and15Percent = (100*between5and15)/total
    between15and25Percent = (100*between15and25)/total
    over25Percent = (100*over25)/total

    pieYValue = np.array([under5Percent, between5and15Percent, between15and25Percent, over25Percent])
    mylabels = ["Under 5", "Between 5 and 15", "Between 15 and 25", "Over 30"]
    colors = ['lightskyblue', 'yellowgreen', 'orange', 'lightcoral']

    plt.figure(figsize=(10,5))
    plt.legend(mylabels, loc= "center")
    plt.title("Percentage Spread of Players With the Following IPD Values Across the NBA")
    patches, texts = plt.pie(pieYValue, colors=colors)
    plt.pie(pieYValue, autopct='%.1f%%', colors = colors)
    plt.legend(patches, mylabels, loc="lower right")
    plt.show()

if question == "8": #Percentage spread across the teams with top 5 average IPD pie chart
    for n in range (0, len(dictTeam["GSW"])):
        if dictTeam["GSW"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["GSW"][n]  >= 5 and dictTeam["GSW"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["GSW"][n]  >= 15 and dictTeam["GSW"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["GSW"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["BOS"])):
        if dictTeam["BOS"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["BOS"][n]  >= 5 and dictTeam["BOS"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["BOS"][n]  >= 15 and dictTeam["BOS"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["BOS"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["POR"])):
        if dictTeam["POR"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["POR"][n]  >= 5 and dictTeam["POR"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["POR"][n]  >= 15 and dictTeam["POR"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["POR"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["CHI"])):
        if dictTeam["CHI"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["CHI"][n]  >= 5 and dictTeam["CHI"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["CHI"][n]  >= 15 and dictTeam["CHI"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["CHI"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["CLE"])):
        if dictTeam["CLE"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["CLE"][n]  >= 5 and dictTeam["CLE"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["CLE"][n]  >= 15 and dictTeam["CLE"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["CLE"][n]  >= 25:
            over25 += 1
            total += 1


    under5Percent = (100*under5)/total
    between5and15Percent = (100*between5and15)/total
    between15and25Percent = (100*between15and25)/total
    over25Percent = (100*over25)/total

    pieYValue = np.array([under5Percent, between5and15Percent, between15and25Percent, over25Percent])
    mylabels = ["Under 5", "Between 5 and 15", "Between 15 and 25", "Over 30"]
    colors = ['lightskyblue', 'yellowgreen', 'orange', 'lightcoral']

    plt.figure(figsize=(10,5))
    plt.legend(mylabels, loc= "center")
    plt.title("Percentage Spread of Players With the Following IPD Values On the Teams with the 5 Worst Average Impact Per Dollar")
    patches, texts = plt.pie(pieYValue, colors=colors)
    plt.pie(pieYValue, autopct='%.1f%%', colors = colors)
    plt.legend(patches, mylabels, loc="lower right")
    plt.show()

if question == "9": #Percentage spread across the teams with top 5 average IPD pie chart
    for n in range (0, len(dictTeam["OKC"])):
        if dictTeam["OKC"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["OKC"][n]  >= 5 and dictTeam["OKC"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["OKC"][n]  >= 15 and dictTeam["OKC"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["OKC"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["MIA"])):
        if dictTeam["MIA"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["MIA"][n]  >= 5 and dictTeam["MIA"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["MIA"][n]  >= 15 and dictTeam["MIA"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["MIA"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["CHA"])):
        if dictTeam["CHA"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["CHA"][n]  >= 5 and dictTeam["CHA"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["CHA"][n]  >= 15 and dictTeam["CHA"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["CHA"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["HOU"])):
        if dictTeam["HOU"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["HOU"][n]  >= 5 and dictTeam["HOU"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["HOU"][n]  >= 15 and dictTeam["HOU"][n] < 25:
            between5and15 += 1
            total += 1
        elif dictTeam["HOU"][n]  >= 25:
            over25 += 1
            total += 1
    for n in range (0, len(dictTeam["MEM"])):
        if dictTeam["MEM"][n] <  5:
            under5 += 1
            total += 1
        elif dictTeam["MEM"][n]  >= 5 and dictTeam["MEM"][n] < 15:
            between5and15 += 1
            total += 1
        elif dictTeam["MEM"][n]  >= 15 and dictTeam["MEM"][n] < 25:
            between15and25 += 1
            total += 1
        elif dictTeam["MEM"][n]  >= 25:
            over25 += 1
            total += 1


    under5Percent = (100*under5)/total
    between5and15Percent = (100*between5and15)/total
    between15and25Percent = (100*between15and25)/total
    over25Percent = (100*over25)/total

    pieYValue = np.array([under5Percent, between5and15Percent, between15and25Percent, over25Percent])
    mylabels = ["Under 5", "Between 5 and 15", "Between 15 and 25", "Over 30"]
    colors = ['lightskyblue', 'yellowgreen', 'orange', 'lightcoral']

    plt.figure(figsize=(11,5))
    plt.legend(mylabels, loc= "center")
    plt.title("Percentage Spread of Players With the Following IPD Values On the Teams with the 5 Best Average Impact Per Dollar")
    patches, texts = plt.pie(pieYValue, colors=colors)
    plt.pie(pieYValue, autopct='%.1f%%', colors = colors)
    plt.legend(patches, mylabels, loc="lower right")
    plt.show()
