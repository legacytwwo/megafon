# megafon
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
  "id": <insert product id>,
  "name": "New_Maximum"
}
  
GET /api/tariffs 
{
  "id": <insert product id>
}
  
OR send request without a body to get all tariffs
  
DELETE /api/tariffs 
{
  "id": <insert product id>
}
