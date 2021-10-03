from urllib.parse import urlparse, parse_qs
import requests
import os
inurl = input("Input video url here: ")

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
        if query.path[:9] == '/playlist': return parse_qs(query.query)['list'][0]

vidid= extract_video_id(inurl)
imgurl = f"https://img.youtube.com/vi/{vidid}/hqdefault.jpg"

response = requests.get(imgurl)

file = open("hq720.jpg", "wb")
file.write(response.content)
file.close()
os.rename("hq720.jpg", "image.jpg")
print("Thumbnail saved as image.jpg to current folder!")