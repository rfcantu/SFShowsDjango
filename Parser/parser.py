import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from cleantext import clean

def getContent(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    parsed = BeautifulSoup(page, "html.parser")
    return parsed

def parseTheFillmore(url):
    found = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    parsed = getContent(url)
    for el in parsed.find_all(class_="faq_main"):
        el = clean(el.get_text(), lower=False, no_line_breaks=True)
        split = el.split(",")
        for i in range(0, len(days)):
            if split[0].find(days[i]):
                split[0] = split[0].replace(days[i], "").strip()
        split[1] = split[1].strip()
        found.append(split)
        statement = "INSERT INTO shows_show(artist, date, venue_id) VALUES ('{artist}', '{date}', 3);".format(artist = split[0], date = split[1])
        print(statement)
    return found

def parseBottomOfTheHill(url):
    found = []
    parsed = getContent(url)
    for el in parsed.find_all("tr.even"):
        el = clean(el.get_text(), lower=False, no_line_breaks=True, no_punct=True)
        inside = []
        inside.append(el)
        found.append(inside)
    return found

def parseGreatAmericanMusicHall(url):
    found = []
    parsed = getContent(url)
    for el in parsed.find_all(class_="list-view-item"):
        el = clean(el.get_text(), lower=False, no_line_breaks=False, no_punct=True)
        el = el.replace("More", "")
        el = el.replace("Info", "")
        split = el.split("\n")
        found.append(split)
        statement = "INSERT INTO shows_show(artist, date, venue_id) VALUES ('{artist}', '{date}', 2);".format(artist = split[1], date = split[2])
        print(statement)
    return found

def main():
    all_parsed = []
    x = 0
    url = "https://thefillmore.com/calendar/"
    all_parsed.append(parseTheFillmore(url))
    # url = "http://www.bottomofthehill.com/calendar.html#sthash.SjLaNJKm.dpbs"
    # all_parsed.append(parseBottomOfTheHill(url))
    url = "https://slimspresents.com/great-american-music-hall/"
    all_parsed.append(parseGreatAmericanMusicHall(url))
    #for i in all_parsed:
     #   print(i)
main()
