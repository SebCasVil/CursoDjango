from django.urls import path
from . import views

urlpatterns = [
    # ex: /app/
    path("", views.index, name="index"),
    # ex: /app/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /app/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /app/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # URLS para el form
    path('crear_pregunta/', views.crearPregunta, name='crear_pregunta'),
    path('crear_opcion/', views.crearOpcion, name='crear_opcion'),
]
