from SpaceDock.config import _cfg, _cfgi
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from SpaceDock.app import app
from SpaceDock.app import app

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(_cfgi("debug-port"), address=_cfg("debug-host"))
    IOLoop.instance().start()
