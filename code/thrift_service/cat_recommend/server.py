import thriftpy2
from thriftpy2.rpc import make_server
import joblib
import pandas as pd
import numpy as np
import redis

CatItem_thrift = thriftpy2.load("../../web/cat_item.thrift", module_name="CatItem_thrift")


# uid = 100

class Dispatcher(object):
    def items(self, uid: int):
        it = redis.StrictRedis(host='localhost', port=6379, db=0)
        model = joblib.load('../../training/model/SGDC.pkl')  # load model
        df = pd.DataFrame(it.keys(), columns=['news_id'])
        # df['news_id'] = df['news_id'].astype(str)
        df['news_id'] = df['news_id'].map(lambda x: x.decode()).map(lambda x: x.lstrip('N'))
        df = df.sample(n=1000)
        df.reset_index(inplace=True, drop=True)
        df['user_id'] = uid
        df['score'] = model.predict(df)
        del df['user_id']
        df.sort_values(by='score', inplace=True)
        print(df.head())

        Items = CatItem_thrift.Items()
        topK = 5

        iid = []
        title = []
        category = []
        abstract = []
        author = []
        date = []
        content = []
        image = []
        path = "../../web/static/news_data/"
        # iid = []
        for k in range(topK):
            news_detail = it.hmget('N' + str(df['news_id'][k]), ['id', 'category', 'title', 'abstract'])


            if news_detail[0]:
                news_detail = list(x.decode() for x in news_detail)
                news_id = news_detail[0]
                iid.append(news_id)
                title.append(news_detail[2])
                category.append(news_detail[1])
                abstract.append(news_detail[3])
                with open(path + "news_author/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
                    data = f.read()
                    data = data.split('\t')
                    author.append(data[0])
                    date.append(data[1])
                with open(path + "news/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
                    content.append(f.read())
                image.append("./static/news_data/" + "news_img/" + news_id + ".jpg")

        Items.iid = iid
        Items.title = title
        Items.category = category
        Items.abs = abstract
        Items.author = author
        Items.date = date
        Items.content = content
        Items.image = image
        return Items


server = make_server(CatItem_thrift.CatItemService, Dispatcher(), '127.0.0.1', 6001)
server.serve()
