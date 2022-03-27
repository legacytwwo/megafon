# megafon
2 задача. Создать REST-сервис со встраиваемой БД (Например, Датафрейм или SQLite). Сервис должен предоставлять

возможность вставки, чтения, удаления и изменения данных в этом хранилище данных. Используемый стек ничем не ограничен.

Sqlite is used as db. Id is generated automatically with uuid4.

Start with 'python3 -m venv modules'

And 'pip3 install --upgrade -r install.txt'

The server is activated with 'python index.py'

Testing with Postman:

POST /api/tariffs 
{
  "name": "Maximum",
  "volume_minutes": 800,
  "volume_sms": 500,
  "volume_traffic": 16384,
  "started_at": "2022-03-26 00:00:00.000000",
  "expired_at": "2030-03-26 00:00:00.000000"
}

PUT /api/tariffs 
{
  "id": "insert your tariff id",
  "name": "New_Maximum"
}
  
GET /api/tariffs 
{
  "id": "insert your tariff id"
}
  
OR send request without a body to get all tariffs
  
DELETE /api/tariffs 
{
  "id": "insert your tariff id"
}
