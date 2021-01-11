from django.shortcuts import render

import requests

def youtube_search(request):
    search=''
    if request.method =='GET':
        search=request.GET.get('input_search')
        print('search :',search)
    url='https://www.googleapis.com/youtube/v3/search'
    prammetr={
        'key':'AIzaSyCHDN-ZHNWkON_ImzXzNP2s7LShFJ5D72I',
        'part':'snippet',
        'q':search,
        'type':'video',
        'maxResults':9,
    }
    search=''
    id_videos=[]
    r=requests.get(url,params=prammetr).json()
    results=r['items']
    print('results :',results)
    for result in results :
        id_videos.append(result['id']['videoId'])
    
    video_prammetr={
        'key':'AIzaSyCHDN-ZHNWkON_ImzXzNP2s7LShFJ5D72I',
        'part':'snippet,contentDetails',
        'id':','.join(id_videos)
    }
    video_url='https://www.googleapis.com/youtube/v3/videos'
    video_r=requests.get(video_url,params=video_prammetr).json()
    resultes=video_r['items']
    videos=[]
    for result in resultes:
        videos_info={
            'title':result['snippet']['title'],
            'id':result['id'],
            'image':result['snippet']['thumbnails']['high']['url'],
            'duration':result['contentDetails']['duration'],
        }
        videos.append(videos_info)
 
    context={
        'obj':videos
    }
    return render(request,'index.html',context)
