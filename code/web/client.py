import thriftpy2
from thriftpy2.rpc import make_client

CatFeature_thrift = thriftpy2.load("cat_item.thrift", module_name="pingpong_thrift")

client = make_client(CatFeature_thrift.CatFeatureService, '127.0.0.1', 6001)
print(client.server())
