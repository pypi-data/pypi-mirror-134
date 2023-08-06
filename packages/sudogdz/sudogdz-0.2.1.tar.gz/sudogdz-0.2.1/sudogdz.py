"""
Parser of everything from the Russian reshebnik GDZ.RU
"""


__version__ = "0.2.1"


import bs4
import requests
import json


def __getUA():
    import random

    list = [{"percent": "13.4%", "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 Win10"},
            {"percent": "6.7%",
                "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "system": "Chrome 96.0 Win10"},
            {"percent": "6.3%",
                "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 Win10"},
            {"percent": "6.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 Win10"},
            {"percent": "5.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36", "system": "Chrome 96.0 Win10"},
            {"percent": "4.8%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36", "system": "Chrome 96.0 macOS"},
            {"percent": "3.3%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0", "system": "Firefox 91.0 Win10"},
            {"percent": "2.9%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15", "system": "Safari 15.1 macOS"},
            {"percent": "2.4%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36", "system": "Chrome 96.0 macOS"},
            {"percent": "2.2%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "system": "Chrome 96.0 macOS"},
            {"percent": "1.9%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 Linux"},
            {"percent": "1.8%",
            "useragent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 Linux"},
            {"percent": "1.8%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 Linux"},
            {"percent": "1.6%",
            "useragent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 Linux"},
            {"percent": "1.6%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 macOS"},
            {"percent": "1.6%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 Linux"},
            {"percent": "1.6%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 macOS"},
            {"percent": "1.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "system": "Chrome 95.0 Win10"},
            {"percent": "1.1%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "system": "Chrome 95.0 macOS"},
            {"percent": "0.9%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43", "system": "Edge 96.0 Win10"},
            {"percent": "0.9%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34", "system": "Edge 96.0 Win10"},
            {"percent": "0.6%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "system": "Firefox 78.0 Linux"},
            {"percent": "0.6%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60", "system": "Opera 81 Win10"},
            {"percent": "0.6%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 macOS"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36", "system": "Chrome 96.0 Linux"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15", "system": "Safari 15.0 macOS"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15", "system": "Safari 15.2 macOS"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62", "system": "Edge 96.0 Win10"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15", "system": "Safari 14.1 macOS"},
            {"percent": "0.5%",
            "useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 Win7"},
            {"percent": "0.4%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53", "system": "Edge 96.0 Win10"},
            {"percent": "0.4%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "system": "Firefox 91.0 Win10"},
            {"percent": "0.4%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "system": "Chrome 96.0 Linux"},
            {"percent": "0.4%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57", "system": "Edge 96.0 Win10"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41", "system": "Edge 96.0 Win10"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 Linux"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "system": "Chrome 95.0 Linux"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61", "system": "Opera 81 Win10"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29", "system": "Edge 96.0 Win10"},
            {"percent": "0.3%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23", "system": "Opera 82 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0", "system": "Firefox 96.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15", "system": "Safari 15.1 macOS"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0", "system": "Firefox 94.0 Win7"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0", "system": "Firefox 78.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36", "system": "Chrome 96.0 Win7"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 Win7"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "system": "Firefox 91.0 Linux"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "system": "Chrome 95.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0", "system": "Firefox 93.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0", "system": "Firefox 95.0 Linux"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 Win8.1"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", "system": "Chrome 92.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "system": "Chrome 96.0 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "system": "Chrome 96.0 Win7"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (X11; CrOS x86_64 14150.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.124 Safari/537.36", "system": "Chrome 94.0 ChromeOS"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36", "system": "Chrome 96.0 macOS"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "system": "Chrome 95.0 macOS"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33", "system": "Opera 82 Win10"},
            {"percent": "0.2%",
            "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0", "system": "Firefox 93.0 Linux"},
            {"percent": "0.2%", "useragent": "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0", "system": "Firefox 93.0 Linux"}]

    UACount = len(list)
    return list[random.randint(0, UACount)]

def getSchoolItems():
    """
    ### Allows you to get avaliable school subjects

    Subject name parsed from GDZ site, so run command and find your subject
    """
    # List
    schoolItemsList = []

    # UA
    useragent = __getUA()

    getGdzPage = requests.get("https://gdz.ru/", headers={'User-Agent': useragent['useragent']}).text
    wrappedPage = bs4.BeautifulSoup(getGdzPage, 'html.parser')

    for schoolitem in wrappedPage.find_all('td', attrs={"class": "table-section-heading"}):
        ejectedUrl = schoolitem.find('a').get('href')
        schoolItemsList.append(str(ejectedUrl).replace('/', ''))

    try:
        schoolItemsList.pop(0)
    except IndexError:
        raise requests.ConnectionError

    return schoolItemsList


def getBooks(type, **args):
    # Lists
    bookList = []
    ErrorList = [
        "school item is null",
        "number is greater than 11 or null"
    ]

    # UA
    useragent = __getUA()

    if (type == 'books'):
        if (int(args.get("schoolclass")) <= 11):
            if ('schoolitem' in args):
                getGdzPage = requests.get(f'https://gdz.ru/class-{args["schoolclass"]}/{args["schoolitem"]}', headers={'User-Agent': useragent['useragent']}).text
            else:
                raise ValueError(ErrorList[0])
        else:
            raise ValueError(ErrorList[1])
    elif (type == 'booksByClass'):
        if ('schoolclass' in args and int(args.get("schoolclass")) <= 11):
            getGdzPage = requests.get(f'https://gdz.ru/class-{args["schoolclass"]}', headers={'User-Agent': useragent['useragent']}).text
        else:
            raise ValueError(ErrorList[1])
    elif (type == 'booksBySchoolItem'):
        if ('schoolitem' in args):
            getGdzPage = requests.get(f'https://gdz.ru/{args["schoolitem"]}', headers={'User-Agent': useragent['useragent']}).text
        else:
            raise ValueError(ErrorList[0])
    elif (type == 'popularBooks'):
        getGdzPage = requests.get(f'https://gdz.ru', headers={'User-Agent': useragent['useragent']}).text
    else:
        return []
    wrappedPage = bs4.BeautifulSoup(getGdzPage, 'html.parser')
    for ul in wrappedPage.find_all(attrs={"class": "book-list"}):
        for li in ul.find_all("a", attrs={"class": ["book", "book-regular"]}):
            bookList.append({
                "url": {
                    "with_domain": f"https://gdz.ru{li['href']}",
                    "without_domain": li['href']
                },
                "name": str(li['title']).replace('ГДЗ ', '').strip(),
                "authors": str(li.find('span', attrs={"itemprop": "author"}).string).split(','),
                "pubhouse": str(li.find('span', attrs={"itemprop": "publisher"}).string).strip(),
                "cover": "https:" + li.find("div", attrs={"class": "book-cover"}).select('noscript>img')[0]['src'],
            })                
    return bookList

    
def getTasksForBook(url):
    # UA
    useragent = __getUA()

    if (str(url).startswith('https://gdz.ru') or str(url).startswith('http://gdz.ru')):
        getGdzPage = requests.get(url, headers={'User-Agent': useragent['useragent']}).text
    else:
        getGdzPage = requests.get(f"https://gdz.ru{url}", headers={'User-Agent': useragent['useragent']}).text

    wrappedPage = bs4.BeautifulSoup(getGdzPage, 'html.parser')

    tasksArray = []

    for taskItem in wrappedPage.find_all('a', attrs={'class': 'task-button js-task-button'}):
        try:
            categoryName = str(taskItem.parent.parent.find('h2', {"class": "heading"}).text).strip()
        except AttributeError:
            categoryName = str(taskItem.parent.parent.find('h3', {"class": "heading"}).text).strip()
        tasksArray.append({
            "num": str(taskItem.text).strip(),
            "category": categoryName,
            "url": {
                "with_domain": f"https://gdz.ru{taskItem['href']}",
                "without_domain": taskItem['href']
            }
        })

    return tasksArray


def getAnswerForBook(url):
    useragent = __getUA()

    if (str(url).startswith('https://gdz.ru') or str(url).startswith('http://gdz.ru')):
        getGdzPage = requests.get(url, headers={'User-Agent': useragent['useragent']}).text
    else:
        getGdzPage = requests.get(f"https://gdz.ru{url}", headers={'User-Agent': useragent['useragent']}).text
        
    wrappedPage = bs4.BeautifulSoup(getGdzPage, 'html.parser')

    answerArray = []

    for index, answerItem in enumerate(wrappedPage.find_all('div', attrs={'class': 'task-img-container'})):
        answerArray.append({
            "id": index,
            "title": str(answerItem.find('div', attrs={'class': 'with-overtask'}).select('img')[0]['alt']).strip(),
            "png": str("https:" + answerItem.find('div', attrs={'class': 'with-overtask'}).select('img')[0]['src']).strip()
        })

    return answerArray