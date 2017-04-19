from src.Crawler.Quora.QuoraCrawler import QuoraCrawler
from src.Crawler.Webmd.WebmdCrawler import WebmdCrawler
from src.Crawler.ThriveGoal.ThriveGoalCrawler import ThriveGoalCrawler
from flask import Flask,request
import json
app = Flask(__name__)


import threading


class MyThread(threading.Thread):
    def __init__(self, name, interest):
        threading.Thread.__init__(self)

        self.name = name
        self.interest = interest
        self.returnData = ''

    def run(self):
        print self.name + ' starting'
        if self.name == "Quora":
            Qc = QuoraCrawler(self.interest)
            dataQuora = Qc.startCrawling()
            self.returnData = dataQuora
        if self.name == "Webmd":
            Wc = WebmdCrawler(self.interest)
            webmdData = Wc.startCrawling()
            self.returnData = webmdData
        print self.name + ' ending'

    def join(self):
        threading.Thread.join(self)
        return self.returnData

@app.route('/',methods=['POST'])
def main():
    # Create new threads
    interest=json.loads(request.data)['interest']
    thread1 = MyThread("Quora",interest)
    thread2 = MyThread("Webmd", interest)
    # return 'hey'
    # Start new Threads
    thread1.start()
    thread2.start()
    returnData={
        "quora":thread1.join(),
        "webmd":thread2.join()
    }


    return json.dumps(returnData)
    # Tc = ThriveGoalCrawler('Abdominal Pain')
    # Tc.startCrawling()


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
