from django.urls import path
from courses.views import CoursesApiView, CourseApiView, ReviewsApiView, ReviewApiView, CoursesApiViewSets, ReviewsApiViewSets

from rest_framework.routers import SimpleRouter


urlpatterns = [
    # CURSOS / v1
    path('courses/', CoursesApiView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseApiView.as_view(), name='course'),

    path('courses/<int:course_pk>/reviews/', ReviewsApiView.as_view(), name='course reviews'),
    path('courses/<int:course_pk>/reviews/<int:review_pk>/', ReviewApiView.as_view(), name='course review'),
    
    # AVALIAÇÕES / v1
    path('reviews/', ReviewsApiView.as_view(), name='reviews'),
    path('reviews/<int:review_pk>/', ReviewApiView.as_view(), name='review'),
]


router = SimpleRouter()
# CURSOS / V2
router.register('courses', CoursesApiViewSets)

# AVALIAÇÕES / V2
router.register('reviews', ReviewsApiViewSets)
