import ast
import pytube
from pytube import YouTube

class Media:
    def __init__(self,id,c,n,di,im,u,du,ca):
        self.id=id
        self.categori=c
        self.name=n
        self.director=di
        self.IMDB_score=im
        self.url=u
        self.duration=du
        self.casts=ca

    def show(self):
        # self.list=[]
        # self.mydict={}
        # myfile=open("databasefilm.txt","r")
        # rows=myfile.read().split("\n")
        # for i in range(len(rows)):
        #     medi=rows[i].split(",")
        #     self.mydict["id"]=int(medi[0])
        #     self.mydict["name"]=medi[1]
        #     self.mydict["director"]=medi[2]
        #     self.mydict["IMDB"]=float(medi[3])
        #     self.mydict["url"]=medi[4]
        #     self.mydict["duration"]=int(medi[5])
        #     self.mydict["casts"]=medi[6]
        #     print(self.mydict)
        #     self.list.append(self.mydict)
        # #return self.list  
        print(f"id : {self.id} *** categori : {self.categori} *** name : {self.name} *** director : {self.director} *** IMDB : {self.IMDB_score} ")

    def download(self):
        link='http://www.youtube.com/watch?v=lVFNRrL79w0'
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename="test.mp4")
        #print(first_stream)
    



   