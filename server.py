import traceback
import cherrypy
from fetchStocks import EqBhavCopyController
import json
import os



class SockSever(object):
    @cherrypy.expose
    def index(self):
        # template = env.get_template('templates/index.html')
        # return template.render()
        return open("templates/index.html")

    @cherrypy.expose
    def get_top_stocks(self,page_no=None):
        res = {"status": 0, "data": ""}
        try:
            page_no=0 if page_no is None else int(page_no)
            con=EqBhavCopyController()
            res=con.get_top_stocks(page_no)
            print(res)
        except Exception as e:
            traceback.print_exc()
            res["data"] = "Error! Please try again later."
        return json.dumps(res)

    @cherrypy.expose
    def get_stock_by_name(self,name_to_search=None):
        res = {"status": 0, "data": ""}
        try:
            if name_to_search is None or name_to_search.strip() == "":
                res["data"] = "Kindly provide valid name"
            else:
                con = EqBhavCopyController()
                res = con.get_stock_by_name(name_to_search.strip())
        except Exception as e:
            traceback.print_exc()
            res["data"] = "Something went wrong, Kindly try again.server222"
        return json.dumps(res)

    @cherrypy.expose
    def get_latest_stocks(self):
        res = {"status": 0, "data": ""}
        try:
            con = EqBhavCopyController()
            res = con.get_latest_stocks()
        except Exception as e:
            traceback.print_exc()
            res["data"] = "Something went wrong, Kindly try again.server333"
        return json.dumps(res)


config={
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
        '/static':
            {'tools.staticdir.on': True,
             #'tools.staticdir.dir':  os.path.abspath(os.getcwd())+"/assets"
             'tools.staticdir.dir':  os.path.join(os.path.abspath(os.getcwd()),"assets")
             }
    }
if __name__ == '__main__':
    cherrypy.quickstart(SockSever(),config=config)
