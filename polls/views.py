from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from django.urls import reverse

class IndexView(ListView):
    template_name = 'polls_question.html'

    def get_queryset(self):
        return Question.objects.order_by('-timestamp')[:3]

#
# class PollDetailView(DetailView):
#     model = Question
#     template_name = 'polls_detail.html'

def polldetail(request, id=None):
    question = get_object_or_404(Question, id=id)
    if request.method=='POST':
        if request.POST.get('answer'):
            try:
                selected_answer = question.answer_set.get(pk=request.POST['answer'])
            except(Answer.DoesNotExist):
                return render(request, 'polls_detail.html', {
                    'question': question,
                    'error_message': "Указан недопустимый ответ",
                })
            selected_answer.votes += 1
            selected_answer.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            return render(request, 'polls_detail.html', {
                'question': question,
                'error_message': "Вы не выбрали ответ.",
            })
    return render(request, 'polls_detail.html', {
        'question': question,
    })


class ResultsView(DetailView):
    model = Question
    template_name = 'polls_results.html'