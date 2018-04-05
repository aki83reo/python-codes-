# python-codes-
In this repo  , i put some simple  codes  which are  useful   in day to day  life  of a  developer  .

The repo  will  be having  code base  of python codes .

#######################  1st .py  file 
In this  my  first  try  is  to  put  some  basic's of connecting  python(3.6)  with  mongodb secoundary db  in server , many people face serious problem's in configuration .



This  configuration.py  file  also  contains  basic  mongo  query operation , to pull data  in various  ways . 

         
####################  2nd .py  file  
In  python_elastic_search.py  file  ,  i  tried  to  do  the below task , 

-->  create  index in  server side  elastic search  one  index  using  pyelasticsearch  package  . 

-->  tried  to make  a  mapping for our index  , before pushing data  . 

-->  tried pushing  data  into  elasticsearch  index type  by  restful API's (GET  &  POST  requests)  

--> pull  data from elastic search  into local python console .


################### 3rd .py file 

In  Date_parser.py  file ,  i  had  tried to  include a  awesome  library from natty called as dateparser  to  parse  textual dates  like ,  yesterday  , tomorrow ,  or any other format . It can  extract  dates from  a  string  contain  a date  like below . 

"  my  birthday was tomorrow  "   =  It will  extract tomorrow  and give  tomorrows  date in datetime format  
datetime.datetime(2018, 3, 14, 17, 9, 56)

I created  two  functions  in this file ,  first(DateParsing(inp2)) to  identify  dates ,  secound is  to  compare  is the asked date ispresent or  past or future   date (which_date() ) .  


########## data_update_elastic.py 

1.In this  file  , i have demonstrated a way  how you  can define  your own schema 

for your database in elastic , and push  some data  according to  that  . 

2. Defined  a  function called  provider_value_insert(provider_name,sensor_1,sensor_2,sensor_3), which  allows any  users  to  create  

a index/database in elasticSearch ,along with 3  tables  .

The dates are  defined  for today  , previous and day  before  yesterday  . 

I hard coded the data  inside , but users  are free to  change  and  manipulate  as per there  choices .


Then  i  used  standard CURL  requests to  push data into  elastic search  . 


###########multiple_db_query.py 

1.  I created  a function  called  ,provider_details(providers_name,single_sensor_retrievel,data_inserted_in_sensor)  , which  basically  gives  users 

flexibility  to  decide which  DB user  want to  access  ,  along with  , define  a  single table/type  value  whose data user  wants  to  see .

third if after manipulation user wants  to  push changes  to a selected  table  he can  describe  it here  . 



In this  i  tried  to  pull  data  from  multiple  index/dbs  from elasticsearch .




