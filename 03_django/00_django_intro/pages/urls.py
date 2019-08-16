from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # url 결로 마지막에 / 를 붙이는 습관
    path('introduce/<name>/<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
