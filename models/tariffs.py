from app import db

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Tariffs(db.Model):
  __tablename__ = 'tariffs'
  ##################
  id = db.Column(db.String(50), primary_key=True)
  ##################
  name = db.Column(db.String(50))
  volume_sms = db.Column(db.Integer)
  volume_traffic = db.Column(db.Integer)
  volume_minutes = db.Column(db.Integer)
  started_at = db.Column(db.DateTime(timezone=False))
  expired_at = db.Column(db.DateTime(timezone=False))
  ##################
  @property
  def label(self):
    return self.name
  def dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

class TariffsScheme(BaseModel):
  id: Optional[str]
  name: Optional[str]
  volume_sms: Optional[int]
  volume_traffic: Optional[int]
  volume_minutes: Optional[int]
  expired_at: Optional[datetime]
  started_at: Optional[datetime]
  class Config: orm_mode = True