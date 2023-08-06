from localstack.utils.aws import aws_models
IoFmp=super
IoFmW=None
IoFmV=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  IoFmp(LambdaLayer,self).__init__(arn)
  self.cwd=IoFmW
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.IoFmV.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(RDSDatabase,self).__init__(IoFmV,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(RDSCluster,self).__init__(IoFmV,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(AppSyncAPI,self).__init__(IoFmV,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(AmplifyApp,self).__init__(IoFmV,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(ElastiCacheCluster,self).__init__(IoFmV,env=env)
class TransferServer(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(TransferServer,self).__init__(IoFmV,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(CloudFrontDistribution,self).__init__(IoFmV,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,IoFmV,env=IoFmW):
  IoFmp(CodeCommitRepository,self).__init__(IoFmV,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
