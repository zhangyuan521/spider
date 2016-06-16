# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser:
    def parse(self,url,cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont,'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup)
        new_urls = self._get_new_url(url,soup)
        return new_urls, new_data

    def _get_new_url(self,url,soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,soup):
        res_data = {}
        try:
            title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
            res_data['title'] = title.get_text()
            summary = soup.find('div', class_="lemma-summary")
            res_data['summary'] = summary.get_text()
        except Exception as e:
            print e
        finally:
            return res_data
