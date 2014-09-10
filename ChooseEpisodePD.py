import random
import pandas

#Initializes function with two arguments
def Chooser(Update = 0, MinView = 0):
    #Opens .csv file containing episodes
    EpTable = pandas.DataFrame.from_csv(path='C:\Users\Nicholas\My Documents\MITMEpisodes.csv')
  
    #If MinView is set to 1, only an episode number with the minimum number of view may be selected
    if MinView:
        MinRows = EpTable[EpTable['Views'] == min(EpTable['Views'])]
        print(MinRows)
        Num = random.choice(MinRows.index)
    #If MinView is set to 0, any episode number from 1 to 151 may be chosen
    else:
        Num = random.randint(1,151)
    #If Update set to 1, the Views column of the selected episode is increased by 1
    if Update:
        print(EpTable.loc[Num])
        EpTable.loc[Num,'Views'] += 1
    #Selects row from .csv file with episode number equal to Num
    Output = EpTable.loc[Num]
    #Print episode info
    print("Episode: "+str(Output[0]))
    print("Season: "+str(Output[1]))
    print("Name: "+str(Output[2]))
    print("Views: "+str(Output[3]))

    #Saves changes to .csv file
    EpTable.to_csv('C:\Users\Nicholas\My Documents\MITMEpisodes.csv',index=True,mode='w')

#Calls function
Chooser(Update = 1, MinView = 1)
