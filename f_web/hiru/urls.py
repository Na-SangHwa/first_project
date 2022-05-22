from django.urls import path
from . import views

app_name='hiru' #네임스페이스

urlpatterns = [
    path('', views.index, name='index'),#별칭 사용
    path('<int:question_id>/', views.detail, name='detail'), #question_id int 매핑, 뷰 호출, 별칭 매핑
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), #answer/create/int 호출시 views.answer_create 호출

]