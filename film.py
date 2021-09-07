from media import Media

class Film(Media):
    
    def __init__(self,media):
        
        Media.__init__(self,media[0],media[1],media[2],media[3],media[4],media[5],media[6],media[7])

    
#         self.list=[]
#         mydict={}
#         myfile=open("databasefilm.txt","r")
#         rows=myfile.read().split("\n")
#         for i in range(len(rows)):
#             media=rows[i].split(",")
            
#             mydict["id"]=int(media[0])
#             mydict["name"]=media[1]
#             mydict["director"]=media[2]
#             mydict["IMDB"]=float(media[3])
#             mydict["url"]=media[4]
#             mydict["duration"]=int(media[5])
#             mydict["casts"]=media[6]
#             self.list.append(self.mydict)
#         return self.list  

#     def show(self):
#         print()
# # f=Film()
# # print(f)
