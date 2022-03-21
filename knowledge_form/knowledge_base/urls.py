
from django.urls import path
from knowledge_base import views

urlpatterns = [
    path('regist/',views.knowledge_regist, name="knowledge_new"),
    path('<int:knowledge_id>/', views.knowledge_detail,name='knowledge_detail'),
    path('<int:knowledge_id>/edit/', views.knowledge_edit,name ='knowledge_edit'),
]