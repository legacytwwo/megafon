from app import app
from lib.flask import jsonify

@app.route('/api/ping', methods=['GET'])
def route_ping():
  return jsonify({'status': True})