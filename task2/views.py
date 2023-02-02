from django.shortcuts import render
from task2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
# Create your views here.

class ReviewEmailView(FormView):
    template_name= 'reviews.html'
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.send_email()
        msg= "thanks for this"
        return HttpResponse(msg)
