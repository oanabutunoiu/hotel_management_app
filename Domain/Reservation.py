from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, Float
from Domain.Room import Room
from Domain.Guest import Guest
Base = declarative_base()


class Reservation(Base):
    __tablename__ = 'reservation'
    reservation_id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.room_id), nullable=False)
    guest_id = Column(Integer, ForeignKey(Guest.guest_id), nullable=False)
    reservation_date = Column(Date)
    arrive_date = Column(Date, nullable=False)
    leave_date = Column(Date, nullable=False)
    breakfast = Column(Boolean)
    parking = Column(Boolean)
    total_price = Column(Float, nullable=False)
