from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=200)


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    @property
    def previous_reservation_id(self):
        previous_reservation_list = self.__class__.objects.filter(
            checkout__lte=self.checkin, rental=self.rental
        ).order_by("-checkout")
        return previous_reservation_list.first().id if previous_reservation_list else "-"
