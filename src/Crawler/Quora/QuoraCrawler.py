from selenium import webdriver
import os
import time
currentDir = os.getcwd()
driverLocation = os.path.join(currentDir, '../driver/phantomjs/phantomjs-2.1.1-macosx/bin/phantomjs')


class QuoraCrawler:

    def __init__(self, interest):
        self.interest = interest
        self.driver = webdriver.PhantomJS(driverLocation)
        self.driver.set_window_size(1120, 550)

    def startCrawling(self):
        driver=self.driver
        url="https://www.quora.com/topic/"+self.interest.replace(' ','-')
        driver.get(url)

        currentHeightOfDocument=driver.execute_script("var body = document.body,html = document.documentElement;var height = Math.max( body.scrollHeight, body.offsetHeight,html.clientHeight, html.scrollHeight, html.offsetHeight ); return height")
        sleepTime=0
        while sleepTime!=10:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            foundHeightOfDocument=driver.execute_script("var body = document.body,html = document.documentElement;var height = Math.max( body.scrollHeight, body.offsetHeight,html.clientHeight, html.scrollHeight, html.offsetHeight ); return height")
            if foundHeightOfDocument!=currentHeightOfDocument:
                sleepTime += 1

        # pageSource=driver.page_source
        allQuestionElements=driver.find_elements_by_class_name("feed_item_inner")
        dataToBeSaved=[]
        for element in allQuestionElements:
            mainThing=element.find_element_by_class_name('question_link')
            link=mainThing.get_attribute('href')
            print link
            title=mainThing.text

            dataToBeSaved.append({
                'link':link,
                'title':title
            })
        return {
            "name":self.interest,
            "type":"quora",
            "data":dataToBeSaved
        }
    @staticmethod
    def getSeconds():
        seconds = int(round(time.time()))
        return seconds