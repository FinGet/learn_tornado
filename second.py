import time
import datetime as dt
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

class SleepHandler(tornado.web.RequestHandler):
  def get(self):
    time.sleep(5)
    # 等5秒 页面才加载完 同时打开两个，第二个会等第一个加载完，再等5秒才加载完成（同步）
    self.write('when i sleep')
    self.write(str(dt.datetime.now()))

if __name__ == "__main__":
  app = tornado.web.Application(
    [(r'/sleep', SleepHandler)]
  )
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(8882)
  tornado.ioloop.IOLoop.instance().start()