from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app import app, db
from models.core import *
from lib.flask import jsonify, request

@app.route('/api/events', methods=['GET'])
def route_get_events():
  try:
    params = request.json
    query = db.session.query(Events)
    if params:
      query = query.filter(Events.id == params['id'])
    query_result = query.all()
    answer = []
    for x in query_result:
      answer.append(x.dict())
    return jsonify({'status': answer})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/events', methods=['POST'])
def route_post_events():
  try:
    params = request.json

    try:
      event = EventsScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    event.id = str(uuid4())
    event.created_at = datetime.now()
    record = Events(**event.dict())

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()

    return jsonify(record.dict())
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/events', methods=['PUT'])
def route_put_events():
  try:
    params = request.json
    if not params['id']:
      return jsonify({'status': 'id not received'})
    try:
      event = EventsScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    record = Events(**params)

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/events', methods=['DELETE'])
def route_delete_events():
  try:
    params = request.json
    Events.query.filter(Events.id == params['id']).delete()
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})