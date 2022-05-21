

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    question_list=Question.objects.order_by('-create_date') ##질문 목록 데이터 역순으로 정렬
    context={'question_list': question_list}
    return render(request,'hiru/question_list.html',context)##템플릿에 적용해 html로 반환

def detail(request, question_id): ##uri 매핑 규칙에 의해 실행
    question = get_object_or_404(Question, pk=question_id) # 없는 페이지 조회시 404 출력
    context = {'question': question}
    return render(request, 'hiru/question_detail.html', context)