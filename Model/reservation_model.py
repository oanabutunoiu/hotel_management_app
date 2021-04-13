from sqlalchemy.orm import sessionmaker

from Domain.Reservation import Reservation


class ReservationSQLModel:
    def __init__(self, engine):
        self.__engine = engine
        self.__session = sessionmaker(bind=engine)()

    def create_reservation(self, room_id, guest_id, reservation_date, arrive_date, leave_date, breakfast,
                           parking, total_price):
        self.__session.add(
            Reservation(room_id=room_id, guest_id=guest_id, reservation_date=reservation_date, arrive_date=arrive_date,
                        leave_date=leave_date, breakfast=breakfast, parking=parking, total_price=total_price)
        )

    def read_reservations(self):
        return self.__session.query(Reservation).all()

    def update_reservation(self, reservation_id, room_id=None, guest_id=None, arrive_date=None, leave_date=None,
                           breakfast=None, parking=None, total_price=None):
        reservation = self.__session.query(Reservation).filter_by(reservation_id=reservation_id).first()
        if reservation:
            self.__session.query(Reservation).filter_by(reservation_id=reservation_id).update({
                'room_id': room_id or reservation.room_id,
                'guest_id': guest_id or reservation.guest_id,
                'arrive_date': arrive_date or reservation.arrive_date,
                'leave_date': leave_date or reservation.leave_date,
                'breakfast': breakfast or reservation.breakfast,
                'parking': parking or reservation.parking,
                'total_price': total_price or reservation.total_price,

            })
            self.__session.commit()

    def delete_reservation(self, identification_number):
        self.__session.query(Reservation).filter_by(identification_number=identification_number).delete()
        self.__session.commit()

    def find_by_number(self, identification_number):
        reservation = self.__session.query(Reservation).filter_by(identification_number=identification_number).first()
        return reservation

    def reservation_exists(self, identification_number):
        reservation = self.__session.query(Reservation).filter_by(identification_number=identification_number).first()
        return True if reservation else False
