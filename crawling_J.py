import requests
from bs4 import BeautifulSoup


url = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin")
html_doc = url.text

# html_check
def check_html(check_url):
    f = open("C:/Users/Jeongmin/Desktop/python_learning_related/lotto_machine_learning/html.txt",'w')
    f.write(check_url)
    f.close()

soup = BeautifulSoup(html_doc,'html.parser')
test_p = soup.get_text()
check_html(test_p)