



                 


        


                    
                        


# Static analyzer import helpers: (STATIC_IMPORT_MARK)
if 0: 
    import gluon
    global cache; cache = gluon.cache.Cache()
    global LOAD; LOAD  = gluon.compileapp.LoadFactory()
    import gluon.compileapp.local_import_aux as local_import #@UnusedImport
    from gluon.contrib.gql import GQLDB #@UnusedImport
    from gluon.dal import Field #@UnusedImport
    global request; request = gluon.globals.Request()
    global response; response = gluon.globals.Response()
    global session; session = gluon.globals.Session()
    from gluon.html import A #@UnusedImport
    from gluon.html import B #@UnusedImport
    from gluon.html import BEAUTIFY #@UnusedImport
    from gluon.html import BODY #@UnusedImport
    from gluon.html import BR #@UnusedImport
    from gluon.html import CENTER #@UnusedImport
    from gluon.html import CODE #@UnusedImport
    from gluon.html import DIV #@UnusedImport
    from gluon.html import EM #@UnusedImport
    from gluon.html import EMBED #@UnusedImport
    from gluon.html import embed64 #@UnusedImport
    from gluon.html import FIELDSET #@UnusedImport
    from gluon.html import FORM #@UnusedImport
    from gluon.html import H1 #@UnusedImport
    from gluon.html import H2 #@UnusedImport
    from gluon.html import H3 #@UnusedImport
    from gluon.html import H4 #@UnusedImport
    from gluon.html import H5 #@UnusedImport
    from gluon.html import H6 #@UnusedImport
    from gluon.html import HEAD #@UnusedImport
    from gluon.html import HR #@UnusedImport
    from gluon.html import HTML #@UnusedImport
    from gluon.html import I #@UnusedImport
    from gluon.html import IFRAME #@UnusedImport
    from gluon.html import IMG #@UnusedImport
    from gluon.html import INPUT #@UnusedImport
    from gluon.html import LABEL #@UnusedImport
    from gluon.html import LEGEND #@UnusedImport
    from gluon.html import LI #@UnusedImport
    from gluon.html import LINK #@UnusedImport
    from gluon.html import MARKMIN #@UnusedImport
    from gluon.html import MENU #@UnusedImport
    from gluon.html import META #@UnusedImport
    from gluon.html import OBJECT #@UnusedImport
    from gluon.html import OL #@UnusedImport
    from gluon.html import ON #@UnusedImport
    from gluon.html import OPTGROUP #@UnusedImport
    from gluon.html import OPTION #@UnusedImport
    from gluon.html import P #@UnusedImport
    from gluon.html import PRE #@UnusedImport
    from gluon.html import STYLE #@UnusedImport
    from gluon.html import SCRIPT #@UnusedImport
    from gluon.html import SELECT #@UnusedImport
    from gluon.html import SPAN #@UnusedImport
    from gluon.html import TABLE #@UnusedImport
    from gluon.html import TAG #@UnusedImport
    from gluon.html import TBODY #@UnusedImport
    from gluon.html import TD #@UnusedImport
    from gluon.html import TEXTAREA #@UnusedImport
    from gluon.html import TFOOT #@UnusedImport
    from gluon.html import TH  #@UnusedImport
    from gluon.html import THEAD #@UnusedImport
    from gluon.html import TITLE #@UnusedImport
    from gluon.html import TR #@UnusedImport
    from gluon.html import TT #@UnusedImport
    from gluon.html import UL #@UnusedImport
    from gluon.html import URL #@UnusedImport
    from gluon.html import XHTML #@UnusedImport
    from gluon.html import XML #@UnusedImport
    from gluon.html import xmlescape #@UnusedImport
    from gluon.http import HTTP #@UnusedImport
    from gluon.http import redirect #@UnusedImport
    import gluon.languages.translator as T #@UnusedImport
    from gluon.sql import DAL
    global db; db = DAL()
    from gluon.sql import SQLDB #@UnusedImport
    from gluon.sql import SQLField #@UnusedImport
    from gluon.sqlhtml import SQLFORM #@UnusedImport
    from gluon.sqlhtml import SQLTABLE #@UnusedImport
    from gluon.tools import  Auth
    global auth; auth = Auth()
    from gluon.tools import Crud
    global crud; crud = Crud()
    from gluon.tools import fetch #@UnusedImport
    from gluon.tools import geocode #@UnusedImport
    from gluon.tools import Mail
    global mail; mail = Mail()
    from gluon.tools import PluginManager
    global plugins; plugins = PluginManager()
    from gluon.tools import prettydate #@UnusedImport
    from gluon.tools import Recaptcha #@UnusedImport
    from gluon.tools import Service
    global service; service = Service()
    from gluon.validators import CLEANUP  #@UnusedImport
    from gluon.validators import CRYPT #@UnusedImport
    from gluon.validators import IS_ALPHANUMERIC #@UnusedImport
    from gluon.validators import IS_DATE #@UnusedImport
    from gluon.validators import IS_DATE_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DATETIME #@UnusedImport
    from gluon.validators import IS_DATETIME_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DECIMAL_IN_RANGE #@UnusedImport
    from gluon.validators import IS_EMAIL #@UnusedImport
    from gluon.validators import IS_EMPTY_OR #@UnusedImport
    from gluon.validators import IS_EQUAL_TO #@UnusedImport
    from gluon.validators import IS_EXPR #@UnusedImport
    from gluon.validators import IS_FLOAT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IMAGE #@UnusedImport
    from gluon.validators import IS_IN_DB #@UnusedImport
    from gluon.validators import IS_IN_SET #@UnusedImport
    from gluon.validators import IS_INT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IPV4 #@UnusedImport
    from gluon.validators import IS_LENGTH #@UnusedImport
    from gluon.validators import IS_LIST_OF #@UnusedImport
    from gluon.validators import IS_LOWER #@UnusedImport
    from gluon.validators import IS_MATCH #@UnusedImport
    from gluon.validators import IS_NOT_EMPTY #@UnusedImport
    from gluon.validators import IS_NOT_IN_DB #@UnusedImport
    from gluon.validators import IS_NULL_OR #@UnusedImport
    from gluon.validators import IS_SLUG #@UnusedImport
    from gluon.validators import IS_STRONG  #@UnusedImport
    from gluon.validators import IS_TIME #@UnusedImport
    from gluon.validators import IS_UPLOAD_FILENAME #@UnusedImport
    from gluon.validators import IS_UPPER #@UnusedImport
    from gluon.validators import IS_URL #@UnusedImport

