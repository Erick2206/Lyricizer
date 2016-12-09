from bing import bing_api
from get_url import *
from get_url import az_url
##import bs4 as BeautifulSoup
from BeautifulSoup import *
import urllib
import pprint

# Stores name of the track
search_track=raw_input("Enter name of song: ")

# Stores name of the artist
search_artist=raw_input("Enter name of artist: ")

search = search_artist + " " +  search_track + " azlyrics"

url=az_url(search)

if url!="Sorry, No Data Found :-(":
    html=urllib.urlopen(url).read()
    lyrics = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = lyrics.findAll('div')[10].findAll('div')

    lyric=tags[11]
    a=list(lyric)
    for line in a:
        if str(line)=='<br />' or str(line)=='<i>' or str(line)=='</i>':
            continue
        print line

else:
    print "Sorry No Data Found! :("
