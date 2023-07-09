import json


def get_news(news_ids):
    details = []
    path = "static/news_data/"
    for news_id in news_ids:
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
            author = f.read()  # 读取文本
        # with open(path + "news/" + news_id + ".txt", "r", encoding='utf-8') as f:  # 打开文本
        #     data = f.read()  # 读取文本
        image = path + "news_img/" + news_id + ".jpg"
        detail = {
            'title': title,
            'category': category,
            'abstract': abstract,
            'author': author,
            'image': image
        }
        details.append(detail)
    return json.dumps(details)