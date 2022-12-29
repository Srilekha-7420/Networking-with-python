import os
import re
import win32api
import concurrent.futures
import pyodbc
def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                insert_file_search_results(root, f, 0)
                break  # if you want to find only one
server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

def show_file_search_results_fromdb():
    values = cursor.execute('select * from FileSearchResults_table2')
    for fileInfo in values:
        print("File Name: {}".format(fileInfo.NameOfFile))
        print("File Location: {}".format(fileInfo.File_Location))

def upload_file_results_todb(fileName, fileLocation, searchCount):
    query = '''  
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('{0}',{1},'{2}')  '''

    insertQuery = query.format(fileLocation, searchCount, fileName)
    cursor.execute(insertQuery)
    cnxn.commit()
    #print("New file search results committed to DB")

# searches for a file in db
# Input : Filename (string)
# output : True or False (Boolean)
def search_in_db_for_file(fileName):
    # select query
    query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
    searchQuery = query.format(fileName)
    values = cursor.execute(searchQuery)
    if(values):
        for fileInfo in values:
            print("==========================")
            print("File name: {}".format(fileInfo.NameOfFile))
            print("File path: {}".format(fileInfo.File_Location))
            print("==========================")
        return True
    return False
def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        [executor.submit(find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

def insert_file_search_results(fileLocation, fileName, searchCount = 0):
    upload_file_results_todb(fileName, fileLocation, searchCount)

def search_forfile_indb(fileName):
    fileSearchStatus = search_in_db_for_file(fileName)

    if(fileSearchStatus):
        find_file_in_all_drives(fileName)

fileToSearch = input()
search_forfile_indb(fileToSearch)