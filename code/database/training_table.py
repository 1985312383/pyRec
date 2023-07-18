import pickle

import pandas as pd
import redis
from tqdm import tqdm

tt = redis.StrictRedis(host='localhost', port=6379, db=2)

df = pd.read_table('../training/datasets/train/behaviors.tsv',
                   header=None,
                   names=['impression_id', 'user_id', 'time', 'history', 'impressions'],
                   chunksize=10000)

index = 0
for users in tqdm(df):
    tt.set("users" + str(index), pickle.dumps(users))
    index += 1
