import pytube
from pytube import YouTube

class Media:
    def __init__(self,id,c,n,di,im,u,du):
        self.id=id
        self.categori=c
        self.name=n
        self.director=di
        self.IMDB_score=im
        self.url=u
        self.duration=du
        #self.casts=ca

    def show(self):
       
        print(f"id : {self.id} *** categori : {self.categori} *** name : {self.name} *** director : {self.director} *** IMDB : {self.IMDB_score} ")

    def download(self):
        url=input("enter your url for download :")
        for i in range (len(self.list)):
            if url==self.url:
                link=self.url
                first_stream=pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./',filename="test.mp4")
               #print(first_stream)
  
