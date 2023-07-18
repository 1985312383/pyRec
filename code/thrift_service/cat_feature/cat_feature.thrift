namespace py cat.feature

struct UserFeauture {
    1: required string uid,
    2: optional string history_click_list,
    3: optional string favorite_category,
}

struct ItemFeature {
    1: required string item_id,
    2: optional string category,
    3: optional string sub_category,
    4: optional string entity_embeddig_id,
}

struct ContentFeature {
    1: required string time,
    2: optional string os,
    3: optional string hour,
    4: optional string minute,
    5: optional string second,
    6: optional string is_am,
}

struct CatFeatureReq {
    1: required string req_id,
    2: required string uid,
    3: required list<string> items,
    4: optional string time,
    5: optional map<string, string> extra_info,
    6: optional UserFeauture user_feature,
    7: optional ItemFeature item_feature,
    8: optional ContentFeature content_feature,
}

struct CatFeatureRsp {
//    1: required map<string, string> input_features,
//    2: optional i64 status_code,
    1: required string time,
    2: optional string os,
}

service CatFeatureService {
    CatFeatureRsp server(),
//    string server(),
}
