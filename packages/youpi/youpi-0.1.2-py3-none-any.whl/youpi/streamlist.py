from typing import List
from .stream import Stream


class StreamList:
    def __init__(self, stream_list: List[Stream]):
        self.stream_list=stream_list
    
    def get_by_itag(self, itag: int):
        ret = next((s for s in self.stream_list if s.itag==itag), None)
        return ret
    
    def get(self, index):
        if not self.stream_list:
            return None
        return self.stream_list[index]
    
    def best_video(self):
        video_list = [s for s in self.stream_list if s.datatype == 'video']
        if not video_list:
            return None
        
        ret = video_list[0]
        for s in video_list:
            if ret.res < s.res:
                ret = s
            elif ret.res == s.res:
                if ret.fps < s.fps:
                    ret = s
                elif ret.fps == s.fps:
                    if s.extension == 'mp4':
                        ret = s
        return ret
    
    def best_audio(self):
        audio_list = [s for s in self.stream_list if s.datatype == 'audio']
        if not audio_list:
            return None
        
        ret = audio_list[0]
        for s in audio_list:
            if ret.bitrate < s.bitrate:
                ret = s
        return ret
    
    def best_both(self):
        both_list = [s for s in self.stream_list if s.datatype == 'both']
        if not both_list:
            return None
        
        ret = both_list[0]
        for s in both_list:
            if ret.res < s.res:
                ret = s
            elif ret.res == s.res:
                if ret.fps < s.fps:
                    ret = s
                elif ret.fps == s.fps:
                    if s.extension == 'mp4':
                        ret = s
        return ret
    
    def filter(
        self,
        res=None,
        fps=None,
        datatype=None,
        extension=None,
        bitrate=None
    ):
        filter_list = []
        if res: filter_list.append(lambda s: s.res == res)
        if fps: filter_list.append(lambda s: s.fps == fps)
        if datatype: filter_list.append(lambda s: s.datatype == datatype)
        if extension: filter_list.append(lambda s: s.extension == extension)
        if bitrate: filter_list.append(lambda s: s.bitrate == bitrate)
        
        ret = self.stream_list
        for filter in filter_list:
            ret = [s for s in ret if filter(s)]
        return StreamList(ret)
    
    def __repr__(self):
        ret = ''
        for s in self.stream_list:
            ret += s.__repr__() + '\n'
        return ret