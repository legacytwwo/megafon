from app import db

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Users(db.Model):
  __tablename__ = 'users'
  ##################
  id = db.Column(db.String(50), primary_key=True)
  ##################
  age = db.Column(db.Integer)
  city = db.Column(db.String(50))
  balance = db.Column(db.String(50))
  created_at = db.Column(db.DateTime(timezone=False))
  last_activity = db.Column(db.DateTime(timezone=False))
  ##################
  events = db.relationship('Events', lazy='noload', foreign_keys='[Events.user_id]', order_by='Events.created_at.asc()')
  ##################
  active_tariff_id = db.Column(db.String(50), db.ForeignKey('tariffs.id'))
  active_tariff = db.relationship('Tariffs', lazy='noload', uselist=False, foreign_keys=[active_tariff_id])
  @property
  def label(self):
    return self.age
  def dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

class UsersScheme(BaseModel):
  id: Optional[str]
  age: Optional[int]
  city: Optional[str]
  balance: Optional[str]
  created_at: Optional[datetime]
  active_tariff_id: Optional[str]
  last_activity: Optional[datetime]
  class Config: orm_mode = True
