from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q


from app_model.database.models import Restaurant


def search_result_view(request, pk):
    # 개별 검색 결과 페이지를 위한 뷰
    restaurant  = get_object_or_404(Restaurant, pk=pk)
    menus       = restaurant.restaurant_menus.all()
    videos      = restaurant.restaurant_videos.all()

    for video in videos:
        text = "&".join([
            f"{key}={value}" for key, value in {"start":video.start_time, "end":video.end_time}.items()
        ])
        if text: text = f"?{text}"
        video.time_contents = text
    
    query = request.GET
    
    location_query = query.get('location_query', '').strip()
    name_query     = query.get('name_query', '').strip()
    category_query = query.get('category_query', '').strip()

    # 검색어를 기반으로 DB에서 검색 결과 조회
    search_results = Restaurant.objects.all()  # 모든 레스토랑을 기본으로 가져옵니다.

    if location_query:
        search_results = search_results.filter(Q(full_address__icontains=location_query) | Q(road_address__icontains=location_query))

    if name_query:
        search_results = search_results.filter(name__icontains=name_query)

    context = {
        'search_results': search_results,
        'location_query': location_query,
        'category_query': category_query,
        'org_query': query.urlencode(),
        
        'restaurant': restaurant,
        'menus': menus,
        'videos': videos,
    }
    return render(request, 'individual/restaurant.html', context)