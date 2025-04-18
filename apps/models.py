from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DecimalField, TextField, ImageField, CASCADE, ForeignKey, BooleanField, \
    PositiveIntegerField


class User(AbstractUser):
    pass


class Category(Model):
    name = CharField(max_length=100)


class Product(Model):
    name = CharField(max_length=100)
    price = DecimalField(decimal_places=2, max_digits=10)
    discount_price = DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    short_description = TextField()
    long_description = TextField()
    image = ImageField(upload_to='products/images/')
    stock = PositiveIntegerField(default=0)
    is_available = BooleanField(default=True)
    category = ForeignKey(Category, CASCADE, related_name='products')
    tags = CharField(max_length=255, blank=True, help_text="Taglarni vergul bilan ajrating (e.g. summer,new)")

    def get_final_price(self):
        return self.discount_price if self.discount_price else self.price

    def __str__(self):
        return f"{self.name} - ${self.get_final_price()}"
