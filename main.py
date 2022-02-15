from urllib.request import urlretrieve


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

totalrequest=0
pastrequest=0

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

from urllib.request import urlretrieve


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

totalrequest=0
pastrequest=0

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)



print("The total requests over the past 6 months is: " + str(pastrequest))
print()
print('The total request overall for the logfile is: ' + str(totalrequest))


