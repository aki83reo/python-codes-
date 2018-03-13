#################  Codes to  connect  with  a  server  mongodb database(replica set)  using  pymongo

####### Packages ############################################
import pymongo                     ###  package  to  connect mongodb  and python
from  pymongo import MongoClient   ###   mongoclient  to establish  connections
from  pymongo import mongo_replica_set_client  ###  package  to  connect  with  server  mongodb  replica set
from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.read_preferences import ReadPreference  #### What  type of access  user is having  (read/write )
import datetime
##################################################################


######################  Codes to  connect to  secoundary replica  set   No sql database
rsc = MongoClient('address1.com,address2.com,arbitor3.com', replicaSet='replica_data',
                  read_preference=ReadPreference.SECONDARY_PREFERRED, ssl=True,
                  ssl_certfile='F:/your_pem_file/xyz.pem')
rsc.database_name.authenticate('username', 'password', mechanism='SCRAM-SHA-1')   ###  authenticating database
db_access = rsc.database_name ####  defining  database
db_my_col = db_access.my_collection ## calling  collections  using  db access

#################################################################################################################


######################  Basic  Mongo   queries

####  1. Getting all  json data  from  a my_collection collection

load_all_data =[]  ###  list will  contain  all json files
for all_info in db_my_col.find({}):load_all_data .append(all_info)

####  2.  Getting  by specific dates  data

current_date_time = datetime.datetime.now()

start_time = current_date_time.replace(day=current_date_time, hour=0, minute=0, second=0, microsecond=0)  ##start  date
end_time = current_date_time.replace( day=current_date_time-1,hour=0, minute=0, second=0, microsecond=0)   ##start  date

loading_date_data=[]


###########  This query will  bring data  from yesterday till today's  date , provided , "date" column should be there in your db.

for all_info in db_my_col.find({"date": {'$gte':start_time ,'$lte': end_time}}):loading_date_data .append(all_info)

##########  This  query  will bring only  three  key-value from your db  , "your_key1","your_key_2","your_key_3"  only leaving other key-value pairs .
loading_date_data=[]
for all_info in db_my_col.find({},{"your_key1": 1, "your_key2": 1, "your_key3": 1}):loading_date_data .append(all_info)

###########This query will extract documents having either  type as "one"  or "two" or "three" or "four"

loading_date_data=[]
for all_info in db_my_col.find(
        {"$or": [{"type": "one"}, {"type": "two"}, {"type": "three"}, {"type": "four"}]},

           ): loading_date_data.append(all_info)

###########  If  you want  to  avoid certain key value  pair ,your_key1=0  ###################

for all_info in db_my_col.find({},{"your_key1":0}):loading_date_data .append(all_info)


