import pdb
from read_data import read_data
import pandas as pd
import time
from sklearn.linear_model import LogisticRegression

train_behaviors = read_data(mode='train', dataset='behaviors')
train_behaviors['time1'] = train_behaviors['time'].apply(
    lambda x: time.mktime(time.strptime(x, '%m/%d/%Y %H:%M:%S %p'))).astype('int64')
train_behaviors['time2'] = train_behaviors['time'].str[-2:]

# impressions = train_behaviors['impressions']
train_behaviors = train_behaviors[['user_id', 'time1', 'time2', 'impressions']]
train_behaviors['time_AM'] = train_behaviors['time2'].apply(lambda x: 1 if x == 'AM' else 0)
train_behaviors['time_PM'] = train_behaviors['time2'].apply(lambda x: 1 if x == 'PM' else 0)
train_behaviors = train_behaviors[['user_id', 'time1', 'time_AM', 'time_PM', 'impressions']]
pdb.set_trace()
train_behaviors = pd.get_dummies(train_behaviors)
pdb.set_trace()
