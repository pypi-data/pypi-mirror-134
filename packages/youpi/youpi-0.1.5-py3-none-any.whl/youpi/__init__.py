from .cache import cached
from .stream import Stream
from .streamlist import StreamList
from .youtube import YouTube
from .semi_singleton import SemiSingleton


__all__ = ['cached', 'Stream', 'StreamList', 'YouTube', 'SemiSingleton']

'''SAMPLE
yt = YouTube('https://www.youtube.com/watch?v=AdeXDmBm69Q')
streams = yt.streams
print(yt.title)
print(yt.author)
print(yt.channel_id)
print(yt.view_count)
print(streams)
streams.get_by_itag(136).download()
'''