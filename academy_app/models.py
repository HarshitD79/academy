from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    is_instructor = models.BooleanField(default=False)
    
# category model
class category(models.Model):
    name = models.CharField(max_length=50)



# MUSIC Model
class music(models.Model):
    title = models.CharField(max_length=50)
    duration = models.TimeField()
    artist = models.CharField(max_length=50)
    language = models.CharField(max_length=50)


# CAR Model
class car(models.Model):
    fuel_choices = [
        ('cng', 'cng'),
        ('petrol', 'petrol'),
        ('diesel', 'diesel'),
    ]
    color_choices = [
        ('blue', 'blue'),
        ('white', 'white'),
        ('black', 'black'),
    ]
    brand = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50, choices=fuel_choices)
    model_year = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    color = models.CharField(max_length=50, choices=color_choices)


# LAPTOP Model
class laptop(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    ram = models.IntegerField()
    storage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    os = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# MOBILE Model

class mobile(models.Model):
    color_choices = [
            ('silver', 'silver'),
            ('white', 'white'),
            ('grey', 'grey'),
            ('rosegold', 'rosegold'),
        ]
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    os = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    color = models.CharField(max_length=50,choices=color_choices)


#  --------------------------------------------- -------------------------------------------
# Inquiry Model
class Inquiry(models.Model):
    education = [
        ('bca', 'bca'),
        ('mca', 'mca'),
        ('cse', 'cse'),
        ('diploma', 'diploma'),
    ]

    course = [
        ('mern stack', 'mern stack'),
        ('full stack', 'full stack'),
        ('artificial intelligence', 'artificial intelligence'),
        ('machine learning', 'machine learning'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    level_of_education = models.CharField(max_length=100,choices=education)
    course_interested = models.CharField(max_length=100,choices=course)
    is_subscribe = models.BooleanField(default=False)


# ----------------------------------------------- -----------------------------------------




# Contact Us Model
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    subject = models.TextField()
    message = models.TextField()



# Course Model
class Course(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    overview = models.TextField()
    learn = models.TextField()
    content = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(category,on_delete=models.PROTECT)
    course_level = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_lectures = models.CharField(max_length=100)
    course_quizzes = models.CharField(max_length=100)
    course_language = models.CharField(max_length=100)
    course_assessments = models.BooleanField()
    course_certificate = models.BooleanField()
