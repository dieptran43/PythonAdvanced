import xml.sax

class MyClass(xml.sax.ContentHandler):
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
            print("* "*30)
            print(self.name.ljust(30), self.year.rjust(10), self.country.center(20))

#run code
if __name__ == "__main__":
    sax_parser = xml.sax.make_parser()
    handlerObj = MyClass()
    sax_parser.setContentHandler(handlerObj)

    print("Name".ljust(30), "Year".rjust(10), "Country".center(20))
    sax_parser.parse("./data/sing_song_01.xml")
