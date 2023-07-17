import redis
import pandas as pd
from tqdm import tqdm

df = pd.read_table('../training/datasets/train/behaviors.tsv',
                   header=None,
                   names=['impression_id', 'user_id', 'time', 'history', 'impressions'])
df = df[['user_id', 'time', 'history']]
it = redis.StrictRedis(host='localhost', port=6379, db=1)

for index, user in tqdm(df.iterrows(), total=df.shape[0]):
    it.hmset(user['user_id'], user.to_dict())
