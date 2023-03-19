from django.urls import path
from .import views
from .import predict
from .import to_db

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('immunization/', views.immunization, name='immunization'),
    path('mortality/', views.mortality, name='mortality'),
    path('health/', views.health, name='health'),
    path('social/', views.social, name='social'),
    path('economic/', views.economic, name='economic'),
    path('take', to_db.store, name='take'),
    path('take1', to_db.store1, name='take1'),
    path('take2', to_db.store2, name='take2'),
    path('take3', to_db.store3, name='take3'),
    path('take4', to_db.store4, name='take4'),
    path('classify', predict.classifyDiabetes, name='classify'),
]