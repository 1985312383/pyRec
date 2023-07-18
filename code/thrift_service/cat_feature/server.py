import thriftpy2
from thriftpy2.rpc import make_server

CatFeature_thrift = thriftpy2.load("cat_feature.thrift", module_name="pingpong_thrift")


class Dispatcher(object):
    def server(self):
        log = CatFeature_thrift.CatFeatureRsp()
        log.time = "ghjkm"
        return log


server = make_server(CatFeature_thrift.CatFeatureService, Dispatcher(), '127.0.0.1', 6000)
server.serve()
