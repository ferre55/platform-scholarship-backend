from django.urls import path
from scholars import views

urlpatterns =[
    path('',views.ScholarView.as_view()),
    path('<int:id>',views.ScholarSingleView.as_view())

]
    