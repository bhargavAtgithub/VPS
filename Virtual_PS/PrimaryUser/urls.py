from django.urls  import path, include
from PrimaryUser import views

app_name = 'PrimaryUser'

urlpatterns = [
    path('', views.PrimaryUserView.as_view(), name = 'PrimaryUser'),
]