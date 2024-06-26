from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import generic
from .forms import userpromptForm

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

            print(reviewpers)
            # redirect to a new URL:
            return HttpResponseRedirect("redirect")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = userpromptForm()

    return render(request, "userprompt.html", {"form": form})

def redirectview(request):
    for r in reviewpers:
        print(r)
    print(reviewcont[0])
    openai.api_type = "azure"
    openai.api_base = "https://reviewmodel.openai.azure.com/" 
    openai.api_version = "2023-03-15-preview"
    openai.api_key = "27e6b907565140a79830da866aec6908"
    response = openai.ChatCompletion.create(
        engine="ReviewAI", # モデルのデプロイ名を指定
        messages = [
            {"role":"system",
            "content":"## 役割\nあなたは、ベテランエンジニアで、私の上司です。クライアントにアウトプットする前に、あなたに対して内部レビューを依頼しています。ユーザーが提供するレビュー依頼文章に対して、特定のレビュー観点を用いて、レビューしてください。レビュー観点/方針については、以下を参照してください。\n## レビュー観点/方針\n"+','.join(reviewpers)},
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
    print(','.join(reviewpers))
    print(response["choices"][0]["message"]["content"]) # 結果を出力する

    return render(request, "redirect.html")


    #template_name = "userprompt.html"
    #form_class = userpromptForm




    

