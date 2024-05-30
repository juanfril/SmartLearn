from django import forms

from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

    def save(self, commit: bool = True) -> Course:
      course: Course = super().save(commit=False)
      if commit:
        course.save()
      return course
