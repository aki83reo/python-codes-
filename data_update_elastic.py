##Packages######################################
import numpy as np
import string
import pandas  as  pd
import datetime
import pymongo
import json
import requests
from dateutil import parser
import pyelasticsearch
from pyelasticsearch import ElasticSearch
from elasticsearch import Elasticsearch
###################################################

es = Elasticsearch("http://127.0.0.1:9300")    #### Initializing  ElasticSearch instance  with localhost  at port  9300


##############################################################################

############################# Mapping  of  data  to be inserted into elastic search############
######  There  will  be 3  sensors in our  database(index)  "sensor" ,  sensor1, sensor2, sensor3  as  type(tables)
#####   Each sensor  have  3  pairs  of values  - "sensor_value" , "created"(date_format) , "sensor_descr" (description about the sensor)
####    Below  we  defined  the  datatypes  of the above variables  using mapping .
'''
PUT provider2
{
    "mappings": {
        "sensor1": {
            "properties": {

                "sensor_value": {
                    "type": "long"
                },

                "created": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss"
                },

                "sensor_descr": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                }
            }
        }
    }
}

'''

##########################################################################
###############Define  Data to  be inserted  into  3 sensors

def provider_value_insert(provider_name,sensor_1,sensor_2,sensor_3):
    from datetime import datetime, timedelta
    import datetime

    ##### Took 3 dates   , present  ,  previous  , and  day  before  previous  for all  the  three  sensors
    #### removed  microsecound

    todays_date= datetime.datetime.now().replace(microsecond=0)
    yesterdays_date=todays_date.replace(microsecond=0)- timedelta(days=1)
    day_before_yesterday_date=todays_date.replace(microsecond=0)- timedelta(days=2)


    sensor1=pd.DataFrame({"sensor_value":[100,101,102],"created":[todays_date,yesterdays_date,day_before_yesterday_date],"sensor_descr":["first_freq","secnd_freq","third_freq"]})
    sensor2=pd.DataFrame({"sensor_value":[200,201,202],"created":[todays_date,yesterdays_date,day_before_yesterday_date],"sensor_descr":["forth_freq","fifth_freq","sixth_freq"]})
    sensor3=pd.DataFrame({"sensor_value":[300,301,302],"created":[todays_date,yesterdays_date,day_before_yesterday_date],"sensor_descr":["seventh_freq","eight_freq","nine_freq"]})


    ###   Convert all  dataframe   to json  format
    SENSOR1_JSON = sensor1.to_dict(orient='records')
    SENSOR2_JSON = sensor2.to_dict(orient='records')
    SENSOR3_JSON = sensor3.to_dict(orient='records')
    ########################################UPDATE SENSOR1 SENSOR2 SENSOR3 TABLES  ###############################

    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    #####################################SENSOR1  UPDATE
    extended_dat = []
    for i in range(sensor1.__len__()):  ###  converting  dict  to  strings
        extended_dat.append(json.dumps(SENSOR1_JSON[i], default=myconverter))

    for item in range(SENSOR1_JSON.__len__()):  ####  dumping  all  data  into  elastic search  .
        req = requests.post('http://localhost:9200/'+provider_name+'/'+sensor_1+'/', data=extended_dat[item])
        print(req.text)

    #####################################SENSOR2  UPDATE
    extended_dat = []
    for i in range(sensor1.__len__()):  ###  converting  dict  to  strings
        extended_dat.append(json.dumps(SENSOR2_JSON[i], default=myconverter))

    for item in range(SENSOR1_JSON.__len__()):  ####  dumping  all  data  into  elastic search  .
        req = requests.post('http://localhost:9200/'+provider_name+'/'+sensor_2+'/', data=extended_dat[item])
        print(req.text)

    #####################################SENSOR3  UPDATE
    extended_dat = []
    for i in range(sensor3.__len__()):  ###  converting  dict  to  strings
        extended_dat.append(json.dumps(SENSOR3_JSON[i], default=myconverter))

    for item in range(SENSOR3_JSON.__len__()):  ####  dumping  all  data  into  elastic search  .
        req = requests.post('http://localhost:9200/'+provider_name+'/'+sensor_3+'/', data=extended_dat[item])
        print(req.text)

######################################### DATA UPDATE  FINISHED ########################

provider_value_insert("provider1","sen1","sen2","sen3")  #### Provider 1

provider_value_insert("provider2","sen4","sen5","sen6")  ###  Provider 2

provider_value_insert("provider3","sen7","sen8","sen9")  ###  Provider 3

