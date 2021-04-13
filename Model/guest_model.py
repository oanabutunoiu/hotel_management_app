from sqlalchemy.orm import sessionmaker

from Domain.Guest import Guest


class GuestSQLModel:
    def __init__(self, engine):
        self.__engine = engine
        self.__session = sessionmaker(bind=engine)()

    def create_guest(self, identification_number, first_name, last_name, birth_date, email):
        self.__session.add(
            Guest(identification_number=identification_number, first_name=first_name, last_name=last_name,
                  birth_date=birth_date,
                  email=email)
        )
        self.__session.commit()

    def read_guests(self):
        return self.__session.query(Guest).all()

    def update_guest(self, identification_number, first_name=None, last_name=None, email=None):
        guest = self.__session.query(Guest).filter_by(identification_number=identification_number).first()
        if guest:
            self.__session.query(Guest).filter_by(identification_number=identification_number).update({
                'first_name': f'{first_name or guest.first_name}',
                'last_name': f'{last_name or guest.last_name}',
                'email': f'{email or guest.email}'
            })
            self.__session.commit()

    def delete_guest(self, identification_number):
        self.__session.query(Guest).filter_by(identification_number=identification_number).delete()
        self.__session.commit()

    def find_by_number(self, identification_number):
        guest = self.__session.query(Guest).filter_by(identification_number=identification_number).first()
        return guest

    def guest_exists(self, identification_number):
        guest = self.__session.query(Guest).filter_by(identification_number=identification_number).first()
        return True if guest else False
