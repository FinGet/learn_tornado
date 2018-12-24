import time
import datetime as dt

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

class SleepHandler(tornado.web.RequestHandler):
  @tornado.gen.coroutine
  def get(self):
    # 在同一个浏览器中访问 还是 同步的，可以用两个重点 curl 测试
    yield tornado.gen.sleep(5)
    self.write(str(dt.datetime.now()))

if __name__ == "__main__":
  app = tornado.web.Application(
    [(r'/', SleepHandler)],
    debug = True
  )
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(8883)
  tornado.ioloop.IOLoop.instance().start()