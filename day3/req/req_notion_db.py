import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_API_KEY')
NOTION_DB = os.getenv('DATABASE_ID')

if not NOTION_TOKEN or not NOTION_DB :
    raise ValueError('.env 값 없엉 oTL')

url = f"https://api.notion.com/v1/databases/{NOTION_DB}/query"

# 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

try : 
    # 요청 전송(POST)
    response = requests.post(url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()
    page_list = data.get("results", [])

    for page in page_list:
        props = page.get("properties")

        # 이름 가져오기 (title 속성 값 가져오기)
        title_list = props.get("상품명", {}).get("title", [])
        title = title_list[0].get("plain_text") if title_list else None

        qty = props.get("재고 수량", {}).get("number", 0)
        #금액
        price = props.get("금액", {}).get("number", 0)
        #총금액
        total_price = props.get("총 금액",{}).get("formula", {}).get("number", 0)
        print(f"상품명: {title} | 수량: {qty} | 금액: {price:,} | 총금액: {total_price}")


except Exception as e:
    print(e)
