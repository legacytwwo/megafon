from app import db

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Events(db.Model):
  __tablename__ = 'events'
  ##################
  id = db.Column(db.String(50), primary_key=True)
  ##################
  count = db.Column(db.Integer)
  service_type = db.Column(db.String(50))
  created_at = db.Column(db.DateTime(timezone=False))
  ##################
  user_id = db.Column(db.String(50), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
  @property
  def label(self):
    return self.count
  def dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

class EventsScheme(BaseModel):
  id: Optional[str]
  count: Optional[int]
  user_id: Optional[str]
  service_type: Optional[str]
  created_at: Optional[datetime]
  class Config: orm_mode = True