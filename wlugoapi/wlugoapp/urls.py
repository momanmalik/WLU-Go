from django.urls import path

from . import views


urlpatterns = [
  path('users/', views.UserListView.as_view()),
  path('courses/', views.CourseListView.as_view()),
  path('ratings/', views.RatingListView.as_view()),
  path('reviews/', views.ReviewListView.as_view()),
  path('professors/', views.ProfessorListView.as_view()),
  path('professor_course/', views.Professor_courseListView.as_view()),
]