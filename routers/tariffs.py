from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app import app, db
from models.core import *
from lib.flask import jsonify, request

@app.route('/api/tariffs', methods=['GET'])
def route_get_tariffs():
  try:
    params = request.json
    query = db.session.query(Tariffs)
    if params:
      query = query.filter(Tariffs.id == params['id'])
    query_result = query.all()
    answer = []
    for x in query_result:
      answer.append(x.dict())
    return jsonify({'status': answer})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/tariffs', methods=['POST'])
def route_post_tariffs():
  try:
    params = request.json

    try:
      tariff = TariffsScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    tariff.id = str(uuid4())
    record = Tariffs(**tariff.dict())

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()

    return jsonify(record.dict())
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/tariffs', methods=['PUT'])
def route_put_tariffs():
  try:
    params = request.json
    if not params['id']:
      return jsonify({'status': 'id not received'})
    try:
      tariff = TariffsScheme(**params)
    except ValidationError as err:
      return jsonify(err.json())

    record = Tariffs(**params)

    record = db.session.merge(record)
    db.session.flush()
    db.session.refresh(record)
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})

@app.route('/api/tariffs', methods=['DELETE'])
def route_delete_tariffs():
  try:
    params = request.json
    Tariffs.query.filter(Tariffs.id == params['id']).delete()
    db.session.commit()
    return jsonify({'status': True})
  except Exception as err:
    return jsonify({'status': 'Error'})