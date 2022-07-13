import requests  # htlm 코드를 가져오기 위한 모듈
import json  # json import하기

# 해당 사이트가 아닌 원본 데이터를 동적으로 들고오는 url을 network에서 가지고 온 것
dynamic_page = 0

base_url = "https://api.jumpit.co.kr/api/positions"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.141 Whale/3.15.136.29 Safari/537.36",
    "referer": "https://www.jumpit.co.kr/positions"
}


# 기술 json이 공백이 나올 때까지 루프
while True:
    dynamic_page = dynamic_page + 1
    url = base_url + f"?page={dynamic_page}"

    result = requests.get(url, headers=headers)
    result.raise_for_status()  # 정상적으로 접속이 되었는지 확인
    result.encoding = "utf8"

    stock_data = json.loads(result.text)  # json 형태의 데이터 저장

    # 기술 json이 빈칸인 경우
    if len(stock_data['result']['positions']) == 0:
        break

    for data in stock_data['result']['positions']:
        for skill in data['techStacks']:
            print(skill)

    print("----- 동적 " + str(dynamic_page + 1) + "페이지 끝 -----")
