from dotenv import load_dotenv
import os # os 조작에 쓰이는 python built-in function

# .env 파일을 열어주는 함수
load_dotenv()

open_ai_api_key = os.getenv("OPEN_AI_API_KEY")
print(open_ai_api_key)
