from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homePage, name='homepage'),
    path('', views.ListPostCreateView.as_view(), name='listPost'),
    path('<int:id>', views.PostRetrieveUpdateDeleteView.as_view(), name='PostRetrieveUpdateDelete'),
    # path('<int:id>', views.getSinglePost, name='get_single-post'),
    # path('update/<int:id>', views.getUpdatePost, name='update-post'),
    # path('delete/<int:id>', views.deletePOST, name='delete-post'),
]
