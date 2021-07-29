from django.db import models
import uuid
# Create your models here.


class Rating(models.Model):
    rating_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birdness = models.IntegerField()
    usefulness = models.IntegerField()
    enjoyability = models.IntegerField()

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length = 5)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    department = models.CharField(max_length = 20)
    rating_id = models.ForeignKey(Rating, on_delete = models.CASCADE) 
    score = models.FloatField()
    mean_grade = models.FloatField()

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

class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Professor_course(models.Model): 
    professor_id = models.ForeignKey(Professor, on_delete = models.CASCADE) 
    course_id =models.ForeignKey(Course, on_delete = models.CASCADE) 


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE) 
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE) 
    body = models.TextField()
    rating_id = models.ForeignKey(Rating, on_delete = models.CASCADE) 
    grade = models.IntegerField()
    professor_id = models.ForeignKey(Professor, on_delete = models.CASCADE) 
    term_taken = models.CharField(max_length=20)
    date_time_created = models.DateTimeField()
