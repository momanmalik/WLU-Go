from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=20)
    password =  models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    graduating_year = models.IntegerField()
    has_access = models.BooleanField()
    is_mod = models.BooleanField()
    is_admin = models.BooleanField()

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length = 8)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    department = models.CharField(max_length = 20)

class Rating(models.Model):
    rating_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE) 
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE) 
    birdness = models.IntegerField()
    usefulness = models.IntegerField()
    enjoyability = models.IntegerField()
    grade = models.CharField(max_length = 3)
    mean_user_score = models.FloatField()
    term_taken = models.CharField(max_length=20)
    date_time_created = models.DateTimeField()

class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)

class Professor_course(models.Model): 
    professor_id = models.ForeignKey(Professor, on_delete = models.CASCADE) 
    course_id =models.ForeignKey(Course, on_delete = models.CASCADE) 

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE) 
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE) 
    rating_id = models.ForeignKey(Rating, on_delete = models.CASCADE) 
    body = models.TextField()
    date_time_created = models.DateTimeField()