from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ()


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ()


class Hotel(models.Model):

    CATEGORY_HOSPEDAGEM = 'hospedagem'
    CATEGORY_APARTAMENTO = 'apartamento'
    CATEGORY_HOSTEL = 'hostel'

    CATEGORY_CHOICES = (
        (CATEGORY_HOSPEDAGEM, 'Hospedagem'),
        (CATEGORY_APARTAMENTO, 'Apartamento'),
        (CATEGORY_HOSTEL, 'Hostel'),
    )

    name = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ()


class Vitrine(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    itens = models.ManyToManyField(Hotel)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ()
