from django.urls import path,include
from.import views
app_name='storeapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('new/',views.new,name='new'),
    path('add/', views.person_create_view, name='add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('load-courses/', views.load_courses, name='load_courses'),  # AJAX
    path('new3/',views.new3,name='new3'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')

]