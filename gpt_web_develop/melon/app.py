from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def home():
    url = "https://www.melon.com/chart/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs = soup.select('.lst50')
    trs50 = soup.select('.lst100')
    answer=[]
    for i, tr in enumerate(trs):
        image = tr.select_one('img')['src']
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        answer.append({"image":image, "title":title, "artist":artist})
    for i, tr in enumerate(trs50):
        image = tr.select_one('img')['src']
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        answer.append({"image":image, "title":title, "artist":artist})
    print(answer)
    return render_template('index.html', data=answer)

if __name__ == "__main__":
    app.run(debug=True)