import requests  # htlm 코드를 가져오기 위한 모듈
import json # json import하기
from bs4 import BeautifulSoup  # 웹 크롤링하기 위한 모듈

# 페이지 동적으로 최대한 늘어나는 수 (임의로 200이라고 함, 실제로 사이트에는 233)
PAGE = 200
# 해당 사이트가 아닌 원본 데이터를 동적으로 들고오는 url을 network에서 가지고 온 것
dynamic_page = 1
url = f"https://api.jumpit.co.kr/api/positions?page={dynamic_page}&sort=reg_dt&highlight=false"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.141 Whale/3.15.136.29 Safari/537.36",
    "referer": "https://www.jumpit.co.kr/positions"
}

# 동적 페이지 숫자 변경해주는 함수
def change_url_page(page):
    if page > PAGE:
        return "400" # 정보가 없는 페이지라는 것을 표시하기 위해 400을 반환
    else:
        global dynamic_page # 동적 페이지 번호 전역 변수로 선언
        dynamic_page = page + 1
        url_temp = "https://api.jumpit.co.kr/api/positions?page=" + str(dynamic_page) + "&sort=reg_dt&highlight=false"
        return url_temp

url = change_url_page(dynamic_page)

if url != "400":
    for page in range(PAGE):
        result = requests.get(url, headers=headers)
        result.raise_for_status()  # 정상적으로 접속이 되었는지 확인
        result.encoding = "utf8"

        stock_data = json.loads(result.text) # json 형태의 데이터 저장

        for data in stock_data['result']['positions']:
            for skill in data['techStacks']:
                print(skill)

        print("----- 동적 " + str(page + 1) + "페이지 끝 -----")


# with open("jumpit.json", "w", encoding="utf8") as f:
#     f.write(result.text)
#
# soup = BeautifulSoup(result.text, "lxml")  # lxml 라이브러리 설치 후 사용, lxml은 parser
