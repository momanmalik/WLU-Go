from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
# ORM 
class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length = 8)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    department = models.CharField(max_length = 20)

class Rating(models.Model):
    rating_id = models.CharField(primary_key=True, max_length=60, editable=False)
    user_id = models.CharField(max_length=60)
    course_id = models.CharField(max_length=60)
    birdness = models.IntegerField()
    usefulness = models.IntegerField()
    enjoyability = models.IntegerField()
    grade = models.CharField(max_length = 3)
    mean_user_score = models.IntegerField()
    term_taken = models.CharField(max_length=20)
    review = models.TextField(default='')

class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)

class Professor_course(models.Model):
    professor_id = models.UUIDField()
    course_id =  models.UUIDField()

