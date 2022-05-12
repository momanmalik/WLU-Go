from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import  Course, Rating, Professor, Professor_course
from .serializers import CourseSerializer, RatingSerializer, ProfessorSerializer, Professor_courseSerializer
from django_filters.rest_framework import DjangoFilterBackend

'''
class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the user item by that id
            try:
                # Check if the user item the user wants to update exists
                queryset = User.objects.get(email=id)
            except User.DoesNotExist:
                # If the user item does not exist, return an error response
                return Response({'errors': 'This user item does not exist.'}, status=400)

            # Serialize user item from Django queryset object to JSON formatted data
            read_serializer =  UserSerializer(queryset)

        else:
            # Get all user items from the database using Django's model ORM
            queryset = User.objects.all()

            # Serialize list of users item from Django queryset object to JSON formatted data
            read_serializer =  UserSerializer(queryset, many=True)

            # Return a HTTP response object with the list of user items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer =  UserSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new user item record in the database
            user_item_object = create_serializer.save()

            # Serialize the new user item from a Python object to JSON format
            read_serializer =  UserSerializer(user_item_object)

            # Return a HTTP response with the newly created user item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            user_item = User.objects.get(email=id)
        except User.DoesNotExist:
        # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # If the user item does exists, use the serializer to validate the updated data
        update_serializer =  UserSerializer(user_item, data=request.data)

        # If the data to update the user item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the user item in the database
            user_item_object = update_serializer.save()

            # Serialize the user item from Python object to JSON format
            read_serializer =  UserSerializer(user_item_object)

            # Return a HTTP response with the newly updated user item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            user_item = User.objects.get(user_id=id)
        except User.DoesNotExist:
            # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # Delete the chosen user item from the database
        user_item.delete()

        # Return a HTTP response notifying that the user item was successfully deleted
        return Response(status=204)

'''
# Course Table View Requests


class CourseListView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    many = True
    serializer_class =  CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code', 'course_id','name']
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the user item by that id
            try:
                # Check if the user item the user wants to update exists
                queryset = Course.objects.get(course_id=id)
            except Course.DoesNotExist:
                # If the user item does not exist, return an error response
                return Response({'errors': 'This user item does not exist.'}, status=400)

            # Serialize user item from Django queryset object to JSON formatted data
            read_serializer =  CourseSerializer(queryset)

        else:
            # Get all user items from the database using Django's model ORM
            queryset = Course.objects.all()

            # Serialize list of users item from Django queryset object to JSON formatted data
            read_serializer =  CourseSerializer(queryset, many=True)

            # Return a HTTP response object with the list of user items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer =  CourseSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new user item record in the database
            course_item_object = create_serializer.save()

            # Serialize the new user item from a Python object to JSON format
            read_serializer =  CourseSerializer(course_item_object)

            # Return a HTTP response with the newly created user item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            course_item = Course.objects.get(id=id)
        except Course.DoesNotExist:
        # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # If the user item does exists, use the serializer to validate the updated data
        update_serializer =  CourseSerializer(course_item, data=request.data)

        # If the data to update the user item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the user item in the database
            course_item_object = update_serializer.save()

            # Serialize the user item from Python object to JSON format
            read_serializer =  CourseSerializer(course_item_object)

            # Return a HTTP response with the newly updated user item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            course_item = Course.objects.get(user_id=id)
        except Course.DoesNotExist:
            # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # Delete the chosen user item from the database
        course_item.delete()

        # Return a HTTP response notifying that the user item was successfully deleted
        return Response(status=204)

# Rating Request


class RatingListView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class =  RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course_id', 'rating_id','user_id']
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the user item by that id
            try:
                # Check if the user item the user wants to update exists
                queryset = Rating.objects.get(rating_id=id)
            except Rating.DoesNotExist:
                # If the user item does not exist, return an error response
                return Response({'errors': 'This user item does not exist.'}, status=400)

            # Serialize user item from Django queryset object to JSON formatted data
            read_serializer =  RatingSerializer(queryset)

        else:
            # Get all user items from the database using Django's model ORM
            queryset = Rating.objects.all()

            # Serialize list of users item from Django queryset object to JSON formatted data
            read_serializer =  RatingSerializer(queryset, many=True)

            # Return a HTTP response object with the list of user items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer =  RatingSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new user item record in the database
            rating_item_object = create_serializer.save()

            # Serialize the new user item from a Python object to JSON format
            read_serializer =  RatingSerializer(rating_item_object)

            # Return a HTTP response with the newly created user item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            rating_item = Rating.objects.get(id=id)
        except Rating.DoesNotExist:
        # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # If the user item does exists, use the serializer to validate the updated data
        update_serializer =  RatingSerializer(rating_item, data=request.data)

        # If the data to update the user item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the user item in the database
            rating_item_object = update_serializer.save()

            # Serialize the user item from Python object to JSON format
            read_serializer =  RatingSerializer(rating_item_object)

            # Return a HTTP response with the newly updated user item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the user item the user wants to update exists
            rating_item = Rating.objects.get(rating_id=id)
        except Rating.DoesNotExist:
            # If the user item does not exist, return an error response
            return Response({'errors': 'This user item does not exist.'}, status=400)

        # Delete the chosen user item from the database
        rating_item.delete()

        # Return a HTTP response notifying that the user item was successfully deleted
        return Response(status=204)

# Add endpoints for the review table
'''
class ReviewListView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the review item by that id
            try:
                # Check if the review item the review wants to update exists
                queryset = Review.objects.get(review_id=id)
            except Review.DoesNotExist:
                # If the review item does not exist, return an error response
                return Response({'errors': 'This review item does not exist.'}, status=400)

            # Serialize review item from Django queryset object to JSON formatted data
            read_serializer =  ReviewSerializer(queryset)

        else:
            # Get all review items from the database using Django's model ORM
            queryset = Review.objects.all()

            # Serialize list of reviews item from Django queryset object to JSON formatted data
            read_serializer =  ReviewSerializer(queryset, many=True)

            # Return a HTTP response object with the list of review items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from review POST request to serializer for validation
        create_serializer =  ReviewSerializer(data=request.data)

        # Check if review POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If review data is valid, create a new review item record in the database
            review_item_object = create_serializer.save()

            # Serialize the new review item from a Python object to JSON format
            read_serializer =  ReviewSerializer(review_item_object)

            # Return a HTTP response with the newly created review item data
            return Response(read_serializer.data, status=201)

        # If the reviews POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the review item the review wants to update exists
            review_item = Review.objects.get(id=id)
        except Review.DoesNotExist:
        # If the review item does not exist, return an error response
            return Response({'errors': 'This review item does not exist.'}, status=400)

        # If the review item does exists, use the serializer to validate the updated data
        update_serializer =  ReviewSerializer(review_item, data=request.data)

        # If the data to update the review item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the review item in the database
            review_item_object = update_serializer.save()

            # Serialize the review item from Python object to JSON format
            read_serializer =  ReviewSerializer(review_item_object)

            # Return a HTTP response with the newly updated review item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the review item the review wants to update exists
            review_item = Review.objects.get(review_id=id)
        except Review.DoesNotExist:
            # If the review item does not exist, return an error response
            return Response({'errors': 'This review item does not exist.'}, status=400)

        # Delete the chosen review item from the database
        review_item.delete()

        # Return a HTTP response notifying that the review item was successfully deleted
        return Response(status=204)

'''

class ProfessorListView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class =  ProfessorSerializer
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the professor item by that id
            try:
                # Check if the professor item the professor wants to update exists
                queryset = Professor.objects.get(professor_id=id)
            except Professor.DoesNotExist:
                # If the professor item does not exist, return an error response
                return Response({'errors': 'This professor item does not exist.'}, status=400)

            # Serialize professor item from Django queryset object to JSON formatted data
            read_serializer =  ProfessorSerializer(queryset)

        else:
            # Get all professor items from the database using Django's model ORM
            queryset = Professor.objects.all()

            # Serialize list of professors item from Django queryset object to JSON formatted data
            read_serializer =  ProfessorSerializer(queryset, many=True)

            # Return a HTTP response object with the list of professor items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from professor POST request to serializer for validation
        create_serializer =  ProfessorSerializer(data=request.data)

        # Check if professor POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If professor data is valid, create a new professor item record in the database
            professor_item_object = create_serializer.save()

            # Serialize the new professor item from a Python object to JSON format
            read_serializer =  ProfessorSerializer(professor_item_object)

            # Return a HTTP response with the newly created professor item data
            return Response(read_serializer.data, status=201)

        # If the professors POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the professor item the professor wants to update exists
            professor_item = Professor.objects.get(id=id)
        except Professor.DoesNotExist:
        # If the professor item does not exist, return an error response
            return Response({'errors': 'This professor item does not exist.'}, status=400)

        # If the professor item does exists, use the serializer to validate the updated data
        update_serializer =  ProfessorSerializer(professor_item, data=request.data)

        # If the data to update the professor item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the professor item in the database
            professor_item_object = update_serializer.save()

            # Serialize the professor item from Python object to JSON format
            read_serializer =  ProfessorSerializer(professor_item_object)

            # Return a HTTP response with the newly updated professor item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the professor item the professor wants to update exists
            professor_item = Professor.objects.get(professor_id=id)
        except Professor.DoesNotExist:
            # If the professor item does not exist, return an error response
            return Response({'errors': 'This professor item does not exist.'}, status=400)

        # Delete the chosen professor item from the database
        professor_item.delete()

        # Return a HTTP response notifying that the professor item was successfully deleted
        return Response(status=204)



class Professor_courseListView(viewsets.ModelViewSet):
    queryset = Professor_course.objects.all()
    serializer_class =  Professor_courseSerializer
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the professor_course item by that id
            try:
                # Check if the professor_course item the professor_course wants to update exists
                queryset = Professor_course.objects.get(professor_course_id=id)
            except Professor_course.DoesNotExist:
                # If the professor_course item does not exist, return an error response
                return Response({'errors': 'This professor_course item does not exist.'}, status=400)

            # Serialize professor_course item from Django queryset object to JSON formatted data
            read_serializer =  Professor_courseSerializer(queryset)

        else:
            # Get all professor_course items from the database using Django's model ORM
            queryset = Professor_course.objects.all()

            # Serialize list of professor_courses item from Django queryset object to JSON formatted data
            read_serializer =  Professor_courseSerializer(queryset, many=True)

            # Return a HTTP response object with the list of professor_course items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from professor_course POST request to serializer for validation
        create_serializer =  Professor_courseSerializer(data=request.data)

        # Check if professor_course POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If professor_course data is valid, create a new professor_course item record in the database
            professor_course_item_object = create_serializer.save()

            # Serialize the new professor_course item from a Python object to JSON format
            read_serializer =  Professor_courseSerializer(professor_course_item_object)

            # Return a HTTP response with the newly created professor_course item data
            return Response(read_serializer.data, status=201)

        # If the professor_courses POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the professor_course item the professor_course wants to update exists
            professor_course_item = Professor_course.objects.get(id=id)
        except Professor_course.DoesNotExist:
        # If the professor_course item does not exist, return an error response
            return Response({'errors': 'This professor_course item does not exist.'}, status=400)

        # If the professor_course item does exists, use the serializer to validate the updated data
        update_serializer =  Professor_courseSerializer(professor_course_item, data=request.data)

        # If the data to update the professor_course item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the professor_course item in the database
            professor_course_item_object = update_serializer.save()

            # Serialize the professor_course item from Python object to JSON format
            read_serializer =  Professor_courseSerializer(professor_course_item_object)

            # Return a HTTP response with the newly updated professor_course item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the professor_course item the professor_course wants to update exists
            professor_course_item = Professor_course.objects.get(professor_course_id=id)
        except Professor_course.DoesNotExist:
            # If the professor_course item does not exist, return an error response
            return Response({'errors': 'This professor_course item does not exist.'}, status=400)

        # Delete the chosen professor_course item from the database
        professor_course_item.delete()

        # Return a HTTP response notifying that the professor_course item was successfully deleted
        return Response(status=204)
