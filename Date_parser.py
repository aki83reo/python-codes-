
############################## Identifying  dates  from  a  string  ##############################

from natty import DateParser  ##
#####################################################################

#######################This below function will  parse a string  and  understand if any dates  available or not  .
def DateParsing(inp2):
    dp = DateParser(inp2)
    return dp.result()

##############Above function  can handle  many dates
##  1. test 1 :  inp2= "i want to have yesterday "

test1=DateParsing(inp2)

##  result1: [datetime.datetime(2018, 3, 14, 17, 6, 2)]


## 2.  test2 :  inp2 = "i want to have yesterday and todays date "

test2= DateParsing(inp2)

####  result2 :  [datetime.datetime(2018, 3, 14, 17, 7, 34)]


##  3.  test3 :  inp2 ="i want to have day before yesterday date"

test3=DateParsing(inp2)

###  result3 :  [datetime.datetime(2018, 3, 13, 17, 8, 59)]

##  4.  test4 :inp2 =="i want to have  yesterday  and tomorrow "

test4 =DateParsing(inp2)

##  result4 :  [datetime.datetime(2018, 3, 14, 17, 9, 56),
                #datetime.datetime(2018, 3, 16, 17, 9, 56)]

#################################################################################################
################################Comparing with  present date  ###################################
##finding dates through out the  user intent
dates_from_user_intent=DateParsing(inp2)[0].replace(hour=0,minute=0,second=0,microsecond=0) #### asked date


###  I am  comparing  the asked date  by  the  user  with  our current date  ,  and  let  know , the date is  a  past date or
###  future date .

###Todays date  to  compare  with  the  asked date
import  datetime
todays_date=datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)##  today's date

### This  below function  will  decide  the  date asked by the user  is  past date  or  a  future  date .
def  which_date(dates_from_intent,todays_date):
    date_value=0
    if (dates_from_intent<todays_date):
        date_value="past_date"
    elif(dates_from_intent<todays_date ) :
        date_value="future_date"
    elif(dates_from_intent==todays_date ):
        date_value="present_date"
    return date_value


########################################################################################################