from read_data import read_data
import time
from sklearn.metrics import roc_auc_score, mean_squared_error, accuracy_score
from sklearn.linear_model import SGDClassifier
import joblib
import redis
import pandas as pd
from tqdm import tqdm
import pickle
import warnings

warnings.filterwarnings("ignore")


def data_preprocess(behaviors, mode):
    behaviors['time1'] = behaviors['time'].apply(
        lambda x: time.mktime(time.strptime(x, '%m/%d/%Y %H:%M:%S %p'))).astype('int64')
    behaviors['time2'] = behaviors['time'].str[-2:]

    # impressions = train_behaviors['impressions']
    behaviors = behaviors[['user_id', 'history', 'impressions']]
    behaviors['user_id'] = behaviors['user_id'].map(lambda x: x.lstrip('U'))
    #
    # behaviors['time_AM'] = behaviors['time2'].apply(lambda x: 1 if x == 'AM' else 0).astype('int32')
    # behaviors['time_PM'] = behaviors['time2'].apply(lambda x: 1 if x == 'PM' else 0).astype('int32')
    # behaviors = behaviors[['user_id', 'time1', 'time_AM', 'time_PM', 'impressions']]
    behaviors_1 = behaviors[['user_id', 'history']]
    behaviors_1 = behaviors_1['history'].str.split(' ', expand=True).stack().reset_index(level=0).set_index(
        'level_0').rename(columns={0: 'news_id'}).join(behaviors_1.drop('history', axis=1))
    behaviors_1['labels'] = 1
    behaviors_2 = behaviors[['user_id', 'impressions']]
    behaviors_2 = behaviors_2['impressions'].str.split(' ', expand=True).stack().reset_index(level=0).set_index(
        'level_0').rename(columns={0: 'news_id'}).join(behaviors_2.drop('impressions', axis=1))

    # if mode == 'train' or mode == 'val':
    behaviors_2['news_id'], behaviors_2['labels'] = behaviors_2['news_id'].str.split('-').str

    # train_behaviors = pd.get_dummies(train_behaviors)
    behaviors = pd.concat([behaviors_1, behaviors_2])
    behaviors['news_id'] = behaviors['news_id'].map(lambda x: x.lstrip('N'))

    behaviors['user_id'] = behaviors['user_id'].astype('int32')
    behaviors['news_id'] = behaviors['news_id'].astype('int32')
    behaviors['labels'] = behaviors['labels'].astype('int32')

    return behaviors


tt = redis.StrictRedis(host='localhost', port=6379, db=2)
SGDC = SGDClassifier()

for index in tqdm(range(tt.dbsize())):
    # for index in tqdm(range(10)):

    df_bytes_from_redis = tt.get("users" + str(index))
    df_from_redis = pickle.loads(df_bytes_from_redis)
    train_data = data_preprocess(df_from_redis, 'train')
    # print(sum(train_data.iloc[:, -1]))
    SGDC.partial_fit(train_data.iloc[:, :-1], train_data.iloc[:, -1], classes=[0, 1])

val_data = read_data('val', nrows=10000)
val_data = data_preprocess(val_data, 'val')
SGDC_pred = SGDC.predict(val_data.iloc[:, :-1])
print("ROC", roc_auc_score(val_data.iloc[:, -1], SGDC_pred))
print("acc", accuracy_score(val_data.iloc[:, -1], SGDC_pred.astype(int)))
print("MSE", mean_squared_error(val_data.iloc[:, -1], SGDC_pred))

# save model
joblib.dump(SGDC, 'model/SGDC.pkl')
# load model
# rfc2 = joblib.load('saved_model/rfc.pkl')
