## 한국어 자연어 처리 예제 패키지

* samsung_report
  + stopwords를 이용해서 불필요한 단어들 제거
  + WordCloud 를 이용하여 빈도수 높은 단어들을 보여줌

* naver_movie
  + 네이버에서 영화를 랭크별 크롤링 (크롬 드라이버 사용)
  + 순위별로 dictionary 형태로 담아 csv 파일로 저장 

* tweet
  + 트위터 보안으로 인해 예제 진행 도중 중단

#### konlpy 사용
```
JPype1-1.3.0-cp38-cp38-win_amd64.whl   # 다운 및 설치
python -m pip install --user --upgrade pip
pip install JPype1-1.3.0-cp38-cp38-win_amd64.whl
pip install -U "jpype1<1.1"
pip install konlpy
pip install tweepy==3.10.0  # 버전 오류인 경우 선택적으로 실행!
```
#### corpora 말뭉치 다운
```
import nltk
nltk.download()
```