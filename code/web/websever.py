# coding: utf-8
"""
# Author: Ran Xiao
# Email : xiaoranone@gmail.com
# File  : apps/app.py
# Date  : 2023/06/22
"""

from flask import Flask, redirect
from flask import render_template
from flask import request, jsonify
from flask import session

app = Flask(__name__)


@app.route('/')
def index():
    if 'refresh_count' not in session:
        session['refresh_count'] = 1
    else:
        session['refresh_count'] += 1
    print("xiaoran-cnt", session['refresh_count'])
    print("refresh_count", session['refresh_count'])

    # 1. 拿到前端get方法传过来的参数，user_id
    user_id = request.args.get('user_id')

    # 1.1 由于我们的用户来自数据日志，可以从全部的数据中随机抽取用户uid，并且生成req_id，传到下游
    uids, req_ids = select_batch_ui ds(session['refresh_count'], all_dev_uids, k=10)

    # print("user_ids", uids)
    # 2. 请求后端的服务，拿到返回的结果，这个服务后面搭建，可以先生成mock的数据
    # rec_client = RecommendClient()
    # answer_news = rec_client.predict_batch_user(uids, req_ids)
    # print("answer_news", answer_news)

    # 3. answer_news，需要包含[(news_id, score)], mock [('N37378', 0.1), ('N37348', 0.05), ]
    # 根据news id得到新闻的详细内容，如上图列表也所示
    news_client = NewsClient()
    news_details = news_client.get_news(answer_news)
    data = news_details
    # 4. 将得到的结果，返回到前端页面进行显示
    # data = [
    #   {
    #       'title': 'pang pang yuanyuan',
    #       'category': 'sport',
    #       'abstract': 'pang pang yuanyuan xxxx',
    #       'author': 'xiaoran',
    #       'image': '../data/pang_yuan.jpg'
    #   },
    #   {
    #       'title': 'pang pang yuanyuan 22',
    #       'category': 'sport 2',
    #       'abstract': 'pang pang yuanyuan xxxx 222',
    #       'author': 'xiaoran-2',
    #       'image': '../data/pang_yuan_2.jpg'
    #   },
    # ]
    return render_template('index.html', data=data)


@app.route('/news')
def news():
    news_id = request.args.get('news_id')
    print("xiaorna-news_id", news_id)
    print("news_id", news_id)
    news_client = NewsClient()
    news_details = news_client.get_news_detail(news_ids=news_id)
    data = news_details
    return render_template('news.html', data=data)


if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'cat_news_app'
    app.run("127.0.0.1", port=5005, debug=True)
