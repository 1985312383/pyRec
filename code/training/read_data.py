import pandas as pd
import os


def read_data(mode='train', dataset='behaviors'):
    if mode == 'train' or mode == 'test' or mode == 'val':
        temp_dir = "./datasets/" + mode
    else:
        raise Exception('Do not have this mode, please check your input!')

    if dataset == 'behaviors':
        # The behaviors.tsv file contains the impression logs and users' news click histories.
        # It has 5 columns divided by the tab symbol:
        # - Impression ID. The ID of an impression.
        # - User ID. The anonymous ID of a user.
        # - Time. The impression time with format "MM/DD/YYYY HH:MM:SS AM/PM".
        # - History. The news click history (ID list of clicked news) of this user before this impression.
        # - Impressions. List of news displayed in this impression and user's click behaviors on them (1 for click and 0 for non-click).
        behaviors_path = os.path.join(temp_dir, 'behaviors.tsv')
        behaviors = pd.read_table(
            behaviors_path,
            header=None,
            names=['impression_id', 'user_id', 'time', 'history', 'impressions'])
        return behaviors

    elif dataset == 'news':
        # The news.tsv file contains the detailed information of news articles involved in the behaviors.tsv file.
        # It has 7 columns, which are divided by the tab symbol:
        # - News ID
        # - Category
        # - Subcategory
        # - Title
        # - Abstract
        # - URL
        # - Title Entities (entities contained in the title of this news)
        # - Abstract Entities (entities contained in the abstract of this news)
        news_path = os.path.join(temp_dir, 'news.tsv')
        news = pd.read_table(news_path,
                             header=None,
                             names=[
                                 'id', 'category', 'subcategory', 'title', 'abstract', 'url',
                                 'title_entities', 'abstract_entities'
                             ])
        return news

    elif dataset == 'entity_embedding':
        # The entity_embedding.vec file contains the 100-dimensional embeddings
        # of the entities learned from the subgraph by TransE method.
        # The first column is the ID of entity, and the other columns are the embedding vector values.
        entity_embedding_path = os.path.join(temp_dir, 'entity_embedding.vec')
        entity_embedding = pd.read_table(entity_embedding_path, header=None)
        entity_embedding['vector'] = entity_embedding.iloc[:, 1:101].values.tolist()
        entity_embedding = entity_embedding[[0,
                                             'vector']].rename(columns={0: "entity"})
        return entity_embedding

    elif dataset == 'relation_embedding':
        # The relation_embedding.vec file contains the 100-dimensional embeddings
        # of the relations learned from the subgraph by TransE method.
        # The first column is the ID of relation, and the other columns are the embedding vector values.
        relation_embedding_path = os.path.join(temp_dir, 'relation_embedding.vec')
        relation_embedding = pd.read_table(relation_embedding_path, header=None)
        relation_embedding['vector'] = relation_embedding.iloc[:,
                                       1:101].values.tolist()
        relation_embedding = relation_embedding[[0, 'vector'
                                                 ]].rename(columns={0: "relation"})
        return relation_embedding
    else:
        raise Exception('Do not have this dataset, please check your input!')


# if __name__ == '__main__':
#     read_data(mode='ff', dataset='be')  # 报错测试
