# polls/view.py
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.object.order_by("-pub_date")[:5]
    # 지름길: render()
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    # output = ", ".join([q.question_text for q in latest_question_list])

    # Template으로 처리 하는 방법
    # template = loader.get_template("polls/index.html")
    # context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))


# Leave the rest of the views (detail, results, vote) unchanged


def detail(request, question_id):
    # 지름길: get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

    # 일반적인 404 에러처리
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
