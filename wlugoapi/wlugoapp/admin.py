from django.contrib import admin

admin.site.site_header = 'WLU GO DB Administration'
# Register your models here.
from .models import Rating 
from .models import Course
from .models import User
from .models import Professor
from .models import Professor_course
from .models import Review

# this class define which department columns will be shown in the department admin web site.
class UserAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['user_id','email','password','first_name','last_name','program',
    'graduating_year','has_access','is_mod','is_admin']

admin.site.register(User, UserAdmin)

# this class define which department columns will be shown in the department admin web site.
class RatingAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['rating_id','birdness','usefulness','enjoyability']

admin.site.register(Rating, RatingAdmin)

# this class define which department columns will be shown in the department admin web site.
class CourseAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['course_id','code','name','description','department','rating_id', 'score',
    'mean_grade']

admin.site.register(Course, CourseAdmin)

# this class define which department columns will be shown in the department admin web site.
class ReviewAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['review_id','user_id','course_id','body','rating_id','grade','professor_id',
        'term_taken','date_time_created']

admin.site.register(Review, ReviewAdmin)

# this class define which department columns will be shown in the department admin web site.
class ProfessorAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['professor_id','first_name','last_name']

admin.site.register(Professor, ProfessorAdmin)

# this class define which department columns will be shown in the department admin web site.
class Professor_courseAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['professor_id','course_id']

admin.site.register(Professor_course, Professor_courseAdmin)