import redis
import pandas as pd
from tqdm import tqdm

df = pd.read_table('../training/datasets/train/news.tsv',
                   header=None,
                   names=[
                       'id', 'category', 'subcategory', 'title', 'abstract', 'url',
                       'title_entities', 'abstract_entities'
                   ])

it = redis.StrictRedis(host='localhost', port=6379, db=0)

for index, news in tqdm(df.iterrows(), total=df.shape[0]):
    it.hmset(news['id'], news.to_dict())
