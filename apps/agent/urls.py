from django.urls import path
from . import views

urlpatterns = [
    path("", views.agent_query, name="agent-query"),
]
