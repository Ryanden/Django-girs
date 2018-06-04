from django.conf.urls import url
from .views import post_list, post_detail

# Browser -> request -> Django -> config.urls -> blog.urls -> r'^$'에 매칭 ->
# df post_list -> return 값을 다시 Browser
urlpatterns = [
    # url의 첫번째 인자 URL정규표현식
    # url의 두번째 인자 view function
    #   view_function
    #       -> request를 받아서 response를 돌려주는 함수

    # 함수를 전달함
    url(r'^$', post_list),
    url(r'^(\d+)', post_detail)
]