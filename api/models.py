from django.db import models


ZODIAC_SIGNS = {
    1: {20: 'Capricorn', 21: 'Aquarius'},
    2: {19: 'Aquarius', 20: 'Pisces'},
    3: {20: 'Pisces', 21: 'Aries'},
    4: {20: 'Aries', 21: 'Taurus'},
    5: {21: 'Taurus', 22: 'Gemini'},
    6: {21: 'Gemini', 22: 'Cancer'},
    7: {22: 'Cancer', 24: 'Leo'},
    8: {23: 'Leo', 24: 'Virgo'},
    9: {23: 'Virgo', 24: 'Libra'},
    10: {23: 'Libra', 24: 'Scorpio'},
    11: {22: 'Scorpio', 23: 'Sagittarius'},
    12: {21: 'Sagittarius', 22: 'Capricorn'}
}


class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return f'{self.city} {self.street} {self.building} apartment:{self.apartment}'


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.ManyToManyField(Address, blank=True)
    date_of_birth = models.DateField()
    zodiac_sing = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        zodiac_keys = [k for k in ZODIAC_SIGNS[self.date_of_birth.month].keys()]
        if self.date_of_birth.day <= zodiac_keys[0]:
            self.zodiac_sing = ZODIAC_SIGNS[self.date_of_birth.month][zodiac_keys[0]]
        else:
            self.zodiac_sing = ZODIAC_SIGNS[self.date_of_birth.month][zodiac_keys[1]]
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name
