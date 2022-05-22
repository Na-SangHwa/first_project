

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

def index(request):
    question_list=Question.objects.order_by('-create_date') ##질문 목록 데이터 역순으로 정렬
    context={'question_list': question_list}
    return render(request,'hiru/question_list.html',context)##템플릿에 적용해 html로 반환

def detail(request, question_id): ##uri 매핑 규칙에 의해 실행
    question = get_object_or_404(Question, pk=question_id) # 없는 페이지 조회시 404 출력
    context = {'question': question}
    return render(request, 'hiru/question_detail.html', context)

def answer_create(request, question_id): # 답변 생성 및 읽어오기
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('hiru:detail', question_id=question_id)