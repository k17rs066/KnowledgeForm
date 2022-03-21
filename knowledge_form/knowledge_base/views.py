from django.shortcuts import render,get_object_or_404   # データベースからデータを取り出す際に、見つからなかった場合404エラーを発生する
from knowledge_base.models import Knowledge
from django.http import HttpResponse

# Create your views here.
def  top(request):
    knowledges = Knowledge.objects.all()    # 登録したナレッジの一覧を取得
    context = {"knowledges": knowledges}    # テンプレートエンジンに渡すオブジェクト
    return render(request,"top.html",context)   

def knowledge_regist():
    return HttpResponse('ナレッジを追加登録')

def knowledge_edit():
    return HttpResponse('ナレッジの編集')

def knowledge_detail(request,knowledge_id):
    knowledge = get_object_or_404(Knowledge)
    return render(request, 'knowledges/knowledge_detail.html',{'knowledge': knowledge})