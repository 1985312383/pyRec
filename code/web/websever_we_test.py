from flask import Flask, escape, url_for, render_template, send_from_directory, request
import os
# import get_data
import pandas as pd
import json

app = Flask(__name__)


def get_news(news_ids):
    details = []
    for news_id in news_ids:
        path = "./code/web/static/news_data/"
        with open(path + "news_abstract/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
            data = f.read()  # 读取文本
            data = data.split('\t')
        # data = pd.read_csv(path + "news_abstract/" + news_id + ".txt", sep='\t')
        # print(data)
        category = data[0]
        title = data[2]
        try:
            abstract = data[3]
        except:
            abstract = ""
        with open(path + "news_author/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
            data = f.read()  # 读取文本
            data = data.split('\t')
            author = data[0]  # 读取文本
            date = data[1]
        # with open(path + "news/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
        #     data = f.read()  # 读取文本
        path = "./static/news_data/"
        image = path + "news_img/" + news_id + ".jpg"
        detail = {
            'title': title,
            'category': category,
            'abstract': abstract,
            'author': author,
            'image': image,
            'id': news_id
        }
        details.append(detail)
    return details


def get_news_details(news_id):
    path = "./code/web/static/news_data/"
    with open(path + "news_abstract/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
        data = f.read()  # 读取文本
        data = data.split('\t')
    # data = pd.read_csv(path + "news_abstract/" + news_id + ".txt", sep='\t')
    # print(data)
    category = data[0]
    title = data[2]
    try:
        abstract = data[3]
    except:
        abstract = ""
    with open(path + "news_author/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
        data = f.read()  # 读取文本
        data = data.split('\t')
        author = data[0]  # 读取文本
        date = data[1]
    with open(path + "news/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
        content = f.read()  # 读取文本
    path = "./static/news_data/"
    image = path + "news_img/" + news_id + ".jpg"
    detail = {
        'title': title,
        'category': category,
        'abstract': abstract,
        'author': author,
        'image': image,
        'id': news_id,
        'content': content,
        'date': date
    }
    return [detail]


@app.route('/')
def index():
    # news_ids = ['N1']
    # for news_id in news_ids:
    news_ids = ['N1', 'N2']
    news_details = get_news(news_ids)
    data = news_details
    return render_template('index.html', data=data)


@app.route('/news')
def news():
    news_id = request.args.get('news_id')
    print("xiaorna-news_id", news_id)
    print("news_id", news_id)
    # news_client = NewsClient()
    # news_details = news_client.get_news_detail(news_ids=news_id)
    news_details = get_news_details(news_id)
    data = news_details
    return render_template('news.html', data=data)

# @app.route('/login')
# def login():
#     return 'login'


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

# if __name__ == '__main__':
#     news_ids = ['N1', 'N2']
#     news_details = get_news(news_ids)
#     print(news_details)
