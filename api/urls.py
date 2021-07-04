from django.urls import path
from api.views import ProjectList,ProjectDetail
urlpatterns = [
    path('prjects/', ProjectList.as_view()),
    path('delete-prjects/<int:pk>/', ProjectDetail.as_view()),
]