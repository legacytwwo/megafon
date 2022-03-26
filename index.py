from app import app, db
from routers.core import *

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4020, debug=True)