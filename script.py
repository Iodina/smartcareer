import mechanize
if __name__ == '__main__':
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-Agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")]
    content = br.open('https://www.linkedin.com/in/oleksandrsochka').read()
    print content