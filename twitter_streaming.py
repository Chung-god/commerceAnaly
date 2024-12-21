import tweepy
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# API 키와 토큰
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# Tweepy 인증
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 사용자 정보 확인
user = api.verify_credentials()
print(f"Authenticated as: {user.name}")
