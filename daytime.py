import datetime 

birthday = "1-May-12"
date_format = "%d-%b-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)
#My computer could not run the date w/o the leading 0, according to Stackoverflow
date_str = parsed_date.strftime("%m/%d/%Y")
print(date_str)