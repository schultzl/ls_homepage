from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("project_index/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    path("papers/<int:pk>/", views.job_detail, name="papers_detail"),
    path("contact/", views.contact, name="contact"),
    path('redirect/', views.project_index),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name="privacy"),
    path('license/', TemplateView.as_view(template_name='license.html'), name="license"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    #path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
] 