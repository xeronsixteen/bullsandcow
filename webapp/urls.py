from django.urls import path

from webapp.views import index_view, history_view

urlpatterns = [
    path('', index_view),
    path('history/', history_view),
]