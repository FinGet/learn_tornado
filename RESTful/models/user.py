class UserModel(object):
  users = {
    1: {'name': 'zhang', 'age': 20},
    2: {'name': 'wang', 'age': 21},
    3: {'name': 'zhao', 'age': 22},
    4: {'name': 'qian', 'age': 24},
    5: {'name': 'sun', 'age': 22},
  }

  @classmethod
  def get(cls, user_id):
    return cls.users[user_id]

  @classmethod
  def get_all(cls):
    return list(cls.users.values)
  
  @classmethod
  def create(cls, name, age):
    user_dict = {'name': name, 'age': age}
    max_id = max(cls.users.keys()) + 1
    cls.users[max_id] = user_dict

  @classmethod
  def update(cls, user_id, age):
    cls.users[user_id]['age'] = age

  @classmethod
  def delete(cls, user_id):
    if user_id in cls.users:
      return cls.users.pop(user_id)
