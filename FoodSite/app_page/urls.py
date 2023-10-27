from django.urls import path
from app_page import views
from app_page.individual import views as individual_views
from app_page.search import views as search_views

app_name = 'app_page'

urlpatterns = [
    path('', search_views.before_search_view, name='first_index'),
    path('search/', search_views.search_view, name='search'),
    path('result/<int:pk>/', individual_views.search_result_view, name='result'),
    # 추가적인 URL 패턴을 정의할 수 있습니다.
]
