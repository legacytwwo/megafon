from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app import app, db
from models.core import *
from lib.flask import jsonify, request

@app.route('/api/users', methods=['GET'])
def route_get_users():
  try:
    params = request.json
    query = db.session.query(Users)
    if params:
      query = query.filter(Users.id == params['id'])
    query_result = query.all()
    answer = []
    for x in query_result:
      answer.append(x.dict())
    return jsonify({'status': answer})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/users', methods=['POST'])
def route_post_users():
  try:
    params = request.json

    try:
      user = UsersScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    user.id = str(uuid4())
    user.created_at = datetime.now()
    record = Users(**user.dict())

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()

    return jsonify(record.dict())
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/users', methods=['PUT'])
def route_put_users():
  try:
    params = request.json
    if not params['id']:
      return jsonify({'status': 'id not received'})
    try:
      user = UsersScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    record = Users(**params)

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/users', methods=['DELETE'])
def route_delete_users():
  try:
    params = request.json
    Users.query.filter(Users.id == params['id']).delete()
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})