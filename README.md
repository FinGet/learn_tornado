## 特性和使用场景

- 不适合复杂的CMS(内容管理系统)应用
- 适合构建网站或者App后端微服务

## 安装

`pip install tornado`

```python
>>> import tornado
>>> tornado.version
'5.1.1'
```

## hello word

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

## web框架主要模块

- tornado.web.Application 和 RequestHandler 类处理http请求
- tornado.template 模板渲染
- tornado.routing 处理路由