from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Rating, Professor, Professor_course
from django.contrib.auth.hashers import make_password

'''
class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    email = serializers.CharField()
    password =  serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    program = serializers.CharField()
    graduating_year = serializers.IntegerField()
    has_access = serializers.BooleanField()
    is_mod = serializers.BooleanField()
    is_admin = serializers.BooleanField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return User.objects.create(
            user_id = validated_data.get('user_id'),
            email = validated_data.get('email'),
            password = validated_data.get('password'),
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            program = validated_data.get('program'),
            graduating_year = validated_data.get('graduating_year'),
            has_access = validated_data.get('has_access'),
            is_mod = validated_data.get('is_mod'),
            is_admin = validated_data.get('is_admin')
    )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
        'user_id',
        'email',
        'password',
        'first_name',
        'last_name',
        'program',
        'graduating_year',
        'has_access',
        'is_mod',
        'is_admin'
    )
'''

class CourseSerializer(serializers.ModelSerializer):
    course_id = serializers.UUIDField()
    code = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    department = serializers.CharField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
            return Course.objects.create(
            course_id =  validated_data.get('course_id'),
            code = validated_data.get('code'),
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            department = validated_data.get('department'),

            )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance

    class Meta:
        model = Course
        fields = (
        'course_id',
        'code',
        'name',
        'description',
        'department',
    )

class RatingSerializer(serializers.ModelSerializer):
    rating_id = serializers.CharField()
    user_id = serializers.CharField()
    course_id = serializers.CharField()
    birdness = serializers.IntegerField()
    usefulness = serializers.IntegerField()
    enjoyability = serializers.IntegerField()
    grade =  serializers.CharField()
    mean_user_score = serializers.IntegerField()
    term_taken = serializers.CharField()
    review = serializers.CharField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return Rating.objects.create(
            rating_id = validated_data.get('rating_id'),
            user_id = validated_data.get('user_id'),
            course_id = validated_data.get('course_id'),
            birdness = validated_data.get('birdness'),
            usefulness = validated_data.get('usefulness'),
            enjoyability = validated_data.get('enjoyability'),
            grade = validated_data.get('grade'),
            mean_user_score = validated_data.get('mean_user_score'),
            review =validated_data.get('review'),
            term_taken = validated_data.get('term_taken'),
    )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.birdness = validated_data.get('birdness',instance.birdness ),
        instance.usefulness = validated_data.get('usefulness',instance.usefulness),
        instance.enjoyability = validated_data.get('enjoyability',instance.enjoyability),
        instance.grade = validated_data.get('grade',instance.grade),
        instance.mean_user_score = validated_data.get('mean_user_score',instance.mean_user_score),
        instance.term_taken = validated_data.get('term_taken',instance.term_taken),
        instance.review = validated_data.get('review',instance.review),
        instance.save()
        return instance

    class Meta:
        model = Rating
        fields = (
            'rating_id',
            'user_id',
            'course_id',
            'birdness',
            'usefulness',
            'enjoyability',
            'grade',
            'mean_user_score',
            'term_taken',
            'review',
    )
'''
class ReviewSerializer(serializers.ModelSerializer):
    review_id = serializers.UUIDField()
    user_id = User.user_id
    course_id = Course.course_id
    rating_id = Rating.rating_id
    body = serializers.CharField()
    date_time_created = serializers.DateTimeField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return Review.objects.create(
            review_id = validated_data.get('review_id'),
            user_id = validated_data.get('user_id'),
            course_id = validated_data.get('course_id'),
            rating_id = validated_data.get('rating_id'),
            body = validated_data.get('body'),
            date_time_created = validated_data.get('date_time_created')
        )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.body = validated_data.get('body',instance.enjoyability),
        instance.date_time_created = validated_data.get('date_time_created',instance.date_time_created)
        instance.save()
        return instance

    class Meta:
        model = Review
        fields = (
        'review_id',
        'user_id',
        'course_id',
        'rating_id',
        'body',
        'date_time_created'
    )
'''

class ProfessorSerializer(serializers.ModelSerializer):
    professor_id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return Professor.objects.create(
            professor_id = validated_data.get('professor_id'),
            name = validated_data.get('name'),
        )
    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.professor_id = validated_data.get('professor_id',instance.professor_id),
        instance.name = validated_data.get('name',instance.name),
        instance.save()
        return instance

    class Meta:
        model = Professor
        fields = (
            'professor_id',
            'name',
        )

class Professor_courseSerializer(serializers.ModelSerializer):
    professor_id = serializers.UUIDField()
    course_id =  serializers.UUIDField()

    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return Professor_course.objects.create(
            professor_id = validated_data.get('professor_id'),
            course_id = validated_data.get('course_id')
    )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.professor_id = validated_data.get('professor_id', instance.professor_id)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.save()
        return instance

    class Meta:
        model = Professor_course
        fields = (
            'professor_id',
            'course_id',
    )




'''
{
"user_id":98765,
"email" : "testuser@gmail.com",
"password" : "password",
"first_name" : "tester1",
"last_name" : "tester1",
"program" : "Comp Sci",
"graduating_year" : 2098,
"has_access" : "True",
"is_mod" : "False",
"is_admin  : "False"
}
'''
