from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    path("papers/<int:pk>/", views.job_detail, name="papers_detail"),
    path("contact", views.contact, name="contact"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
] 