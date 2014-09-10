MITMRandomEpisode
=================

In the absence of a Netflix "Play Random Episode" option, this is some Python code which will select at random from all 151 episodes of the Malcolm in the Middle show and print out the details. Other features are detailed below.  This version relies on a SQLite database to store episodes.  This is what the code will query from to find our random episode.

The code is in two parts:

MalcolmInTheMiddleEpisodes.py

This code serves to set up the SQLite database to be queried from in the next script.  The table is constructed from the information taken from this site: http://en.wikipedia.org/wiki/List_of_Malcolm_in_the_Middle_episodes
urllib2 and BeautifulSoup are used to read and parse the HTML and the sqlite3 package is used to interface with the SQLite database on your machine.


ChooseEpisode.py

This is the code which queries the SQLlite database and produces the chosen episode info.  The Update argument can be set to 1 which will increase the View column of the selected episode by 1.  If the MinView argument is set then the program will only choose an episode that has the minimum number of views out of the entire table.
