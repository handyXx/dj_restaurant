from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NUMBER_RESERVATION_PEOPLE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (5, 6),
    (7, 7),
)

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = PhoneNumberField()
    date = models.DateField()
    person_num = models.PositiveIntegerField(
        default=1,
        choices=NUMBER_RESERVATION_PEOPLE
    )
    time = models.TimeField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
