#!/usr/bin/env python3

import requests

from selectolax.parser import HTMLParser


def extract(url):
    """Get raw HTLM text from a page."""
    resp = requests.get(url)
    return resp.text

def parse(html):
    """Process HTML and get the title."""
    html = HTMLParser(html)
    elements = html.css("title")
    for i in elements:
        return i.text()

def match_titles(num, lst_urls):
    """Compare titles and alarm on mismatches."""
    titles = set()
    page_404 = "Страница не существует"

    for url in lst_urls:
        html = extract(url)
        title = parse(html)
        titles.add(title)
        if page_404 in titles:
            print(f"Error in line {num}")
            print(f"Page not found:\n{titles=}")
            break
        elif len(titles) > 1:
            print(f"Error in line {num}")
            print(f"Mismatched titles:")
            [print(title) for title in titles]
            break



def main():
    """Check input file line by line and compare titles."""
    with open("example.txt") as file:
        for num, line in enumerate(file, 1):
            lst_urls = line.replace("\n", "").rsplit(",")
            # no need to check less than 2 links
            if len(lst_urls) < 2:
                print(f"Less than 2 links in line {num}")
                print(f"Error in {lst=}")
            else:
                match_titles(num, lst_urls)

if __name__ == "__main__":
    main()
