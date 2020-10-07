from django.urls import path
from . import views
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    # path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)