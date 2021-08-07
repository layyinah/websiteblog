from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('add/',views.addblog,name='addblog'),
    path('detail/<int:id>', views.blogdetail, name='blogdetail'),

    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')


    ]