# -*- coding:Utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView

from datetime import date

from models import Member
from forms import AdhesionForm

def adherer(request):
    message = "Merci, votre demande d'adhésion a bien été pris en compte, merci."
    return render(request, "simple.html", {'message': message})

class AdhesionFormView(FormView):
    form_class=AdhesionForm
    template_name="members/member_form.html"
    success_url="/adherer/post/"

    def post(self, request, *args, **kwargs):
        to_return = super(AdhesionFormView, self).post(request, *args, **kwargs)
        form = AdhesionForm(request.POST)
        if form.is_valid():
            Member.objects.create(name=form.cleaned_data["name"],
                                  surname=form.cleaned_data["surname"],
                                  email=form.cleaned_data["email"],
                                  address=form.cleaned_data["address"],
                                  demande=date.today()
                                 )
        return to_return
