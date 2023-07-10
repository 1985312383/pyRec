from read_data import read_data
import pandas as pd
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, mean_squared_error, accuracy_score


def data_preprocess(mode):
    behaviors = read_data(mode=mode, dataset='behaviors')
    behaviors['time1'] = behaviors['time'].apply(
        lambda x: time.mktime(time.strptime(x, '%m/%d/%Y %H:%M:%S %p'))).astype('int64')
    behaviors['time2'] = behaviors['time'].str[-2:]

    # impressions = train_behaviors['impressions']
    behaviors = behaviors[['user_id', 'time1', 'time2', 'impressions']]
    behaviors['user_id'] = behaviors['user_id'].map(lambda x: x.lstrip('U'))

    behaviors['time_AM'] = behaviors['time2'].apply(lambda x: 1 if x == 'AM' else 0).astype('int32')
    behaviors['time_PM'] = behaviors['time2'].apply(lambda x: 1 if x == 'PM' else 0).astype('int32')
    behaviors = behaviors[['user_id', 'time1', 'time_AM', 'time_PM', 'impressions']]
    behaviors = behaviors['impressions'].str.split(' ', expand=True).stack().reset_index(level=0).set_index(
        'level_0').rename(columns={0: 'impressions'}).join(behaviors.drop('impressions', axis=1))
    behaviors['impressions'] = behaviors['impressions'].map(lambda x: x.lstrip('N'))
    if mode == 'train' or mode == 'val':
        behaviors['impressions'], behaviors['lables'] = behaviors['impressions'].str.split('-').str
        behaviors['lables'] = behaviors['lables'].astype('int32')
    # train_behaviors = pd.get_dummies(train_behaviors)
    return behaviors


train_data = data_preprocess('train')
lr = LogisticRegression()
lr.fit(train_data.iloc[:, :-1], train_data.iloc[:, -1])

val_data = data_preprocess('val')
lr_pred = lr.predict(val_data.iloc[:, :-1])
print("ROC", roc_auc_score(val_data.iloc[:, -1], lr_pred))
print("acc", accuracy_score(val_data.iloc[:, -1], lr_pred))
print("MSE", mean_squared_error(val_data.iloc[:, -1], lr_pred))
