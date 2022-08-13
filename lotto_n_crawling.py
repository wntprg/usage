import requests
from bs4 import BeautifulSoup

# html_check
def html_check(text):
  f = open("C:/Users/Jeongmin/Desktop/round_lotto_number.txt", 'w')
  f.write(str(text))
  f.close()


# lotto_number_get
def lotto_n_get(count):
    global lotto_number
    global wnt_url

    # round_change
    for c in range(1026,count,1):
        # url_html_get
        data = {'drwNo': c, 'dwrNoList': c}
        res = requests.post(wnt_url, data=data)
        
        # lotto_object_parser
        soup = BeautifulSoup(res.text, 'html.parser')
        lotto_tags = soup.body.find("div", class_="num win").p.find_all('span')

        # lotto_number_parser
        for lotto_tag in lotto_tags:
            lotto_number.append(int(lotto_tag.string))

        # lotto_number_store
        lotto_number.append(int(soup.body.find("div", class_="num bonus").p.find('span').string))

# lotto_url
wnt_url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'

# lotto_number_storage
lotto_number = []

# lotto_number_get(round+1)
lotto_n_get(1028)
html_check(lotto_number)