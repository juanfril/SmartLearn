from typing import List
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models import Course

def course_list(request: HttpRequest) -> HttpResponse:
  courses: List[Course] = Course.objects.all()
  return render(request, 'courses/course_list.html', {'coursesa': courses})

class CourseGenerationView(APIView):
  def post(self, request: HttpRequest) -> Response:
    topic: str = request.data.get('topic')
    if not topic:
      return Response({"error": "Topic is required"}, status=status.HTTP_400_BAD_REQUEST)

    course_outline: str = "Mock course outline for " + topic
    return Response({"course_outline": course_outline}, status=status.HTTP_200_OK)
