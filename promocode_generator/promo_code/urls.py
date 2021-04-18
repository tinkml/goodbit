from django.urls import path

from promo_code import views


urlpatterns = [
    path('promo_code/', views.PromoCodeView.as_view()),
    path('promo_code/<str:promo_code_name>/', views.CheckPromoCodeView.as_view()),
]
