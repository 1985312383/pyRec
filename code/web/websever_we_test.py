from flask import Flask, escape, url_for, render_template, send_from_directory
import os
# import get_data
import pandas as pd

app = Flask(__name__)





@app.route('/')
def index():
    # news_ids = ['N1']
    # for news_id in news_ids:
    news_ids = ['N1', 'N2']
    # news_details = get_data.get_news(news_ids)
    news_details = [
        {"title": "Texans defensive tackle D.J. Reader is taking advantage of his opportunities", "category": "sports",
         "abstract": "Houston Texans defensive tackle D.J. Reader is taking advantage of opportunities given by defensive end J.J. Watt.\n",
         "author": "Avery Duncan\t10/17/2019\n", "image": "static/news_data/news_img/N1.jpg"},
        {"title": "Mormons to the Rescue?", "category": "news",
         "abstract": "The one religious faith that is the most heavily Republican is somewhat disgusted with Trump. Barely half the members of the American-grown Church of Jesus Christ of Latter-day Saints approve of his presidency.\n",
         "author": "Timothy Egan\t10/12/2019\n", "image": "static/news_data/news_img/N2.jpg"}]

    data = news_details
    # data = [
    #     {
    #         'title': 'pang pang yuanyuan',
    #         'category': 'sport',
    #         'abstract': 'pang pang yuanyuan xxxx',
    #         'author': 'xiaoran',
    #         'image': '../data/pang_yuan.jpg'
    #     },
    #     {
    #         'title': 'pang pang yuanyuan 22',
    #         'category': 'sport 2',
    #         'abstract': 'pang pang yuanyuan xxxx 222',
    #         'author': 'xiaoran-2',
    #         'image': '../data/pang_yuan_2.jpg'
    #     },
    # ]
    return render_template('index.html', data=data)


@app.route('/login')
def login():
    return 'login'


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# 运行命令
# set FLASK_APP=code/web/websever_we_test.py
# flask run

if __name__ == '__main__':
    news_ids = ['N1', 'N2']
    news_details = get_news(news_ids)
    print(news_details)
