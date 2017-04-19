import requests
from bs4 import BeautifulSoup


class WebmdCrawler:
    def __init__(self, name):
        self.name = name

    def startCrawling(self):
        url = "http://www.webmd.com/search/search_results/default.aspx"
        querystring = {"query": self.name}
        headers = {}
        response = requests.request("GET", url, headers=headers, params=querystring)
        soup = BeautifulSoup(response.text,"html.parser")
        elements = soup.find_all("div", class_="search-results-doc-container")
        dataToBeSaved = []
        for element in elements:
            tags=element.find_all('a',href=True)
            if len(tags)!=0:
                link=tags[0]['href']
                title = tags[0].text.strip()
                dataToBeSaved.append({
                    'link': link,
                    'title': title
                })
                print link
        return {
            "name": self.name,
            "type": "webmd",
            "data": dataToBeSaved
        }

