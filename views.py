from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api1.model import Score, Ranking


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        score = request.POST.get('score', '')
        if score:
            # 获取旧分数
            old_score = Score.objects.filter(client=request.user).first()
            if old_score:
                if old_score.score != score:
                    old_score.score = score
                    old_score.save()
            # 添加用户分数
            else:
                Score.objects.create(client=request.user, score=score)
            # 更新排名表
            Ranking.objects.all().delete()
            score_li = [score_obj.id for score_obj in Score.objects.all().order_by('-score')]
            n = 1
            for i in score_li:
                Ranking.objects.create(c_id_id=i, rank=n)
                n = n + 1
            return JsonResponse({'status': 'sucess', 'code': 0})
        return JsonResponse({'status': 'error', 'code': 1})


@csrf_exempt
def display(request):
    if request.method == 'POST':
        try:
            start = int(request.POST.get('start'))
            end = int(request.POST.get('end'))
        except ValueError as e1:
            return JsonResponse({'status': 'error'})
        context = {'scores': [{'ranking': score.rank.rank, 'client': score.client, 'score': score.score} for score in
                              Score.objects.all().order_by('-score')[start - 1:end]]}
        return JsonResponse({'status': 'sucess', 'context': context})
