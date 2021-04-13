from sqlalchemy.orm import sessionmaker

from Domain.Room import Room


class RoomSQLModel:
    def __init__(self, engine):
        self.__engine = engine
        self.__session = sessionmaker(bind=engine)()

    def create_room(self, room_number, floor, room_type, price_per_night, sea_view):
        self.__session.add(
            Room(room_number=room_number, floor=floor, room_type=room_type, price_per_night=price_per_night,
                 sea_view=sea_view)
        )
        self.__session.commit()

    def read_rooms(self):
        return self.__session.query(Room).all()

    def update_room(self, room_number, room_type=None, price_per_night=None):
        room = self.__session.query(Room).filter_by(room_number=room_number).first()
        if room:
            self.__session.query(Room).filter_by(room_number=room_number).update({
                'room_type': f'{room_type or room.room_type}',
                'price_per_night': price_per_night or room.price_per_night
            })
            self.__session.commit()

    def delete_room(self, room_number):
        self.__session.query(Room).filter_by(room_number=room_number).delete()
        self.__session.commit()

    def find_by_number(self, room_number):
        room = self.__session.query(Room).filter_by(room_number=room_number).first()
        return room

    def room_exists(self, room_number):
        room = self.__session.query(Room).filter_by(room_number=room_number).first()
        return True if room else False
