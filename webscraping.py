from bs4 import BeautifulSoup
import requests
import csv

# with open('simple.html') as file_html:
#    soup = BeautifulSoup(file_html,'lxml')
# print(soup.prettify())
# match=soup.title #match =soup.title.text
# match = soup.find('div',class_='footer')# find_all
# print(match)
# healine = article.h2.a.text
# summary = article.p.text
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# print(soup.prettify())
# article = soup.find('article')
# print(article.prettify())
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
# access like dictionary
    try:

        vid_src = article.find('iframe', class_='youtube-player')['src']
    # print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None
    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
