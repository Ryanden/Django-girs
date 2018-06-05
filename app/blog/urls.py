from django.conf.urls import url
from .views import post_list, post_detail, post_create

# Browser -> request -> Django -> config.urls -> blog.urls -> r'^$'에 매칭 ->
# df post_list -> return 값을 다시 Browser
urlpatterns = [
    # url 의 첫번째 인자 URL 정규표현식
    # url 의 두번째 인자 view function
    #   view_function
    #       -> request 를 받아서 response 를 돌려주는 함수

    # 함수를 전달함
    url(r'^$', post_list, name='post-list'),
    url(r'^(\d+)/', post_detail, name='post-detail'),
    url(r'^write/', post_create, name='post-create'),
]
