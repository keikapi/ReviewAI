from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import generic
from .forms import userpromptForm

class IndexView(generic.TemplateView):
    template_name = "top.html"


def userpromptview(request):
    if request.method == 'POST':
        form = userpromptForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            reviewpers=[]
            reviewcont=request.POST.get("reviewcont")
            if request.POST.get("reviewpers_1") == "on":
                reviewpers.append("信頼性")
            if request.POST.get("reviewpers_2") == "on":
                reviewpers.append("網羅性")
            if request.POST.get("reviewpers_3") == "on":
                reviewpers.append("妥当性")
            if request.POST.get("reviewpers_4") == "on":
                reviewpers.append("可読性")
            if request.POST.get("reviewpers_5") == "on":
                reviewpers.append("誤字脱字")

            print(reviewpers[1])
            # redirect to a new URL:
            return HttpResponseRedirect("redirect")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = userpromptForm()

    return render(request, "userprompt.html", {"form": form})



def redirectview(request):

    return render(request, "redirect.html")


    #template_name = "userprompt.html"
    #form_class = userpromptForm




    

