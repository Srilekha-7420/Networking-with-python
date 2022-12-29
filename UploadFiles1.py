import pyodbc

server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class UploadFilesToDB:

    def show_file_search_results_fromdb(self):
        values = cursor.execute('select * from FileSearchResults_table2')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))

    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        query = '''  
                    INSERT INTO FileSearchResults_table2 (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("New file search results committed to DB")

    # searches for a file in db
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # select query
        query = ''' select * from FileSearchResults_table2 where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = cursor.execute(searchQuery)

        for fileInfo in values:
            print("==========================")
            print("File name: {}".format(fileInfo.NameOfFile))
            print("File path: {}".format(fileInfo.File_Location))
            print("==========================")
        self.update_file_searchcount(fileName)


    def update_file_searchcount(self, fileName):
        query = ''' select * from FileSearchResults_table2 where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        noCount = """ SET NOCOUNT ON; """

        values = cursor.execute(noCount+searchQuery)

        for fileInfo in values:
            fileSearchCount = fileInfo.SearchCount
            fileinfoQuery = '''
                    Update FileSearchResults_table2 SET SearchCount = {0} WHERE NameOfFile = '{1}'
                    '''
            updateQuery = fileinfoQuery.format(fileSearchCount + 1, fileName)
            cursor.execute(noCount+updateQuery)
            cursor.commit()
            print("Updated file search count")

