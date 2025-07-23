from django.urls import path
from RestApiapp import views

urlpatterns = [
    path('', views.health_check),
    path('GET/users', views.get_all_users),
    path('GET/user/<int:id>', views.get_user_by_id),
    path('POST/users', views.create_user),
    path('PUT/user/<int:id>', views.update_user),
    path('DELETE/user/<int:id>', views.delete_user),
    path('GET/search/', views.search_users),
    path('login', views.login_user),
]


