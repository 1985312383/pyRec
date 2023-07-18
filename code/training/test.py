import thriftpy2
from thriftpy2.rpc import make_client
user_i = 100
CatItem_thrift = thriftpy2.load("../web/cat_item.thrift", module_name="CatItem_thrift")
client = make_client(CatItem_thrift.CatItemService, '127.0.0.1', 6001)
news_details = client.items(user_i)
datas = []
for i in range(len(news_details.title)):
    data = {
        'title': news_details.title[i],
        'category': news_details.category[i],
        'abstract': news_details.abs[i],
        'author': news_details.author[i],
        'date': news_details.date[i],
        'id': news_details.iid[i],
        'content': news_details.content[i],
        'image': news_details.image[i],
    },
    datas.append(data)