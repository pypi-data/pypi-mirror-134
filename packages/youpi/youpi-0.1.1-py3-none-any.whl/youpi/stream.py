from urllib.request import urlopen, Request

class Stream:
    def __init__(
        self,
        itag,
        url,
        datatype,
        extension,
        vcodec = None,
        acodec = None,
        res = None,
        fps = None,
        bitrate = None,
        samplerate = None
    ):
        self.itag=itag
        self.url=url
        self.datatype=datatype
        self.extension=extension
        self.vcodec=vcodec
        self.acodec=acodec
        self.res=res
        self.fps=fps
        self.bitrate=bitrate
        self.samplerate=samplerate
        
    def __repr__(self):
        if self.datatype=='both':
            return f'<{self.itag}, video&audio({self.extension}), {self.res}p/{self.fps}fps, vcodec={self.vcodec}, acodec={self.acodec}>'
        elif self.datatype=='video':
            return f'<{self.itag}, video({self.extension}), {self.res}p/{self.fps}fps, vcodec={self.vcodec}>'
        elif self.datatype=='audio':
            return f'<{self.itag}, audio({self.extension}), {self.bitrate/1000}kbps/{self.samplerate}kHz, acodec={self.acodec}>'
        return 'hello'
        
    def download(self, filename='filename'):
        MB = 1024*1024
        headers = {'Content-Type': 'application/json', "User-Agent": "Mozilla/5.0", "accept-language": "ko_KR,en-US;q=0.8,en;q=0.6"}
        
        def stream(url, chunk_size = 9437184):
            file_size = chunk_size  # fake filesize to start
            downloaded = 0
            while downloaded < file_size:
                stop_pos = min(downloaded + chunk_size, file_size) - 1
                range_header = f"bytes={downloaded}-{stop_pos}"

                headers.update({"Range": range_header})
                req = Request(url, headers=headers)
                response = urlopen(req)

                if file_size == chunk_size:
                    content_range = response.info()["Content-Range"]
                    file_size = int(content_range.split("/")[1])
                    print(file_size/1024/1024,'MB')
                
                chunk = response.read()
                downloaded += len(chunk)
                yield chunk, file_size, downloaded
            return

        with open(filename+'.'+self.extension, "wb") as f:
            for chunk, file_size, downloaded in stream(self.url, chunk_size=10*MB):
                print(f'{downloaded/MB:.1f}/{file_size/MB:.1f} MBs downloading...')
                f.write(chunk)