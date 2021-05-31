import os
import requests
import termcolor

from core.article import Article
from core.conference import Conferences
from bs4 import BeautifulSoup

print_success = lambda x: termcolor.cprint(x, 'green')
print_error = lambda x: termcolor.cprint(x, 'red')
print_warning = lambda x: termcolor.cprint(x, 'yellow')
print_info = lambda x: termcolor.cprint(x)

def legalise_filename(filename):
    illegal_chars = {"|":"OR"}
    legal_filename = filename
    for k, v in illegal_chars.items():
        legal_filename = legal_filename.replace(k, v)
    return legal_filename

class DBLP:
    def search(self, area, conf):
        if conf:
            keyword = "{} venue:{}:".format(area, conf.venue)
        else:
            keyword = area
        print_info("[*] Searching {} on {}".format(termcolor.colored(area, "cyan"), conf))
        params = {
            "q": keyword,
            "h": 30,
            "f": 0,
            "s": "ydvspc",
        }
        url = "http://dblp.uni-trier.de/search/publ/inc"
        
        response = requests.get(url, params=params)
        content = response.text
        articles = self.parse(content)
        return articles

    def save(self, area, articles):
        folder = os.path.join("result", area)
        try: os.makedirs(folder)
        except: pass
        bibtexes = []
        if len(articles) > 0:
            for article in articles:
                bibtexes.append(article.bibtex)
            bibtexes_filename = legalise_filename("{} - {}.bib".format(area, conf.short))
            bibtexes_path = os.path.join(folder, bibtexes_filename)
            with open(bibtexes_path, "w") as f:
                f.write("\n".join(bibtexes))

    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        articles_li = soup.find_all(class_="toc")
        articles = []
        for article_li in articles_li:
            doi_link = article_li.find("a")["href"]
            title = article_li.find("span", class_="title").text
            author_spans = article_li.find_all("span", itemprop="author")
            authors = []
            for author_span in author_spans:
                authors.append(author_span.find("span")["title"])
            confname = article_li.find("span", itemprop="isPartOf").find("span", itemprop="name").text
            pub_year = article_li.find("span", itemprop="datePublished").text
            dblp_key = article_li.find("ul", class_="bullets").find("small").text
            bibtex_link = article_li.find("nav", class_="publ").find_all("li", class_="drop-down")[1].find("div", class_="head").find("a")["href"]
            article = Article(title, authors, confname, pub_year, dblp_key, doi_link, bibtex_link)
            print_success("\t{}".format(article))
            articles.append(article)
        return articles

dblp = DBLP()
areas = ["Taint Analysis", "DNS Security", "PHP", "DNS", "DNS (Poison OR Spoof OR Inject)"]
area = "Taint Analysis"
for conf in Conferences:
    articles = dblp.search(area, conf)
    if len(articles) == 0:
        print_error("[{}] articles found".format(len(articles)))
    else:
        print_info("[{}] articles found".format(len(articles)))
    dblp.save(area, articles)