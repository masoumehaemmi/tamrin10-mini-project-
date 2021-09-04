import film
import series
import documentary
import clip
import time
import os
import main
class Media:
    def __init__(self,id,n,di,im,u,du,c):
        self.id=id
        self.name=n
        self.director=di
        self.IMDBscore=im
        self.url=u 
        self.duration=du 
        self.casts=c
       
    def show_menu(ce):
        print("1-enter your add Video media: ")
        print("2-enter your edit Video media: ")
        print("3-enter your search Video media : ")
        print("4-enter your exit: ")

    def add_Video_Media(self):
        Add_id=int(input("enter your id media :"))
        Add_name=input("enter your name media :")
        Add_directore=input("enter your director media :")
        Add_IMDB=float(input("enter your IMDB media :")) 
        Add_url=input("enter your url media :")
        Add_duration=int(input("enter your duration media :"))
        Add_casts=input("enter your actor media :")
        self.mydict={"id":int(Add_id),"name":Add_name,"directore":Add_directore,"IMDB":float(Add_IMDB),"url":Add_url,"duration":int(Add_duration),"casts":Add_casts} 
        self.list.append(self.mydict)
        

        
f=Media(1,"nagahanderakht","safiyazdanian",4.9,"url:http://namadownload.ir.domains.blog.ir/post/download-film-nagahan-derakht",91,"peimanmoadi")
# f.showInfo()

# print(f.download())

f.show_menu()

while True:
    ce=int(input("enter a select number : "))

    if ce == 1:
       print(f.add_Video_Media())
    elif ce == 2:
        pass
    elif ce == 3:
        pass
    elif ce == 4:
        exit()
