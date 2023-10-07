from.import views
from django.urls import path
app_name='todoapp'
urlpatterns = [
     path('',views.index,name='index'),
     path('delete/<int:taskid>/',views.delete ,name='delete'),
     path('update/<int:id>/',views.update ,name='update')

]
