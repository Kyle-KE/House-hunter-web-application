from django.urls.resolvers import URLPattern
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hhapp'

urlpatterns = [
    path('hostels/', views.HostelListView.as_view(), name='hostel_list'),
    path('hostel/<int:pk>/', views.HostelDetailView.as_view(), name='hostel_detail'),
    path('',views.home, name='home'),
    path('new/', views.CreateHostelView.as_view(), name='hostel_new'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/', views.user_registration, name='user_registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    