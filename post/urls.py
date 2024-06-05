from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.initial_page, name='initial-page'),
    path('post/<int:id>', views.post, name='post_details')
]