from localstack.utils.aws import aws_models
LKBNM=super
LKBNU=None
LKBNm=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  LKBNM(LambdaLayer,self).__init__(arn)
  self.cwd=LKBNU
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.LKBNm.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(RDSDatabase,self).__init__(LKBNm,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(RDSCluster,self).__init__(LKBNm,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(AppSyncAPI,self).__init__(LKBNm,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(AmplifyApp,self).__init__(LKBNm,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(ElastiCacheCluster,self).__init__(LKBNm,env=env)
class TransferServer(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(TransferServer,self).__init__(LKBNm,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(CloudFrontDistribution,self).__init__(LKBNm,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,LKBNm,env=LKBNU):
  LKBNM(CodeCommitRepository,self).__init__(LKBNm,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
