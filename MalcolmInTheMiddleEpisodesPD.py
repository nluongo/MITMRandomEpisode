import urllib2
from bs4 import BeautifulSoup
import pandas

#Sets variables Episode Number (overall), Season Number, and SeasEpNumber (episode number within the season)
EpisodeNumber = 1
SeasonNumber = 1
SeasEpNumber = 1

#Creates DataFrame to hold episode info
EpTable = pandas.DataFrame(columns=['Number','Episode','Season','Name','Views'])

#Opens connection to webpage containing list of episodes
myurl = "http://en.wikipedia.org/wiki/List_of_Malcolm_in_the_Middle_episodes"
HTML = urllib2.urlopen(myurl).read()

#Reads and parses HTML using BeautifulSoup
Soup = BeautifulSoup(HTML)
PrettySoup = Soup.prettify()

#Searches HTML for episode names
for Table in Soup.body.find_all("table"):
    if (Table.get("class") == [u'wikitable', u'plainrowheaders']):
        for TR in Table.find_all("tr"):
            if (TR.get("class") == [u'vevent']):
                for TD in TR.find_all("td"):
                    if (TD.get("class") == [u'summary']):
                        #Episodes 52 and 53 had unusual setup so they are manually coded
                        if EpisodeNumber == 52:
                            NewValues = {'Number' : [52],'Episode' : [11],'Season' : [3],'Name' : 'Company Picnic: Part 1','Views' : [0]}
                            NewRow = pandas.DataFrame(NewValues,columns=['Number','Episode','Season','Name','Views'])
                            EpTable = pandas.concat([EpTable,NewRow])
                            EpisodeNumber += 1
                            continue
                        if EpisodeNumber == 53:
                            NewValues = {'Number' : [53],'Episode' : [12],'Season' : [3],'Name' : 'Company Picnic: Part 2','Views' : [0]}
                            NewRow = pandas.DataFrame(NewValues,columns=['Number','Episode','Season','Name','Views'])
                            EpTable = pandas.concat([EpTable,NewRow])
                            EpisodeNumber += 1
                        EpisodeName = TD.Text
                        if 1 <= EpisodeNumber <= 16:
                            SeasonNumber = 1
                            SeasEpNumber = EpisodeNumber
                        elif 17 <= EpisodeNumber <= 41:
                            SeasonNumber = 2
                            SeasEpNumber = EpisodeNumber - 16
                        elif 42 <= EpisodeNumber <= 63:
                            SeasonNumber = 3
                            SeasEpNumber = EpisodeNumber - 41
                        elif 64 <= EpisodeNumber <= 85:
                            SeasonNumber = 4
                            SeasEpNumber = EpisodeNumber - 63
                        elif 86 <= EpisodeNumber <= 107:
                            SeasonNumber = 5
                            SeasEpNumber = EpisodeNumber - 85
                        elif 108 <= EpisodeNumber <= 129:
                            SeasonNumber = 6
                            SeasEpNumber = EpisodeNumber - 107
                        elif 130 <= EpisodeNumber <= 151:
                            SeasonNumber = 7
                            SeasEpNumber = EpisodeNumber - 129
                        #Creates new DataFrame and adds it to EpTable as a new row
                        NewValues = {'Number' : [EpisodeNumber],
                                     'Episode' : [SeasEpNumber],
                                     'Season' : [SeasonNumber],
                                     'Name' : TD.text,
                                     'Views' : [0]}
                        NewRow = pandas.DataFrame(NewValues,columns=['Number','Episode','Season','Name','Views'])
                        EpTable = pandas.concat([EpTable,NewRow])
                        #Increments to next episode number
                        EpisodeNumber += 1
                        print(TD.text)

#Writes EpTable to .csv file
EpTable.to_csv('C:\Users\Nicholas\Documents\MITMEpisodes.csv',index=False)
