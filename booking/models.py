from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Awaiting"), (1, "Approved"))

TABLE_SEATS = (
    (2, '2'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)

COURSE_SELECTION = (
    ('main', 'main'),
    ('starter', 'starter'),
    ('side', 'side'),
    ('desert', 'desert'),
)

TIME_SLOTS = (
    (datetime.time(10, 00, 00), u'10 AM'),
    (datetime.time(11, 00, 00), u'11 AM'),
    (datetime.time(12, 00, 00), u'12 AM'),
    (datetime.time(13, 00, 00), u'1 PM'),
    (datetime.time(14, 00, 00), u'2 PM'),
    (datetime.time(15, 00, 00), u'3 PM'),
    (datetime.time(16, 00, 00), u'4 PM'),
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
    created_on = models.DateTimeField(auto_now_add=True)
    num_seats = models.IntegerField(default=2, choices=TABLE_SEATS)
    num_of_bookings = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Table number {self.table_number}"
    
    def add_num_of_bookings(self):
        self.num_of_bookings += 1
    
    def remove_num_of_bookings(self):
        self.num_of_bookings -= 1


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    booking_time = models.TimeField(choices=TIME_SLOTS)
    booking_date = models.DateField(default=datetime.date.today)
    number_of_guests = models.IntegerField(default=2, choices=TABLE_SEATS)
    booked_on = models.DateTimeField(auto_now_add=True)
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booked_by"
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"Booking number {self.id}"


class MenuItem(models.Model):
    name = models.CharField(max_length=20, default='menu item')
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, default='menu item')
    price = models.IntegerField(default=10)
    img = CloudinaryField('image', default='placeholder')
    course = models.CharField(max_length=20, choices=COURSE_SELECTION, default='main')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
