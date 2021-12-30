from django.urls import path, re_path

from .views import (
    menu_list,
    menu_detail,
    cat_list,
    cat_detail,
    )
from .api import (
    CategoriesCreateAPIView,
    CategoriesListAPIView,
    CategoriesRetrieveAPIView,
    CategoriesRetrieveDestroyAPIView,
    CategoriesRetrieveUpdateAPIView,
    MenuCreateAPIView,
    MenuListAPIView,
    MenuRetrieveAPIView,
    MenuRetrieveDestroyAPIView,
    MenuRetrieveUpdateAPIView,
    )

app_name='menu'
urlpatterns = [
    path('',
        menu_list,
        name="menu_list"
        ),
    path('category/',
        cat_list,
        name="cat_list"
        ),
    re_path(r'^category/details/(?P<slug>[\w-]+)/$',
        cat_detail,
        name="cat_detail"
        ),
    re_path(r'^details/(?P<slug>[\w-]+)/$',
        menu_detail,
        name="menu_detail"
        ),
    # menu api
    path('api/',
        MenuListAPIView.as_view(),
        name="menu_list_api"
        ),
    path('api/create/',
        MenuCreateAPIView.as_view(),
        name="menu_create_api"
        ),
    re_path(r'^api/(?P<slug>[\w-]+)/$',
        MenuRetrieveAPIView.as_view(),
        name="menu_detail_api"
        ),
    re_path(r'^api/(?P<slug>[\w-]+)/update/$',
        MenuRetrieveUpdateAPIView.as_view(),
        name="menu_update_api"
        ),
    re_path(r'^api/(?P<slug>[\w-]+)/destroy/$',
        MenuRetrieveDestroyAPIView.as_view(),
        name="menu_destroy_api"
        ),
    # category api
    path('category/api/',
        CategoriesListAPIView.as_view(),
        name="cat_list_api"
        ),
    path('category/api/create/',
        CategoriesCreateAPIView.as_view(),
        name="cat_create_api"
        ),
    re_path(r'^category/api/(?P<slug>[\w-]+)/$',
        CategoriesRetrieveAPIView.as_view(),
        name="cat_detail_api"
        ),
    re_path(r'^category/api/(?P<slug>[\w-]+)/update/$',
        CategoriesRetrieveUpdateAPIView.as_view(),
        name="cat_update_api"
        ),
    re_path(r'^category/api/(?P<slug>[\w-]+)/destroy/$',
        CategoriesRetrieveDestroyAPIView.as_view(),
        name="cat_destroy_api"
        ),
]
