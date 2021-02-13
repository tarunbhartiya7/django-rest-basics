from django.urls import include, path
from rest_framework import routers
from firstProject.cbvApp import views as student_view
from firstProject.nestedApp import views as literature_view

router = routers.DefaultRouter()
router.register('author', literature_view.AuthorViewSet)
router.register('book', literature_view.BookViewSet)
router.register('students', student_view.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
