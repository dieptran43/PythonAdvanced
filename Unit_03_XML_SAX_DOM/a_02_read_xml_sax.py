import xml.sax


class MyClass(xml.sax.ContentHandler):
    def __init__(self):
        self.currentElement = ""
        self.name = ""
        self.year = ""
        self.country = ""
        self.category = ""
        self.singer = ""

    def startElement(self, tag, attributes):
        self.currentElement = tag
        if self.currentElement == "singsong":
            print("*****Sing song*****")
            # test attr name in method startElement vs method endElement
            name = attributes["name"]
            print("This is name: ", name)
            print("Year: ", attributes["year"])
            print("Country: ",attributes["country"])
    
    def endElement(self, tag):
        # test attr name in method startElement vs method endElement
        if self.currentElement == "name":
            print("Name end: ", self.name)

        if self.currentElement == "singsong":
            print("Year is: ", self.category)
            print("Country : ", self.category)

        elif self.currentElement == "category":
            print("Category is: ", self.category)
        elif self.currentElement == "singer":
            print("Singer is: ", self.singer)       
        
        self.currentElement = ""

    def characters(self, content):
        # test attr name in method startElement vs method endElement
        if self.currentElement == "name":
            self.name = content
        elif self.currentElement == "category":
            self.category = content
        elif self.currentElement == "singer":
            self.singer = content

if __name__ == "__main__":
    sax_parser = xml.sax.make_parser()
    sax_parser.setFeature(xml.sax.handler.feature_namespaces,0)

    handlerObj = MyClass()
    sax_parser.setContentHandler(handlerObj)
    sax_parser.parse("./data/sing_song_02.xml")
