from django.urls import path
from . import views

urlpatterns = [
    path('socialize/', views.index, name='all_socialize'),
    path('socialize/success', views.registration_complete, name='registration_complete'),
    # our-domain.com/socialize
    path('socialize/<slug:socializes_slug>', views.socializes_details, name='socializes-details'), # our-domain.com/socialize/<dynamic-path-segment>a-second-socialize
    # path('#')

]

