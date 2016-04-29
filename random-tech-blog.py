import requests
import xmltodict
import random
import webbrowser


class Feed():

    def __init__(self, url):
        self.url = url

    def getUrl(self):
        return self.url


class FeedList():

    def __init__(self, feeds):
        self.feeds = feeds

    def getFeeds(self):
        return self.feeds


class LoadFeed():

    def __init__(self, url):
        page = requests.get(url)
        feedList = []
        feeds = xmltodict.parse(page.text)
        for f in feeds['opml']['body']['outline']['outline']:
            feedList.append(Feed(f['@htmlUrl']))

        self.feedList = FeedList(feedList)

    def getFeedList(self):
        return self.feedList


class LoadRandom():

    def __init__(self, url):
        fl = LoadFeed(url)
        self.feedList = fl.getFeedList().getFeeds()

    def openTechBlogInBrowser(self):
        webbrowser.open(self.randomTechBlog())

    def randomTechBlog(self):
        return random.choice(self.feedList).getUrl()

if __name__ == "__main__":
    lr = LoadRandom("https://raw.githubusercontent.com/kilimchoi/" +
                    "engineering-blogs/master/engineering_blogs.opml")
    lr.openTechBlogInBrowser()
