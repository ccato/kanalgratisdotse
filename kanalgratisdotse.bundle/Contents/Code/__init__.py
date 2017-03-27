TITLE = 'KanalGratisDotSE'
PREFIX = '/video/kanalgratisdotse'
NS = {'atom': 'http://www.w3.org/2005/Atom','media':'http://search.yahoo.com/mrss/'}

ICON = 'icon-default.png'
URL = 'https://www.youtube.com/feeds/videos.xml?user=kanalgratisdotse'


####################################################################################################
def Start():
    ObjectContainer.title1 = TITLE


####################################################################################################
@handler('/video/kanalgratisdotse', 'KanalGratisDotSE')
def MainMenu():
    oc = ObjectContainer()
    feed = XML.ElementFromURL(URL)

    for entry in feed.xpath('/atom:feed/atom:entry', namespaces=NS):
        try:
            oc.add(VideoClipObject(
                url=entry.xpath('./atom:link/@href', namespaces=NS)[0],
                title=entry.xpath('./media:group/media:title/text()', namespaces=NS)[0],
                thumb=Resource.ContentsOfURLWithFallback(url=entry.xpath('./media:group/media:thumbnail/@url', namespaces=NS)[0]),
                summary=entry.xpath('./media:group/media:description/text()', namespaces=NS)[0],
                originally_available_at=Datetime.ParseDate(entry.xpath('./atom:published/text()', namespaces=NS)[0])
            ))
        except Exception, e:
            Log("Error: %s" % str(e))
    return oc
