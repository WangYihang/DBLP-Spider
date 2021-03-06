import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, title, authors, conf, year, dblp_key, doi_link, bibtex_link) -> None:
        self.title = title
        self.authors = authors
        self.doi_link = doi_link
        self.conf = conf
        self.year = year
        self.dblp_key = dblp_key
        self.bibtex_link = bibtex_link

    def __str__(self):
        if len(self.authors) > 0:
            return "[{} - {}] {} - {}".format(self.conf, self.year, self.title, self.authors[0])
        else:
            return "[{} - {}] {}".format(self.conf, self.year, self.title)

    def get_bibtex(self):
        response = requests.get(self.bibtex_link)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        bibtex = soup.find("pre", class_="verbatim select-on-click").text
        return bibtex
