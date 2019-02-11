# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.check_args(attrs)
                

    def handle_endtag(self, tag):
        print("End   :", tag)
        #check_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
     
        print("Empty :", tag)
        self.check_args(attrs)

    def check_args(self, attr):
        if len(attr) > 0:
            for name, value in attr:
                print(f"-> {name} > {value}")



parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())


