from django.urls import path

from enrollments.views import EnrollmentListCreate

urlpatterns = [
    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list-create'),
]
