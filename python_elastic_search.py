####################### Packages
import requests     ####  this package is  to put and retrieve data from elastic search
import yaml         ####   after bringing data from elastic search , converting it to  a dictionery
import json         ####  while putting dict  in elastic , it need to be converted to json
from elasticsearch import Elasticsearch ### this package  will be helpful to create an index in elastic
import datetime
import pandas as pd
#######################################################
es = Elasticsearch()         ##initializing  elastic search
################### CREATING A INDEX  IN ELASTIC SEARCH  ###################

################## INDEX  ARE KIND OF DATABASES  ########################
################## TYPES  ARE TABLES  IN THE DATABASE #################

################################ This below function will  check for any index available or not , if not  to create  a new  one .
def chck_indx_avail():
    if es.indices.exists(index="index_name"):
        return "Both  index  exists "
    else:
        es.indices.create(index='index_name', ignore=400)
        return "index insert  sucessful"

#########################################################################################

#1.  CREATING  MAPPING FOR DATA PUSH  #############################################
###Tasks :
          ####  Before pushing data , define a mapping for your data like below example .
          ###  i want to push  , 3 variables , " amount" , "name", "todays_date"
          ###  Its  ideal  to setup kibana / Postman, there this codes  can be executed easily



   # PUT index_name  ###########  PUT  command follow by index name /database name in layman  language.
    #{
     #   "mappings": {
      #      "index_type": {   ### It is the  code for table  creation  ,  index_type  will  be your table ,where all 3 vars will be added
       #         "properties": {
        #            "amount": {        #####  1st  var
         #               "type": "long"  ### defining  as  long
          #          },
           ##            "type": "name",  ###  2nd var
             #           "fields": {
              #              "keyword": {
               #                 "type": "keyword", ## define as keyword type
                #                "ignore_above": 256
                 #           }
                  ###"todays_date": {  ##  3rd var
                     #   "type": "date", ## define as date variable
                      #  "format": "yyyy-MM-dd HH:mm:ss"
                    #}
                #}
            #}
        #}
    #}

############################################################################################

###2. DATA  PUSH  FROM DICTIONERY TO  JSON

#######################################Some time during pushing date will create  problem ,
####################################### you will  understand while pushing data  with dates
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

my_data=pd.read_csv("F://my.csv")  ########## Reading a dataset  as csv
my_data_elastic =my_data.to_dict(orient='records')  ## Convert dataframe  as  dictionery


#########loop  through the dictionery  and append it  a list
######### json.dumps to  convert dict obj to  json_serialize
data_list = []
for i in range(my_data_elastic.__len__()):  ###  converting  dict  to  strings
    data_list.append(json.dumps(my_data_elastic[i], default=myconverter))

headers = {'Content-Type': 'application/json', }  ###  THis are to  know we are pushing  a json file
########## Loop through the dictionery  and push  data  into  index and  type
for item in range(my_data_elastic.__len__()):  ####  dumping  all  data  into  elastic search  .
    req = requests.post('http://localhost:9200/index_name/index_type/',headers=headers,data=my_data_elastic[item])
    print(req.text)

####################################################################################################################

###3. PULL  DATA    FROM  ELASTIC SEARCH  INDEX  AND FROM A   PERTICULAR TYPE
     ### By  default  you  can pull at most 10000 documents from elatic
params = (('pretty', ''),)
data = '\n{\n  "size":10000\n}'   ### how many docs needed to  be brought
response = requests.get('http://localhost:9200/index_name/index_type/_search', params=params,data=data)
brought_data=yaml.load(response.text)   ######  to convert to  dictionery

###################################################################################################

