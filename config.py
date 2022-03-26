
def config(value):
  return Configuration.__dict__[value]

def get_string_db():
  return 'sqlite:///db/megafon-sqlite.db'

class Configuration(object):
  ################################
  SEND_FILE_MAX_AGE_DEFAULT = 0
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SQLALCHEMY_DATABASE_URI = get_string_db()
  ################################