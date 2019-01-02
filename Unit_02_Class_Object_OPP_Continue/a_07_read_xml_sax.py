import xml.sax

class Myclass(xml.sax.ContentHandler):
    def __init__(self):
        self.currentElement = ""
        self.name = ""
        self.year = ""
        self.country = ""
    
    def startElement(self, tag, attributes):
        self.currentElement = tag
        if tag == "singsong":
            self.name = attributes["name"]
            self.year = attributes["year"]
            self.country = attributes["country"]
    
    def endElement(self, tag):
        if tag == "singsong":
            print("*" *50)
            print("Song name: ", self.name, ", year: ", self.year, ", country: ", self.country)


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    handerClass = Myclass()
    parser.setContentHandler(handerClass)
    parser.parse("./data/sing_song.xml")