from django.urls import path
from . import views 

urlpatterns = [
   
    path('',views.homepage,name='homepage'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>/',views.customer_record,name='customer_record'),
    path('delete_record/<int:pk>/',views.delete_customer_record,name='delete_customer_record'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>/',views.update_record,name='update_record'),
    

]