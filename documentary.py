from media import Media
class Documentary(Media.Media):
    def __init__(self,media):
        media.__init__(self,media[0],media[1],media[2],media[3],media[4],media[5],media[6])
        self.episod=media[7]