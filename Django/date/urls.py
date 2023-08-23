from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("review_list/", views.ReviewList.as_view(), name="review_list"),
    path("main_area/<str:q>/",views.SelectPage.as_view(), name="select_page"),
    path("place/",views.PlaceList.as_view(),name="place_list"),
    path("place/cafe/",views.PlaceCafe.as_view(),name = "place_cafe"),
    path("place/rest/",views.PlaceRest.as_view(),name = "place_rest"),
    path("place/place/",views.PlacePlace.as_view(),name = "place_place"),
    path("place/cafe/<str:q>/",views.PlaceCafeLoc.as_view(),name = "place_cafe_loc"),
    path("place/rest/<str:q>/",views.PlaceRestLoc.as_view(),name = "place_rest_loc"),
    path("place/place/<str:q>/",views.PlacePlaceLoc.as_view(),name = "place_rest_loc"),
    path("cafedetail/<str:q>/",views.CafeDetail.as_view(), name = "cafe_detail"),
    path("restdetail/<str:q>/",views.RestDetail.as_view(), name = "rest_detail"),
    path("placedetail/<str:q>/",views.PlaceDetail.as_view(), name = "place_detail"),
    path("cos/<int:q1>/<int:q2>/<int:q3>", views.CosPage.as_view(), name="cos_page"),
]