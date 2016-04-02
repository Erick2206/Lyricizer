from bing import bing_api
import pprint

<<<<<<< HEAD
=======
# Stores name of the track
#search_track=raw_input("Enter name of song: ")

# Stores name of the artist
#search_artist=raw_input("Enter name of artist: ")

# Stores the final search query
#search = search_artist + " " +  search_track + " azlyrics"

>>>>>>> af9563100d75ef3d504f7dce896ce3ad9e08edda
def az_url(search):
    '''
    A function that returns the URL of azlyrics
    '''
    result=bing_api(search)


    temp_url=[]

    list_of_url=[]

    for i in range(10):
        list_of_url.append(result['d']['results'][i]['Url'])

    for url in list_of_url:
        temp_url.append(url.split('.'))

    flag=0
    counter=0

    for url in temp_url:
        counter+=1
        if 'azlyrics' in url:
            flag=1
            break

    if flag==0:
        return "Sorry, No Data Found :-("

    else:
        return list_of_url[counter-1]
<<<<<<< HEAD

if __name__=='__main__':
    # Stores name of the track
    search_track=raw_input("Enter name of song: ")

    # Stores name of the artist
    search_artist=raw_input("Enter name of artist: ")

    # Stores the final search query
    search = search_artist + " " +  search_track + " azlyrics"

    # Calls az_url function
    az_url(search)
=======
>>>>>>> af9563100d75ef3d504f7dce896ce3ad9e08edda
