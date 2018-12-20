import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("500.html", msg="后台发送的信息，参数传递")

def make_app():
    return tornado.web.Application(
        # 路由
        [
          (r"/", MainHandler),
          (r"/500", ErrorHandler)
        ],
        # 模板路径
        template_path = os.path.join(
          os.path.dirname(__file__),"templates"
        ),
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8881)
    tornado.ioloop.IOLoop.current().start()