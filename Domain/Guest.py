from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
Base = declarative_base()


class Guest(Base):
    __tablename__ = 'guest'
    guest_id = Column(Integer, primary_key=True, autoincrement=True)
    identification_number = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    email = Column(String, nullable=False)

    def __str__(self):
        return(f'room_id: {self.guest_id}\n'
               f'room_number: {self.identification_number}\n'
               f'floor: {self.first_name}\n'
               f'room_type: {self.last_name}\n'
               f'price_per_night: {self.birth_date}\n'
               f'sea_view: {self.email}')
