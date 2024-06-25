from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def home():
    def generate_lotto_numbers():
        numbers = random.sample(range(1, 46), 6)
        return sorted(numbers)

    def common_lotto():
        return len(set(lotto) & set(lotto_numbers))

    name = '전민성'
    lotto = [16, 18, 22, 43, 32, 11]
    lotto_numbers = generate_lotto_numbers()
    common_numbers = common_lotto()

    context = {
        "name": name, "lotto": lotto, "lotto_numbers": lotto_numbers, "common_numbers": common_numbers
    }
    return render_template('index.html', data=context)


@app.route('/mypage')
def mypage():
    return 'This is MyPage!'


@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(
        f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route('/boxoffice')#숙제 경로
def boxoffice():
    ser = request.args.get('ser')
    print(ser)
    if ser is not None:
        res = requests.get(
            f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={ser}"
        )
        rjson = res.json()
        officelist = rjson["boxOfficeResult"]
        ans=0
    else:
        ans=1
        officelist=1
    context = {
        "officelist": officelist, 
        "defalt": ans,
    }
    return render_template('boxoffice.html', data=context)




if __name__ == '__main__':
    app.run(debug=True)