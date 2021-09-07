from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

class Main:
    def __init__(self):
        try:
            filename=open("database.txt","r")
        except:
            print("error! database not fond")
        big_text=filename.read()
        parts= big_text.split("\n")

        self.list=[]
        i = 0

        while i< len(parts):
            info= parts[i].split(",")

            if info[1] == "film":
                self.list.append(Film(info))
            elif info[1]== "series":
                self.list.append(Series(info))
            elif info[1]== "documentary":
                self.list.append(Documentary(info))
            elif info[1]== "clip":
                self.list.append(Clip(info))
            else:
                print("wronge data!")
            i=+1

        #print(self.list)
        self.show_menu()

    def show_menu(self):
        print("1-enter show list: ")
        print("2-enter your add Video media: ")
        print("3-enter your edit Video media: ")
        print("4-enter your search Video media : ")
        print("5-enter your exit: ")

        user_select=int(input("enter a select number : "))
        if user_select== 1:
            self.show_info()
        elif user_select == 2:
            self.add_Video_Media(self)
        elif user_select ==3:
             self.show_edit_menu(self)
        elif  user_select ==4:
            self.del_Video_Media(self)
        elif user_select ==5:
            self.search_Video_Media(self)    
        elif user_select == 6:
            self.save_and_exit_media(self)
        else:
            print("wrong input!")
    def show_info(self):
        for i in len(self.list):
            self.show(self)

        self.show_menu()
    def add_Video_Media(self):

        Add_id=input("enter your id media :")
        Add_categori=input("enter your categori :")
        Add_name=input("enter your name media :")
        Add_directore=input("enter your director media :")
        Add_IMDB=input("enter your IMDB media :")
        Add_url=input("enter your url media :")
        Add_duration=input("enter your duration media :")
        
        if self.categori=="film":
            Add_casts=input("enter your actor media :")
        elif self.categori=="documentary" or self.categori=="clip":
            Add_episod=input("enter your episod documentary or clip :")
        elif self.series=="series":
            Add_casts=input("enter your casts :")
            Add_episod=input("enter your episod series :")
        info={"id":Add_id,"name":Add_name,"directore":Add_directore,"IMDB":Add_IMDB,"url":Add_url,"duration":Add_duration,"casts":Add_casts,"episod":Add_episod} 
        
        if self.categori == "film":
                self.list.append(Film(info))
        elif self.categori== "series":
                self.list.append(Series(info))
        elif self.categori== "documentary":
                self.list.append(Documentary(info))
        elif self.categori== "clip":
                self.list.append(Clip(info))
        else:
                print("wronge data!")

        self.show_menu()
        
    def show_edit_menu(self):
        print("1- categori")
        print("2- name")
        print("3- director")
        print("4- IMDB")
        print("5- url")
        print("6- duration")
        print("7- casts")
        print("8- episod")
        print("9- end")
    
    def edit_Video_Media(self):

        id = input("enter your idkala for edit :")
        for i in range (len(self.list)):
        
            if list[i]["id"] == id:
                while True:
                    self.show_edit_menu(self)
                    choice=input("choice from edit menu:")
                    if choice == 1:
                        new_categori =input("enter your new categori:")
                        self.list[i]["categori"] == new_categori
                    elif choice == 2:
                        new_name =input("enter your new name :")
                        self.list[i]["name"]== new_name
                    
                    elif choice ==3 :
                        new_director =input("enter your new director :")
                        self.list[i]["director"] == new_director

                    elif choice ==4 :
                        new_IMDB =input("enter your new IMDB :")
                        self.list[i]["IMDB"] == new_IMDB

                    elif choice ==5 :
                        new_url =input("enter your new url :")
                        self.list[i]["url"] == new_url

                    elif choice ==6 :
                        new_duration =input("enter your new duration :")
                        self.list[i]["duration"] == new_duration
                    
                    elif choice ==7 :
                        new_casts =input("enter your new casts :")
                        self.list[i]["casts"] == new_casts
                    
                    elif choice ==8 :
                        new_episod =input("enter your new episod :")
                        self.list[i]["episod"] == new_episod
                
                    elif choice == 9:
                        break
                    else:
                        print("no input")

    def del_Video_Media(self):
        id= input("enter your id media for delete :")
        
        for i in range(len(self.list)):
            if self.list[i]["id"]==id:
                self.list.pop(i)
                print("hazf shod")
                break

    def search_Video_Media(self):
    
        user_keyword = input("your id media or name for jostojo :")

        for i in range(len(self.list)):
        
           if self.list[i]['name'] == user_keyword or self.list[i]["id"]== user_keyword:
            print(self.list[i])             

    def save_and_exit_media(self):
        filename= open("database.txt","w")
       # r=0
        for i in range(len(self.list)):
            row = (self.list[i]["id"] + ',' + self.name[i]["categori"] + "," + self.list[i]["name"] 
            + ',' + self.list[i]["director"] + ',' + self.list[i]["IMDB"] + ',' + self.list[i]["url"] 
            + ',' + self.list[i]["duration"] + ',' + self.list[i]["casts"] + ',' + self.list[i]["episod"])
            filename.write(row)
        #    r=r+1
        #    if r<len(PRODUCTION):
        #        my_file.write("\n")
        filename.close()
        exit()    
f=Main()


    
