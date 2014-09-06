import sqlite3, random

#Initializes function with two arguments
def Chooser(Update = 0, MinView = 0):
    #Establishes connection with SQLite database
    conn = sqlite3.connect("C:\SQLite\MalcolmInTheMiddle.db")
    c = conn.cursor()

    #If MinView is set to 1, only an episode number with the minimum number of view may be selected
    if MinView:
        c.execute("SELECT Number FROM Episodes WHERE Views = (SELECT MIN(Views) FROM Episodes)")
        TempOutput = c.fetchall()
        Num = random.choice(TempOutput)[0]
    #If MinView is set to 0, any episode number from 1 to 151 may be chosen
    else:
        Num = random.randint(1,151)
    #If Update set to 1, the View column of the selected episode is increased by 1
    if Update:
        c.execute("UPDATE Episodes SET Views = Views + 1 WHERE Number = %d" % Num)
    #Selects row from SQLite database with episode number equal to Num
    c.execute("SELECT * FROM Episodes WHERE Number = %d" % Num)
    Output = c.fetchone()
    #Print episode info
    print("Episode: "+str(Output[1]))
    print("Season: "+str(Output[2]))
    print("Name: "+str(Output[3]))
    print("Views: "+str(Output[4]))

    #Commits changes to database and closes connection
    conn.commit()
    conn.close()

#Calls function
Chooser(Update = 0, MinView = 0)
