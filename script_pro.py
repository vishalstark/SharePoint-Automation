from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import io
import pandas as pd
import base64


###########################################################################
# KINDLY CHANGE VALUES OF THE FOLLOWING ACCORDING TO YOUR NEEDS AND ACCOUNT
###########################################################################

FILE_NAME = 'file.csv'
USERNAME = 'username@mail.com'
PASSWORD = input('Enter the password : ')
PASSWORD = base64.b64decode(PASSWORD).decode("utf-8")
SITELINK = 'https://xyz.sharepoint.com/sites/MySharePointSite/'
FOLDER = 'Shared Documents/This Folder'

##########################################################################

def uploadFunc(df):
    try:
        authcookie = Office365('https://xyz.sharepoint.com', username = USERNAME, password = PASSWORD).GetCookies()
        site = Site(SITELINK, version=Version.v2016, authcookie=authcookie)
        folder = site.Folder(FOLDER)

        stream = io.StringIO()

        df.to_csv(stream, sep=",",index=False)

        print(stream.getvalue())
        folder.upload_file(stream.getvalue(), FILE_NAME)

        print('Task Completed Successfully')

    except Exception as e:

        print(f'Error Occured : {e}')

def readFunc(FILE_NAME):

    try:
        authcookie = Office365('https://xyz.sharepoint.com', username = USERNAME, password = PASSWORD).GetCookies()
        site = Site(SITELINK, version=Version.v2016, authcookie=authcookie)
        folder = site.Folder(FOLDER)
        
        bytes_file = folder.get_file(FILE_NAME)
        df = pd.read_csv(io.StringIO(bytes_file.decode('utf-8')), index_col=False)
        return df

    except Exception as e:

        print(f'Error Occured : {e}')


## Replace the following line with your dataframe
df = pd.DataFrame([[1,2,3,4,5]],columns=['a','b','c','d','e'])
uploadFunc(df)
readFunc(FILE_NAME)

