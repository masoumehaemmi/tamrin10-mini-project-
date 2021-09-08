from media import Media
class Actors(Media):
    def __init__(self,n):
        self.name = n

    def show(self):
        print(self.name)