
## use Tower to management project
import os

class TowerAPI:
    _instance = None
    _web = False

    
    
    def setMethod(self, method):
        """
        @description  : set class method in web services or cmd
        ---------
        @param  : method: 'web' or others
        -------
        @Returns  : none
        -------
        """
        
        if method == 'web':
            self._web = True
        else:
            self._web = False
        return self

    def get_access_token(self):

        # check access file exist
        if not os.path.exists(os.path.join(os.getcwd(),'tmp','tower_access_token.json')):
            pass

    def get_access_token():
        pass
    
        
    def check_access_file():
        print
        # if os.path.exists(access_token_file_name):
        # print("get existed access code")

    ## single instance model
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
        
    def __init__(self):
        return self

    def __str__(self) -> str:
        
        pass