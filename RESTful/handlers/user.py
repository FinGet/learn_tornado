import tornado.web

from tornado.escape import json_encode

class UserListHandler(tornado.web.RequestHandler):
  def get(self):
    from models.user import UserModel
    users = UserModel.get_all()
    self.write(json_encode(users))

  def post(self):
    from models.user import UserModel
    name = self.get_argument('name')
    age = self.get_argument('age')
    UserModel.create(name, age)
    resp = {'status': True, 'msg': 'create success'}
    self.write(json_encode(resp))