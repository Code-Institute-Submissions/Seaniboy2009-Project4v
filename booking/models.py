from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Awaiting"), (1, "Approved"))

BOOKING_TIMES = (
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
)

TABLE_SEATS = (
    ('2', '2'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.stars.count()


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booked = models.BooleanField(default=False)
    num_seats = models.CharField(max_length=10, choices=TABLE_SEATS, default='2')
    time = models.CharField(max_length=10, choices=BOOKING_TIMES, default='8:00')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Table number {self.table_number}"
