import os


class BaseEngine(object):
    
    database = ''

    def __init__(self, database_name="indexdir"):
        self.database_name = database_name
        database_folder_path = "/tmp/epub_worker/databases/"

        if not os.path.exists(database_folder_path):
            os.mkdir(database_folder_path)

        self.database_path = database_folder_path + database_name
        self.open()
        pass

    def open(self):
        '''
        Opens the database for reading
        '''
        pass

    def create(self):
        '''
        Creates the database if it is not present
        Otherwise open current DB

        Setup writing to DB
        '''
        pass

    def clear(self):
        '''
        Clears the current database if it present
        '''
        pass

    def add(self, path='', href='', title='', cfiBase='', spinePos=''): 
        '''
        Called to load a single document from the spine
            - path = Relative path to the chapter
            - href = URL to chapter from the manifest
            - title = Title from the TOC
            - cfiBase = Chapter Base of the EPUBCFI
            - spinePos = position in the book (starting at 1) 
        '''
        pass

    def finished(self):
        '''
        Cleanup after adding all the chapters
        '''
        pass

    def query(self, q, limit=None):
        '''
        Returns a List of results containing Dicts with the following keys: 
            title
            href
            path
            title
            cfiBase
            spinePos
        '''
        results = []
        
        hit = [] # replace with DB query

        for hit in hits:
            item = {}
            item['title']   = hit["title"]
            item['href']    = hit["href"]
            item['path']    = hit["path"]
            item['title']   = hit["title"]
            item['cfiBase'] = hit["cfiBase"]
            item['spinePos']= hit["spinePos"]

            results.append(item)

        return results
