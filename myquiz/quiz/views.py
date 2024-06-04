from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView

from results.models import Result
from .models import Quiz
from quiz_questions.models import Answer, Question

class QuizListView(ListView):
    # Utiliser la classe ListView pour afficher une liste des quizzes
    model = Quiz
    template_name = "quiz/main.html"

def quiz_view(request, pk):
    # Obtenir le quiz spécifique ou renvoyer une erreur 404 si non trouvé
    quiz_object = get_object_or_404(Quiz, pk=pk)
    # Préparer le contexte avec l'objet quiz pour l'affichage
    context = {'quiz_object': quiz_object}
    # Renvoyer la page du quiz avec le contexte
    return render(request, 'quiz/quiz.html', context)

def quiz_data_view(request, pk):
    # Obtenir le quiz spécifique ou renvoyer une erreur 404 si non trouvé
    quiz_object = get_object_or_404(Quiz, pk=pk)
    questions = []

    for q in quiz_object.get_questions():
        answers = []

        # Supposant que les modèles Question et Answer sont définis et liés à Quiz
        # Parcourir les réponses associées à chaque question du quiz
        for a in q.answer_set.all():
            answers.append(a.text)
        # Ajouter la question et ses réponses à la liste des questions
        questions.append({str(q): answers})

    # Renvoyer les données du quiz au format JSON avec le temps requis
    return JsonResponse({
        "data": questions,
        "time": quiz_object.time,
    })


def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop("csrfmiddlewaretoken")

        for k in data_.keys():
            print('key:', k)
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = get_object_or_404(Quiz, pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []

        for q in questions:
            a_selected = request.POST.get(q.text)
            correct_answer = None
            
            if a_selected:
                question_answers = Answer.objects.filter(question=q)
                
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    elif a.correct:
                        correct_answer = a.text

                results.append({str(q): {"correct_answer": correct_answer, "answered": a_selected}})
            else:
                results.append({str(q): "not answered"})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score >= quiz.required_score_to_pass:
            return JsonResponse({"passed": True, "score": score_, "results": results})
        else:
            return JsonResponse({"passed": False, "score": score_, "results": results})
                    
    
    