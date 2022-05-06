

# Create your views here.
from django.shortcuts import render
from .models import Question

def index(request):
    question_list=Question.objects.order_by('-create_data') #질문 목록 데이터 역순으로 정렬
    context={'question_list': question_list}
    return render(request,'hiru/question_list.html',context)#템플릿에 적용해 html로 반환
