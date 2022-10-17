from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpview.as_view(), name='sign-up'),
]
