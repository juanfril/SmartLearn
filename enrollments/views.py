from rest_framework import generics

from enrollments.models import Enrollment
from enrollments.serializers import EnrollmentSerializer

class EnrollmentListCreate(generics.ListCreateAPIView):
  queryset = Enrollment.objects.all()
  serializer_class = EnrollmentSerializer
