__author__ = 'Artemko'

from BeautifulSoup import BeautifulSoup
import mechanize


class Crawler:
    def __init__(self, url):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-Agent',
                          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")]

        self._br = br
        self._content = self._br.open(url).read()

    def get_skills(self):
        # content = self._br.open(url).read()
        result = map(lambda x: x.text.encode('utf-8'),
                     BeautifulSoup(self._content).findAll('a', 'endorse-item-name-text'))
        if not result:
            raise ValueError("No skills found")
        return result

    def get_profs(self):
        # content = self._br.open(url).read()
        result = map(lambda x: x.text.encode("utf-8"),
                     [prof.div.header.h4 for prof in BeautifulSoup(self._content).findAll("div", "current-position") +
                      BeautifulSoup(self._content).findAll("div", "past-position")])
        # result = map(lambda x: x,
        #         divs =        BeautifulSoup(content).findAll(("div"), "current-position")
        #         for x in divs:
        #             print x.div.header.h4.text
        #         divs2 = BeautifulSoup(content).findAll(("div"), "past-position")
        #         for x in divs2:
        #             print x.div.header.h4.text
        if not result:
            raise ValueError("No profs found")
        return result

# link_name = "https://www.linkedin.com/pub/r-unni-menon/21/347/764"
# crawler = Crawler()
# print crawler.get_skills(link_name)
# print crawler.get_profs(link_name)
