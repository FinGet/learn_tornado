import time
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

class SleepHandler(tornado.web.RequestHandler):
  def get(self):
    time.sleep(5)
    # 等5秒 页面才加载完
    self.write('when i sleep')

if __name__ == "__main__":
  app = tornado.web.Application(
    [(r'/sleep', SleepHandler)]
  )
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(8882)
  tornado.ioloop.IOLoop.instance().start()