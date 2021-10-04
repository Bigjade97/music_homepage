import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music_homepage.settings")
import django
django.setup()
# ## BlogData를 import해옵니다
from member.models import New_Album

def name_adjective():
  header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
  req = requests.get('https://www.melon.com/new/album/index.htm#params%5BareaFlg%5D=O&params%5BorderBy%5D=&po=pageObj&startIndex=1', headers = header) ## 주간 차트를 크롤링 할 것임
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  adjective_album = soup.select(
    '#frm > div > ul > li > div.entry > div.info > a'
  )
  adjective_singer = soup.select(
    '#frm > div > ul > li > div.entry > div.info > span.ellipsis.artist > a'
  )
  adjective_date = soup.select(
    '#frm > div > ul > li > div.entry > div.meta > span.reg_date'
  )
  adjective_kind = soup.select(
    '#frm > div > ul > li > div.entry > div.info > span.vdo_name'
  )
  adjective_many = soup.select(
    '#frm > div > ul > li > div.entry > div.meta > span.tot_song'
  )
  adjective_list = []

  for i in range(len(adjective_album)):
    adjective_list2 = []
    for k in range(1):
      adjective_list2.append(adjective_album[i].text.strip())
      adjective_list2.append(adjective_singer[i].text.strip())
      adjective_list2.append(adjective_date[i].text.strip())
      adjective_list2.append(adjective_kind[i].text.strip())
      adjective_list2.append(adjective_many[i].text.strip())
    adjective_list.append(adjective_list2)
  return adjective_list

if __name__=='__main__':
    blog_data_dict = name_adjective()
    print(blog_data_dict)
    for i in range(len(blog_data_dict)):
      New_Album(album = blog_data_dict[i][0], singer = blog_data_dict[i][1], date = blog_data_dict[i][2], kind = blog_data_dict[i][3], many = blog_data_dict[i][4]).save()

    