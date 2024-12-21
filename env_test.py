from dotenv import load_dotenv
import tweepy
import os


# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 가져오기
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# 확인: 변수 출력
print(API_KEY)  # 정상적으로 로드되었는지 확인


# Twitter API 인증
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# API 객체 생성
api = tweepy.API(auth)

# 인증 테스트: 내 계정 정보 가져오기
try:
    user = api.verify_credentials()
    print("Authentication successful!")
    print(f"Logged in as: {user.screen_name}")
except Exception as e:
    print("Authentication failed:", e)
