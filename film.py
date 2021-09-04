import media

class Film(media.Media):
    
    def __init__(self):
        self.list=[]
        mydict={}
        myfile=open("databasefilm.txt","r")
        rows=myfile.read().split("\n")
        for i in range(len(rows)):
            media=rows[i].split(",")
            
            mydict["id"]=int(media[0])
            mydict["name"]=media[1]
            mydict["director"]=media[2]
            mydict["IMDB"]=float(media[3])
            mydict["url"]=media[4]
            mydict["duration"]=int(media[5])
            mydict["casts"]=media[6]
            self.list.append(self.mydict)
        return self.list  

    def show(self):
        print()
f=Film()
print(f)
