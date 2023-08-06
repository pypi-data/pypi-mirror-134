from urllib.request import Request, urlopen
import time
import json
import re

from youpi.cache import cached
from youpi.streamlist import StreamList
from youpi.stream import Stream
from youpi.semi_singleton import SemiSingleton


class YouTube:
    def __init__(self, url):
        self.url = url
        self.raw = self.get_info(url)
        #with open('info.json', 'w') as f:
        #    json.dump(self.raw, f)
        
        self.title = self.raw['videoDetails']['title']
        self.author = self.raw['videoDetails']['author']
        self.channel_id = self.raw['videoDetails']['channelId']
        self. view_count = self.raw['videoDetails']['viewCount']
        self.thumbnailurl = self.raw['videoDetails']['thumbnail']['thumbnails'][-1]['url']
        
        self.singleton = SemiSingleton(self.title)
        
        stream_list = []
        for i in self.raw['streamingData']['formats']:
            stream_list.append(self.convert(i, progressive=True))
        for i in self.raw['streamingData']['adaptiveFormats']:
            stream_list.append(self.convert(i, progressive=False))
        self.streams = StreamList(stream_list)
    
    @cached(is_classmethod=True, expireFunc = lambda raw: time.time() + int(raw['streamingData']['expiresInSeconds'])-30)
    def get_info(self, url, client='android'):
        video_id = self.get_youtube_id(url)
        
        headers = {'Content-Type': 'application/json', "User-Agent": "Mozilla/5.0", "accept-language": "ko_KR,en-US;q=0.8,en;q=0.6"}
        data = {
            'android':{'context': {'client': {'clientName': 'ANDROID', 'clientVersion': '16.20'}}},
            'android_embed':{'context': {'client': {'clientName': 'ANDROID', 'clientVersion': '16.20','clientScreen': 'EMBED'}}},
            'web':{'context': {'client': {'clientName': 'WEB','clientVersion': '2.20200720.00.02'}}},
            'web_embed':{'context': {'client': {'clientName': 'WEB','clientVersion': '2.20200720.00.02','clientScreen': 'EMBED'}}}
        }
        
        endpoint_url = f'https://www.youtube.com/youtubei/v1/player?videoId={video_id}&key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&contentCheckOk=True&racyCheckOk=True'
        
        
        req = Request(endpoint_url, bytes(json.dumps(data[client]), encoding="utf-8"), headers=headers)
        response = urlopen(req)
        response_json = json.loads(response.read())
        return response_json
    
    def get_youtube_id(self, url):
        if(len(url)==11):
            return url
        
        regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(embed/|v/|.+[?&]v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
        return regex.match(url).group('id')
        
    def convert(self, s, progressive=False):
        itag = s.get('itag')
        url = s.get('url')
        
        # ex) video/3gpp; codecs="mp4v.20.3, mp4a.40.2"
        mimetype = s.get('mimeType')
        datatype = 'both' if progressive else mimetype[:mimetype.index('/')] 
        extension = mimetype[mimetype.index('/')+1:mimetype.index(';')]
        
        vcodec = acodec = None
        if datatype == 'both':
            vcodec, acodec = mimetype.split('"')[1].split(', ')
        elif datatype == 'video':
            vcodec = mimetype.split('"')[1]
        elif datatype == 'audio':
            acodec = mimetype.split('"')[1]
        
        res = s.get('height')
        fps = s.get('fps')
        bitrate = s.get('bitrate')
        samplerate=s.get('audioSampleRate')
        return Stream(self.singleton, itag, url, datatype, extension, vcodec, acodec, res, fps, bitrate, samplerate)