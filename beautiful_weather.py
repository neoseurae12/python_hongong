# BeautifulSoup 모듈 => 날씨 가져오기

# 모듈 읽어들이기
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수 => 기상청의 전국 날씨 읽기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup => 웹 페이지 분석
soup = BeautifulSoup(target, "html.parser")

# location 태그 찾기
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그 찾기 -> 출력
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


'''
도시: 서울
날씨: 흐리고 비
최저기온: 24
최고기온: 29

도시: 인천
날씨: 흐리고 비
최저기온: 23
최고기온: 29

도시: 수원
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 파주
날씨: 흐리고 비
최저기온: 22
최고기온: 29

도시: 이천
날씨: 흐리고 비
최저기온: 22
최고기온: 30

도시: 평택
날씨: 흐리고 비
최저기온: 23
최고기온: 31

도시: 춘천
날씨: 흐리고 비
최저기온: 23
최고기온: 29

도시: 원주
날씨: 흐리고 비
최저기온: 22
최고기온: 29

도시: 강릉
날씨: 흐리고 비
최저기온: 23
최고기온: 28

도시: 대전
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 세종
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 홍성
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 청주
날씨: 흐리고 비
최저기온: 24
최고기온: 31

도시: 충주
날씨: 흐리고 비
최저기온: 22
최고기온: 30

도시: 영동
날씨: 흐리고 비
최저기온: 22
최고기온: 31

도시: 광주
날씨: 흐리고 비
최저기온: 24
최고기온: 31

도시: 목포
날씨: 흐리고 비
최저기온: 25
최고기온: 29

도시: 여수
날씨: 흐리고 비
최저기온: 24
최고기온: 29

도시: 순천
날씨: 흐리고 비
최저기온: 25
최고기온: 31

도시: 광양
날씨: 흐리고 비
최저기온: 24
최고기온: 31

도시: 나주
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 전주
날씨: 흐리고 비
최저기온: 24
최고기온: 31

도시: 군산
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 정읍
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 남원
날씨: 흐리고 비
최저기온: 23
최고기온: 31

도시: 고창
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 무주
날씨: 흐리고 비
최저기온: 21
최고기온: 30

도시: 부산
날씨: 흐리고 비
최저기온: 24
최고기온: 29

도시: 울산
날씨: 흐리고 비
최저기온: 23
최고기온: 29

도시: 창원
날씨: 흐리고 비
최저기온: 23
최고기온: 31

도시: 진주
날씨: 흐리고 비
최저기온: 23
최고기온: 30

도시: 거창
날씨: 흐리고 비
최저기온: 21
최고기온: 30

도시: 통영
날씨: 흐리고 비
최저기온: 23
최고기온: 29

도시: 대구
날씨: 흐리고 비
최저기온: 23
최고기온: 31

도시: 안동
날씨: 흐리고 비
최저기온: 22
최고기온: 30

도시: 포항
날씨: 흐리고 비
최저기온: 23
최고기온: 29

도시: 경주
날씨: 흐리고 비
최저기온: 22
최고기온: 30

도시: 울진
날씨: 흐리고 비
최저기온: 21
최고기온: 26

도시: 울릉도
날씨: 흐리고 비
최저기온: 22
최고기온: 26

도시: 제주
날씨: 흐리고 비
최저기온: 27
최고기온: 31

도시: 서귀포
날씨: 흐리고 비
최저기온: 25
최고기온: 30

'''