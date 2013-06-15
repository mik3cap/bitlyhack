"""
Rovi integration

usage: python rovi.py
Options and arguments:
-d : debug output (also --debug)
-h : print this help message and exit (also --help)

"""

__author__ = "Mike Caprio (mik3cap@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/06/15 15:17:00 $"
__copyright__ = ""
__license__ = "Python"


#import errno
#import sys
#import os
#import getopt
import datetime
import hashlib

#from database.mysql_config import *
#from utilities.datetimeutil import gettime
#from utilities.log import log
from url_request import dorequest

shared_secret = "QYDb7gXPXp"
api_key = "tyh5tujv82t7jyf25y849p6n"

server = "http://api.rovicorp.com/data/"
version = "v1.1/"
request_type = "GET"

output_country = "US"
output_lang = "en"
output_format = "json"


url = server + version + "descriptor/musicmoods"

### No options for descriptor/musicmoods


### No options for 
# The URL for which the content's profile should be retrieved.
#url_string = "http://www.techcrunch.com/"

# By default, each classification category is represented in the profile by
# its ID (a String). If you send true you will instead receive the
# human-readable names.
#humread_bool = "1"


future = datetime.datetime.now()
epoch_ts = future.strftime("%s")

message = api_key + shared_secret + epoch_ts
SHA_sig = hashlib.md5(message).hexdigest()

response_dict = {}

# Params will be encoded in the dorequest function
params = {"country": output_country,
          "language": output_lang,
          "format": output_format,
          "apikey": api_key,
          "sig": SHA_sig}

# Process the result from the search query, parse JSON
# into a dictionary of results
response_dict = dorequest(url, request_type, params)

# Find the data list and paging dict in the response dictionary
print response_dict
#data_list = response_dict[""]

#for each_key in data_list.keys():
#    url_response = data_list[each_key]["url"]
#    classification_reponse = data_list[each_key]["classification"]

    # Insert into a DB?
