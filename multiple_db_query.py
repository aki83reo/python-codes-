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
import yaml
###################################################
es = Elasticsearch("http://127.0.0.1:9300")    #### Initializing  ElasticSearch instance  with localhost  at port  9300

def provider_details(providers_name,single_sensor_retrievel,data_inserted_in_sensor):

    ####  1. List all sensors  from the  database
    params = (('pretty', 'true\''),)
    response = requests.get('http://localhost:9200/'+providers_name+'/_mapping', params=params)
    k=yaml.load(response.text)
    list_of_sensors=list(k[providers_name]['mappings'].keys())   ###  result  will  be  ['sensor1', 'sensor2', 'sensor3']

    #################################################################################################################

    ####  2. Get data for a sensor by either ID, time range, value or combination of any of those.

    ###  I will try to get data  from a sensor  table data based  on daterange

    date1="2018-03-26 22:12:58"
    date2="2018-03-28 22:12:58"

    headers = {'Content-Type': 'application/json', }
    body = {
        "query": {
            "range": {
                "created": {
                    "gt":date1 ,
                    "lt":date2
                }
            }
        }
    }

    response = requests.post('http://localhost:9200/'+providers_name+ '/'+single_sensor_retrievel+'/_search', headers=headers,data=json.dumps(body))
    queried_data = yaml.load(response.text)

    single_sensor_data=queried_data['hits']['hits'][0]['_source']


    #### Result  set from the above  query

    #{'created': '2018-03-24 11:57:56',
     #'sensor_descr': 'secnd_freq',
     #'sensor_value': 101}

    ################################################################################################

    ## 3. Get data for all sensors based on a time range, value or a combination

    date1="2018-03-27 11:57:56"
    date2="2018-03-31 11:57:56"
    headers = {
        'Content-Type': 'application/json',
    }

    sensor_appnd1=0
    sensor_appnd2=0
    sensor_appnd3=0
    if(providers_name=="provider1"):
        sensor_appnd1="sen1"
        sensor_appnd2 = "sen2"
        sensor_appnd3="sen3"
    elif(providers_name=="provider2"):
        sensor_appnd1 = "sen4"
        sensor_appnd2 = "sen5"
        sensor_appnd3 = "sen6"
    elif (providers_name == "provider3"):
        sensor_appnd1 = "sen7"
        sensor_appnd2 = "sen8"
        sensor_appnd3 = "sen9"




    data1 = '\n{"type": "'+sensor_appnd1+'"}\n{"query" : {"range" : {"sensor_value":{ "gt":100 , "lt":102}}}}' \
            '\n{"type": "'+sensor_appnd2+'"}\n{"query" : {"range" : {"created":{"gt":'+'"'+''+date1+''+'"'',"lt":'+'"'+''+date2+''+'"''}}}}' \
            '\n{"type":"'+sensor_appnd3+'"}\n{"query" : {"range" : {"sensor_value":{ "gt":300}}}}\n'


    response = requests.post('http://localhost:9200/'+providers_name+'/_msearch', headers=headers, data=data1)
    queried_all_data = yaml.load(response.text)

    sensor1_queried_data=queried_all_data['responses'][0]['hits']['hits'][0]['_source']  ##  first sensor  quaried data
    sensor2_queried_data=queried_all_data['responses'][1]['hits']['hits'][0]['_source']  ##  secound sensor  quaried data
    sensor3_queried_data=queried_all_data['responses'][2]['hits']['hits'][0]['_source']  ##  third sensor  quaried data

    all_sensor_data={"sensor1":sensor1_queried_data,"sensor2":sensor2_queried_data,"sensor3":sensor3_queried_data}

    ############################

    ###  4. Insert data for a sensor with ID, timestamp and 2 parameters and their values.

    ##  We will  insert into  sensor3  new  data  based   on  parameters  from  sensor1,sensor2,sensor3
    #  called  "sensor_value"  sum them and update .
    ## in sensor3  with  a new  parameter  as  "updated_sensor_value  by time .
    ##  i am inserting date for tomorrow

    from datetime import datetime, timedelta
    import datetime
    tomorrows_date=datetime.datetime.now().replace(microsecond=0)+timedelta(days=1)   ###  date  parameter
    total_sum_value_from_three_sensors=sensor1_queried_data['sensor_value']+sensor2_queried_data['sensor_value']+sensor3_queried_data['sensor_value']


    Json_Update_sensor3={"updated_date":tomorrows_date,"total_sensor_value":total_sum_value_from_three_sensors,}


    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    #####################################SENSOR1  UPDATE
    extended_dat = []

    extended_dat.append(json.dumps(Json_Update_sensor3, default=myconverter))

      ####  dumping  all  data  into  elastic search  .
    req = requests.post('http://localhost:9200/'+providers_name+ '/'+data_inserted_in_sensor+'/', data=extended_dat[0])
    print(req.text)

    return print("List_of sensors"+  str(list_of_sensors)), print("Single_sensor_date"+ str(single_sensor_data)), print("All_sensor_data"+str(all_sensor_data))

provider_details("provider1","sen1","sen3")

provider_details("provider3","sen7","sen9")

provider_details("provider2","sen4","sen6")

