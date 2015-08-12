from bs4 import BeautifulSoup
import urllib
import mechanize

professions = {
  "Java developer": ["Java", "Algorithms", "Probability theory", "JVM"],
  "Database Administrator": ["Databases", "Logical thinking", "Probability theory"], 
  "Project manager": ["Algorithms", "Leadership"],
  "Back-end developer": ["PHP", "JavaScript", "Python", "Node.js"],
  "Front-end developer": ["CSS", "HTML", "JavaScript"],
  "Web-designer": ["Photoshop", "CSS", "Paint", "HTML"],
  "IOS developer": ["Algorithms", "Swift", "Objective-C"],
  "C# developer": ["C#", "Algorithms", "Probability theory", "ASP.NET"],
  "Android developer": ["Java", "XML", "Android"],
  "Embedded developer": ["C", "Embedded", "Linux"],
}

# link_name = "https://www.linkedin.com/in/oleksandrsochka"

class Crawler:
    def __init__(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-Agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")]

        self._br = br

    def get_skills(self, url):
        content = self._br.open(url).read()
        return map(lambda x: x.text.encode('utf-8'),
                BeautifulSoup(content, 'html.parser').find_all('a', 'endorse-item-name-text'))

def get_profession(skills):
    def match(prof_skills):
        count = 0
        for skill in skills:
            for prof_skill in prof_skills:
                if skill.lower() == prof_skill.lower():
                    count += 1
        return float(count) / len(prof_skills)

    return { profession: match(prof_skills) for profession, prof_skills in professions.items()}

def sort_skills(d):
    return sorted(d, key=d.get, reverse=True)

if __name__ == '__main__':
    crawler = Crawler()
    print sort_skills(get_profession(crawler.get_skills(link_name)))[:3]
 #   print sort_skills(get_profession(crawler.get_skills("https://ua.linkedin.com/in/alexeyshmalko")))[:3]
