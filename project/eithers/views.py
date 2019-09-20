from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions}
    return render(request, 'eithers/index.html', context)


def create(request):
    # CREATE
    if request.method == 'POST':        
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect(question)
    # NEW
    else:
        return render(request, 'eithers/create.html')



def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    context = {'question': question, 'answers': answers,}
    return render(request, 'eithers/detail.html', context)


def answers_create(request, question_pk):
    
    for answer in answers:

    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        pick = request.POST.get('pick')
        answer = Answer(question=question, comment=comment, pick=pick)
        answer.save()
        return redirect(question)
    else:
        return redirect(question)