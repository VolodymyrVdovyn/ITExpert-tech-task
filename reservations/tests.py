import pytest

from reservations.models import Rental, Reservation

pytestmark = pytest.mark.django_db


@pytest.fixture
def rental():
    return Rental.objects.create(name="Rental-test")


@pytest.fixture
def create_reservation(rental):
    def reservation(checkin, checkout):
        return Reservation.objects.create(rental=rental, checkin=checkin, checkout=checkout)

    return reservation


class TestReservation:
    @staticmethod
    def test_previous_reservation_exist(create_reservation):
        previous_reservation = create_reservation("2022-01-01", "2022-01-13")
        current_reservation = create_reservation("2022-01-20", "2022-02-10")
        assert current_reservation.previous_reservation_id == previous_reservation.id

    @staticmethod
    def test_previous_reservation_not_exist(create_reservation):
        current_reservation = create_reservation("2022-01-20", "2022-02-10")
        assert current_reservation.previous_reservation_id == "-"
