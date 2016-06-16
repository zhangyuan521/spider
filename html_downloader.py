# coding:utf-8
import urllib2
class HtmlDownloader:
    def download(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        return response.read()
