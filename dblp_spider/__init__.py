import os
import requests
import termcolor
import glob
import argparse

from .core.article import Article
from .core.conference import Conferences
from .core.conference import Conferences_CCF_A
from .core.conference import Conferences_CCF_B
from .core.conference import Conferences_CCF_C
from bs4 import BeautifulSoup

__version__ = "0.0.2"


def print_success(x): return termcolor.cprint(x, 'green')
def print_error(x): return termcolor.cprint(x, 'red')
def print_warning(x): return termcolor.cprint(x, 'yellow')
def print_info(x): return termcolor.cprint(x)


def legalise_filename(filename):
    illegal_chars = {
        "|": "OR",
        "/": "-",
        "(": "[",
        ")": "]",
    }
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
        print_info(
            "[*] Searching {} on {}".format(termcolor.colored(area, "cyan"), conf))
        params = {
            "q": keyword,
            "h": 100,
            "f": 0,
            "s": "ydvspc",
        }
        url = "http://dblp.uni-trier.de/search/publ/inc"

        response = requests.get(url, params=params)
        content = response.text
        articles = self.parse(content)
        return articles

    def save(self, base_folder, area, conf, articles):
        folder = os.path.join(base_folder, legalise_filename(
            area), legalise_filename(conf.short))
        if len(articles) > 0:
            try:
                os.makedirs(folder)
            except:
                pass
        for article in articles:
            print("\t{}".format(termcolor.colored(article, "green")), end="")
            filename = legalise_filename("{}.bib".format(article.dblp_key))
            filepath = os.path.join(folder, filename)
            if not os.path.exists(filepath):
                with open(filepath, "w") as f:
                    f.write(article.get_bibtex())
            print(" {} {}".format(termcolor.colored("=>", "yellow"),
                                  termcolor.colored(filepath, "cyan")))

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
            confname = article_li.find("span", itemprop="isPartOf").find(
                "span", itemprop="name").text
            pub_year = article_li.find("span", itemprop="datePublished").text
            dblp_key = article_li.find(
                "ul", class_="bullets").find("small").text
            bibtex_link = article_li.find("nav", class_="publ").find_all(
                "li", class_="drop-down")[1].find("div", class_="head").find("a")["href"]
            article = Article(title, authors, confname,
                              pub_year, dblp_key, doi_link, bibtex_link)
            articles.append(article)
        return articles


def summary(base_folder, area):
    # Save summary bibtex
    folder = os.path.join(base_folder, legalise_filename(area))
    bibtexes = glob.glob(os.path.join(folder, "**", "*.bib"))
    bibtexes_contents = []
    for bibtex in bibtexes:
        with open(bibtex, "r") as f:
            bibtexes_contents.append(f.read())
    with open(os.path.join(folder, "summary.bib"), "w") as f:
        f.write("\n".join(bibtexes_contents))


def main():

    parser = argparse.ArgumentParser(description='DBLP BibTeX Spider')
    parser.add_argument('--keywords', required=True, nargs='+', help='DBLP searching keywords')

    parser.add_argument('--ccf-a', required=False, help='Search in CCF A recommandation venues', action="store_true")
    parser.add_argument('--ccf-b', required=False, help='Search in CCF B recommandation venues', action="store_true")
    parser.add_argument('--ccf-c', required=False, help='Search in CCF C recommandation venues', action="store_true")

    parser.add_argument('--output', required=True, help='Output BibTeX folder')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()

    dblp = DBLP()

    venues = set()
    if (not args.ccf_a) and (not args.ccf_b) and (not args.ccf_c):
        venues = venues.union(Conferences)
    else:
        if args.ccf_a:
            venues = venues.union(Conferences_CCF_A)
        if args.ccf_b:
            venues = venues.union(Conferences_CCF_B)
        if args.ccf_c:
            venues = venues.union(Conferences_CCF_C)

    for area in args.keywords:
        for venue in venues:
            articles = dblp.search(area, venue)
            if len(articles) == 0:
                print_error("[{}] articles found".format(len(articles)))
            else:
                print_info("[{}] articles found".format(len(articles)))
            dblp.save(args.output, area, venue, articles)
        summary(args.output, area)

if __name__ == "__main__":
    main()
