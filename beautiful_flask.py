# BeautifulSoup 스크레이핑

# 모듈 읽어들이기
from flask import Flask
from bs4 import BeautifulSoup
from urllib import request

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수 => 기상청의 전국 날씨 읽기
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup => 웹 페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 찾기
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그 찾기 -> 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최고/최저 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"

    return output

app.run()