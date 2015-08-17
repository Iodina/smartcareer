# coding=utf-8
__author__ = 'Artemko'

import urllib2
from parse_skills_profs import *
import time

base_url = "https://uk.linkedin.com/directory/people"

# Меняете здесь имя файла
file_profs_skills = open("profs_skills_b_1440.txt", "w")
# Меняете здесь букву алфавита
soup_content = BeautifulSoup(urllib2.urlopen(base_url + "-" + "b").read())


counter = 0
for link in soup_content.findAll("li", attrs={"class": "content"}):
    soup_link = BeautifulSoup(urllib2.urlopen(link.a["href"]).read())
    for link_1 in soup_link.findAll("li", attrs={"class": "content"}):
        soup_link_1 = BeautifulSoup(urllib2.urlopen(link_1.a["href"]).read())
        for link_11 in soup_link_1.findAll("li", attrs={"class": "content"}):
            time.sleep(1)
            # Можете поменять здесь количество людей, которое собираетесь парсить
            if counter > 1440:
                file_profs_skills.close()
                exit(0)
            counter += 1
            try:
                crawler = Crawler(link_11.a["href"])
                file_profs_skills.write(str(counter) + " | " + link_11.a["href"] + " | " +
                                        str(crawler.get_profs()) + " | " +
                                        str(crawler.get_skills()) + "\n")
            except Exception, e:
                print str(counter) + " | " + link_11.a["href"] + " | " + e.message

file_profs_skills.close()

