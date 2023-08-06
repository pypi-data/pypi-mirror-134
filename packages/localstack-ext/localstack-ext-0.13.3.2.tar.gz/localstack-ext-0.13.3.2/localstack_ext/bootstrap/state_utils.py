import logging
IRJqT=bool
IRJqi=hasattr
IRJqU=set
IRJqD=True
IRJqG=False
IRJqF=isinstance
IRJqw=dict
IRJqv=getattr
IRJqm=None
IRJqB=str
IRJqz=Exception
IRJqP=open
import os
from typing import Any,Callable,List,OrderedDict,Set,Tuple
import dill
from localstack.utils.common import ObjectIdHashComparator
API_STATES_DIR="api_states"
KINESIS_DIR="kinesis"
DYNAMODB_DIR="dynamodb"
LOG=logging.getLogger(__name__)
def check_already_visited(obj,visited:Set)->Tuple[IRJqT,Set]:
 if IRJqi(obj,"__dict__"):
  visited=visited or IRJqU()
  wrapper=ObjectIdHashComparator(obj)
  if wrapper in visited:
   return IRJqD,visited
  visited.add(wrapper)
 return IRJqG,visited
def get_object_dict(obj):
 if IRJqF(obj,IRJqw):
  return obj
 obj_dict=IRJqv(obj,"__dict__",IRJqm)
 return obj_dict
def is_composite_type(obj):
 return IRJqF(obj,(IRJqw,OrderedDict))or IRJqi(obj,"__dict__")
def api_states_traverse(api_states_path:IRJqB,side_effect:Callable[...,IRJqm],mutables:List[Any]):
 for dir_name,_,file_list in os.walk(api_states_path):
  for file_name in file_list:
   try:
    subdirs=os.path.normpath(dir_name).split(os.sep)
    region=subdirs[-1]
    service_name=subdirs[-2]
    side_effect(dir_name=dir_name,fname=file_name,region=region,service_name=service_name,mutables=mutables)
   except IRJqz as e:
    LOG.warning(f"Failed to apply {side_effect.__name__} for {file_name} in dir {dir_name}: {e}")
    continue
def load_persisted_object(state_file):
 if not os.path.isfile(state_file):
  return
 import dill
 with IRJqP(state_file,"rb")as f:
  try:
   content=f.read()
   result=dill.loads(content)
   return result
  except IRJqz as e:
   LOG.debug("Unable to read pickled persistence file %s: %s"%(state_file,e))
def persist_object(obj,state_file):
 with IRJqP(state_file,"wb")as f:
  result=f.write(dill.dumps(obj))
  return result
# Created by pyminifier (https://github.com/liftoff/pyminifier)
