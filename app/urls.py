from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.Add.as_view(),name="add"),
    path('update/',views.Update.as_view(),name="update"),
    path('manage/update/<slug:pk>',views.Update.as_view(),name="update"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('manage/data-source/',views.datatables,name="manage"),
    path('manage/',views.Manage.as_view(),name="manage"),
  
    path('manage/delete/<int:pk>',views.Delete.as_view(),name="delete"),
    # path('my/datatable/data/', views.OrderListJson.as_view(), name='order_list_json')
]
