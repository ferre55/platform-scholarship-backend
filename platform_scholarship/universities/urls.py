from django.urls import path
from universities import views

urlpatterns =[
    path('',views.UniversityView.as_view()),
    path('<int:id>',views.UniversitySingleView.as_view())

]
    