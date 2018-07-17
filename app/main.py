from flask import Flask, request, render_template, redirect

from models import Tweet
from tasks import post_tweets

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', tweets=Tweet.select())

    elif request.method == 'POST':
        tweet_text = request.form['text']
        if tweet_text:
            Tweet.create(text=tweet_text)
        return redirect('/')


@app.route("/post_tweets")
def telegram_post():
    post_tweets.delay()
    return 'Репостинг успешно запущен'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
