"""
Page Scraper - Create an application which connects to a site and pulls out all links,
or images, and saves them to a list. Optional: Organize the indexed content and don’t allow
duplicates. Have it put the results into an easily searchable index file.
"""
# noinspection PyCompatibility
import _pickle as pickle
import re
import time
# noinspection PyCompatibility
from urllib import request
from bs4 import BeautifulSoup

URL_BASE = "http://www.pj.ma/pagesjaunes?"


class PJ:
    """
        PJ object that executes queries and returns set of results

        URL templates to make PJ searches.
            http://www.pj.ma/pagesjaunes?page=2&pro_quiquoi=ophtalmologue&pro_ou=Casablanca
            http://www.google.com/search?
            page=page number
            &pro_quiquoi= object of search
            &pro_ou= location
    """

    def __init__(self, pause=5.0, page=1, pj_query="", location=""):
        """
            :type  pause: long
            url, not to burden the server
            :type  page: int
            :param page: pagination
            :type  pj_query: str
            :param pj_query: the object of the search
            :type  location: str
            :param location: where to look
            :rtype:  object
            :return: the instance of PJ
        """
        self.pause = pause
        self.page = page
        self.query = pj_query
        self.location = location

    def set_pause(self, pause):
        """:param pause:"""
        self.pause = pause

    def set_page(self, page=0):
        """:param page:"""
        self.page = next if page > 0 else self.page + 1

    def get_page(self):
        """:return:"""
        return self.page

    def set_query(self, s_query):
        """:param s_query:"""
        self.query = s_query

    def set_location(self, location):
        """:param location:"""
        self.location = location

    def __url_construction(self):
        """
        Construct the search url
        """
        url_search = URL_BASE
        # page
        page = "page=%(page)s&" % {"page": self.page}
        url_search += page
        # pro_quiquoi
        url_query = "pro_quiquoi=%(query)s&" % {"query": self.query}
        url_search += url_query
        # pro_ou
        location = "pro_ou=%(location)s&" % {"location": self.location}
        url_search += location
        return url_search

        # Returns a generator that yields URLs.

    def search(self, file=None):
        """
        Returns search results for the current query as a iterator.
        """
        # pause, so as to not overburden PJ
        # time.sleep(self.pause+(random.random()-0.5)*5)

        # Request the PJ Search results page.
        while True:
            try:
                html = self.__get_result(self.__url_construction())
                # Parse the response and extract the summaries
                if BeautifulSoup(html, features="lxml").findAll(text=re.compile("captcha")):
                    print("Failed page " + str(self.get_page()) + ", captcha retrying")
                else:
                    break
            except TypeError:
                print("Failed page " + str(self.get_page()) + ", retrying")
                time.sleep(4)

        # noinspection SpellCheckingInspection
        if BeautifulSoup(html, features="lxml").findAll(text=re.compile("cette recherche")):
            # noinspection SpellCheckingInspection
            print(BeautifulSoup(html).findAll(text=re.compile("cette recherche")))
            return False

        # noinspection SpellCheckingInspection
        for table in BeautifulSoup(html, features="lxml").findAll("li",
                                                                {"class": "gauchezonebcenter"}):
            result = ""
            # noinspection Pylint
            try:
                # noinspection SpellCheckingInspection
                search_prof = ' '.join(re.findall('\w+', table.findNext("h2", {
                    "class": "annoncesd-ttre"}).a.findNext(text=True)))
                result += search_prof + ' | '
                # noinspection SpellCheckingInspection
                activity = ' '.join(re.findall('\w+', table.findNext("div", {
                    "class": "annoncesd-Activite"}).span.findNextSiblings(text=True)[0]))
                result += activity + ' | '
                # noinspection SpellCheckingInspection
                address_phone = table.findNext("li", {"class": "annoncesd-adressec"})
                glo_address = address_phone.div.div
                address = ' '.join(re.findall('\w+', glo_address.next.string))
                result += address + ' | '
                city = ' '.join(re.findall('\w+', glo_address.strong.string))
                result += city + ' | '
                phones = address_phone.span.findNextSibling('strong')
                phone1 = ' '.join(re.findall('\w+', phones.string))
                result += phone1 + ' | '
                phone2 = ' '.join(re.findall('\w+', phones.findNextSibling('strong').string))
                result += phone2 + ' | '
            except AttributeError:
                pass
            try:
                pickle.dump(result, file)
            except TypeError:
                pass
        return True

    @staticmethod
    def __get_result(url):
        """
        Request the given URL and return the response page, using the cookie jar.

        :type  url: str
        :param url: URL to retrieve.

        :rtype:  str
        :return: Web page retrieved for the given URL.

        :raise IOError: An exception is raised on error.
        :raise urllib2.URLError: An exception is raised on error.
        :raise urllib2.HTTPError: An exception is raised on error.
        """
        requests = request.Request(url)
        requests.add_header('User-Agent',
                            'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        response = request.urlopen(requests)
        html = response.read()
        response.close()
        return html


# When run as a script, take all arguments as a search query and run it.
if __name__ == "__main__":
    PROF = open("medecins.txt", "w")
    QUERY = 'medecin'
    P_J = PJ()
    P_J.set_query(QUERY)
    STAT = True
    while STAT:
        STAT = P_J.search(PROF)
        P_J.set_page()
    PROF.close()
