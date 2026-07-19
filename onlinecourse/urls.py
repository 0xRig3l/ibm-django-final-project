from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
                  # route is a string contains a URL pattern
                  # view refers to the view function
                  # name the URL
                  path(route='', view=views.CourseListView.as_view(), name='index'),
                  path('signup/', views.signup_request, name='signup'),
                  path('login/', views.login_request, name='login'),
                  path('logout/', views.logout_request, name='logout'),
                  # ex: /course/5/
                  path('course/<uuid:pk>/', views.CourseDetailsView.as_view(), name='course_details'),
                  # ex: /course/5/enroll/
                  path('course/<uuid:course_id>/enroll/', views.enroll, name='enroll'),
                  path('course/<uuid:course_id>/submit/', views.submit, name='submit'),
                  path('course/<uuid:course_id>/submission/<uuid:submission_id>/result/', views.show_exam_result,
                       name='exam_result'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
