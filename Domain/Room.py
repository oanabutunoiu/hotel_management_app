from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float
Base = declarative_base()


class Room(Base):
    __tablename__ = 'room'
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(Integer, unique=True, nullable=False)
    floor = Column(Integer, nullable=False)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    sea_view = Column(Boolean)

    def __str__(self):
        return(f'room_id: {self.room_id}\n'
               f'room_number: {self.room_number}\n'
               f'floor: {self.floor}\n'
               f'room_type: {self.room_type}\n'
               f'price_per_night: {self.price_per_night}\n'
               f'sea_view: {self.sea_view}')
