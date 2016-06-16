import url_manager,html_downloader,html_parser,html_outputer

class Spider:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser  = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url,url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(url, html_cont)
                self.urls.add_new_urls(new_urls)
                print(new_data)
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count +=1
            except Exception as e:
                print e
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    url = "http://baike.baidu.com"
    spider = Spider()
    spider.craw(root_url,url)