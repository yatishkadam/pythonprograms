import requests
from bs4 import BeautifulSoup
import time
import re

# declaration of all the lists used as global variables
main_links, visited_links, depth1, depth2, depth3, depth4, depth5 = [], [], [], [], [], [], []


def crawler(url):
    a, b = [], []
    visited_links.append(url)

    time.sleep(1)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    data = soup.find('div', {'class': 'mw-body-content'})
    if len(soup.find('ol', class_='references') or ()) > 1:
        soup.find('ol', class_='references').decompose()
    for link in data.find_all('a',):
        if ':' not in link.get('href'):
            href = "https://en.wikipedia.org" + link.get('href')
            hlist = href.split('#')
            a.append(str(hlist[0]))

    for i in a:
        if i not in b:
            if len(i) > 1:
                if i not in visited_links:
                    b.append(i)

    for i in b:
        if i not in main_links:
            main_links.append(i)

    return b


def next_link(list):
    for i in list:
        if i not in visited_links:
            return i
    if list == depth1:
        if len(depth1) < 1000:
            return next_link(depth2)
    if list == depth2:
        if len(depth2) < 1000:
            return next_link(depth3)
    if list == depth3:
        if len(depth3) < 1000:
            return next_link(depth4)
    if list == depth4:
        if len(depth4) < 1000:
            return next_link(depth5)
    return "No more links"


def write_to_file():
    numbering = 1
    file = open('task1.txt', 'w+')
    for link in main_links[0:1000]:
        row = str(numbering) + " " + str(link) + "\n"
        file.write(row)
        numbering += 1
    file.close()


def main_crawler(seed):
    depth1.append(seed)
    main_links.append(seed)

    while len(main_links) < 1000:

        page_url = next_link(depth1)

        if page_url == "No more links":
            print "No more links to crawl"
            break
        else:
            if page_url in depth1:
                depth1_urls = crawler(page_url)
                for link in depth1_urls:
                    depth2.append(link)
            elif page_url in depth2:
                depth2_urls = crawler(page_url)
                for link in depth2_urls:
                    if (link not in depth1) and (link not in depth2):
                        depth3.append(link)
            elif page_url in depth3:
                depth3_urls = crawler(page_url)
                for link in depth3_urls:
                    if (link not in depth2) and (link not in depth3):
                        depth4.append(link)
            elif page_url in depth4:
                depth4_urls = crawler(page_url)
                for link in depth4_urls:
                    if (link not in depth3) and (link not in depth4):
                        depth5.append(link)
    write_to_file()


main_crawler("https://en.wikipedia.org/wiki/Sustainable_energy")