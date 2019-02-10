# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.runner(tag,attrs)

    def handle_startendtag(self, tag, attrs):
        self.runner(tag,attrs)
    
    def runner(self, tag, attrs):
        if len(attrs) == 0:
            print(tag)
        else:
            print(tag)
            for attr, val in attrs:
                print(f"-> {attr} > {val}")


parser = MyParser()
for _ in range(int(input())):
    parser.feed(input())


