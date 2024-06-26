from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import generic
from .forms import userpromptForm
from .models import Reviewcont

import openai

class IndexView(generic.TemplateView):
    template_name = "top.html"

reviewpers =[]
reviewcont = []
def userpromptview(request):
    if request.method == 'POST':
        form = userpromptForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            #reviewpers=[]
            reviewcont.append(request.POST.get("reviewcont"))
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

            # redirect to a new URL:
            return HttpResponseRedirect("redirect")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = userpromptForm()

    return render(request, "userprompt.html", {"form": form})

reviewperspectives=[]
def redirectview(request):
    for r in reviewpers:
        print(r) 
    print(reviewcont[0])
    for i in reviewpers:
        reviewperspectives.append(i+"-"+str(Reviewcont.objects.get(review_pers=i).review_dir))
    
    openai.api_type = "azure"
    openai.api_base = "https://reviewmodel.openai.azure.com/" 
    openai.api_version = "2023-03-15-preview"
    openai.api_key = "27e6b907565140a79830da866aec6908"
    response = openai.ChatCompletion.create(
        engine="ReviewAI", # モデルのデプロイ名を指定
        messages = [
            {"role":"system",
            "content":"## 役割\nあなたは、ベテランエンジニアで、私の上司です。ユーザーがクライアントにアウトプットする前に、あなたに対して内部レビューを依頼しています。ユーザーが提供するレビュー依頼文章に対して、以下のレビュー観点とレビュー方針を用いて、レビューしてください。\n## レビュー観点-レビュー方針\n"+','.join(reviewperspectives)},
            # レビュー依頼文面を追加
            {"role":"user",
            "content":reviewcont[0]}
            ],
        temperature=1,
        max_tokens=800,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    print(','.join(reviewperspectives))
    print(response["choices"][0]["message"]["content"]) # 結果を出力する
    context={
        'feedback':response["choices"][0]["message"]["content"]
    }

    return render(request, "redirect.html",context)


    #template_name = "userprompt.html"
    #form_class = userpromptForm




    

