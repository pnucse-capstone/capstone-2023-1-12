from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.db.models import Q

from django.urls import reverse
from django.shortcuts import redirect

from app_model.database.models import Restaurant, RestaurantServiceName

from django.templatetags.static import static
from django.db.models import Count

def before_search_view(request):
    context = {
    }
    return render(request, 'search/before_search.html', context)

def gpt(q):
    a = ''
    return a


def search_view(request):
    query = request.GET

    location_query = query.get('location_query', '').strip()
    name_query     = query.get('name_query', '').strip()
    gpt_query      = query.get('gpt_query', '').strip()
    gpt_answer     = query.get('answer', '').strip()

    # 검색어를 기반으로 DB에서 검색 결과 조회
    search_results = Restaurant.objects.filter(service__is_use=True)  # 모든 레스토랑을 기본으로 가져옵니다.

    if location_query:
        search_results = search_results.filter(Q(full_address__icontains=location_query) | Q(road_address__icontains=location_query))

    if name_query:
        search_results = search_results.filter(name__icontains=name_query)

    if gpt_query and not gpt_answer:
        gpt_answer = "answer1234"
        
        # 결과를 쿼리 매개변수로 URL에 추가
        query = request.GET.copy()  # 쿼리를 복사하여 업데이트합니다.
        query['answer'] = gpt_answer  # 쿼리 매개변수에 업데이트합니다.

        # 새로운 URL로 리디렉션
        return redirect(reverse('search') + f'?{query.urlencode()}')

    print(query.urlencode())
    print(query.urlencode()+f'&answer={gpt_answer}')

    service_objects = (
        search_results.values('service')
        .annotate(service_count=Count('service'))
        .order_by('-service_count')
    )
    service_list = [
        RestaurantServiceName.objects.get(idx=x["service"]).service
        for x in service_objects
    ]
    print("\n".join(service_list))

    marker_informations = {
        "default": {
            "box_all" : static('img/default/box_all.png'),
            "box_off" : static('img/default/box_off.png' ),
            "off"     : static('img/default/off.png'),
        },
    }
    for name in ['fried_chicken', 'italian', 'pizza']:
        marker_informations[name] = {}
        for i in ['box', 'on', 'off'] + [str(x) for x in range(1, 10)]:
            marker_informations[name][i] = static(f'img/{name}/{i}.png')
            

    context = {
        'search_results': search_results,
        'location_query': location_query,
        'name_query'    : name_query,
        'gpt_query'     : gpt_query,
        'gpt_answer'    : gpt_answer,
        'org_query'     : query.urlencode()+f'&answer={gpt_answer}',
        'marker_informations': marker_informations,
        'service_list'  : service_list,
    }
    return render(request, 'search/search.html', context)