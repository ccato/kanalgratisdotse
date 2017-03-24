TITLE = 'KanalGratisDotSE'
PREFIX = '/video/kanalgratisdotse'

ICON = 'icon-default.png'
URL = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCwTrHPEglCkDz54iSg9ss9Q'

####################################################################################################
def Start():
    ObjectContainer.title1 = TITLE


####################################################################################################
@handler('/video/kanalgratisdotse', 'KanalGratisDotSE')
def MainMenu():
    feed = XML.ElementFromURL(URL)

    for entries in feed.xpath('//feed/entry'):
        for entry in entries:
            title = entry.xpath('./media:group/media:title/text()')[0]
            url = entry.xpath('./link/@href')[0]
            thumb = entry.xpath('./media:thumbnail/@url')[0]
            desc = entry.xpath('./media:description/text()')[0]
            date = entry.xpath('./published/text()')[0]

            oc.add(VideoClipObject(
                url=url,
                title=title,
                thumb=Resource.ContentsOfURLWithFallback(url=thumb),
                summary = desc,
                originally_available_at = date
            ))
    return oc

