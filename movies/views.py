from django.shortcuts import render
import tmdbsimple as tmdb
from decouple import config,Csv
from googleapiclient.discovery import build
import requests,json

# Create your views here.
#API KEYS and Request Parameters
tmdb.API_KEY =config('API_KEY')  
YOUTUBE =  config('YOUTUBE_API_KEY') 

# Create your views here.
def movies(request):
    popular_movies_tmdb = tmdb.Movies('popular')
    popular_movies = popular_movies_tmdb.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    # nowshowing_movies_tmdb = tmdb.Movies('nowshowing')
    # nowshowing_movies = nowshowing_movies_tmdb.info()['results']

    return render(request, 'index.html', {'popular':popular_movies, 'upcoming':upcoming_movies})



# def youtube_movie(request):
#     # Get movie name and use it to pass it as an argument to the youtube api.
#     movie_name = movies['original_title']
#     youtube = build( YOUTUBE)
#     search_response = youtube.search().list(q=movie_name, part='id,snippet', maxResults=1).execute()
#     for search_result in search_response.get('items', []):
#         if search_result['id']['kind'] == 'youtube#video':
#             video_id = search_result['id']['videoId']
#         return render(request, 'youtube_movie.html', {'movies':movies, 'videoId':video_id})

def indexpage(request,category):
    key =  config('API_KEY')  
    url =  config('url') 
    url2 = url.format(category,key)
    urll = requests.get(url2)
    urlll = urll.json()
    return urlll

def youtube(request,id):
    YOUTUBE =  config('YOUTUBE_API_KEY') 
    popular = indexpage(request,'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = YOUTUBE)
    req = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = req.execute()
    return render(request,'youtube_movie.html',{'response':res})