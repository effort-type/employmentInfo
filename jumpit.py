import requests  # htlm 코드를 가져오기 위한 모듈
from bs4 import BeautifulSoup  # 웹 크롤링하기 위한 모듈

url = "https://www.jumpit.co.kr/positions"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.141 Whale/3.15.136.29 Safari/537.36"}

result = requests.get(url, headers=headers)
result.raise_for_status() # 정상적으로 접속이 되었는지 확인
result.encoding = "utf8"

with open("jumpit.html", "w", encoding="utf8") as f:
    f.write(result.text)

soup = BeautifulSoup(result.text, "lxml") # lxml 라이브러리 설치 후 사용, lxml은 parser

