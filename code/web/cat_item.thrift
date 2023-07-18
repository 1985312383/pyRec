//struct item {
//    1: required string title,
//    2: optional string category,
//    3: optional string abs,
//    4: optional string author,
//    5: optional string image,
//    6: optional string content,
//    7: optional string date,
//}

struct Items {
    1: optional list<string> iid
    2: optional list<string> title,
    3: optional list<string> category,
    4: optional list<string> abs,
    5: optional list<string> author,
    6: optional list<string> date
    8: optional list<string> content
    9: optional list<string> image,
}

service CatItemService {
    Items items(1:i32 request),
}
