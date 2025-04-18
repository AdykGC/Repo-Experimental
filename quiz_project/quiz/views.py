from django.shortcuts import render

# Create your views here.
from .models import Question

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def submit_quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score = 0
        total = 0
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_answer:
                score += question.points
            total += question.points
        return render(request, 'quiz/result.html', {'score': score, 'total': total})
