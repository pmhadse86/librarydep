"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Book.views import *
from subscribe.views import subscribe_mail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name = 'home'),
    path("homepage/", homepage, name="home"),
    path("show-all-books/", get_books, name="show-book"),
    path("delete-book/<int:id>/", delete_book, name="delete"),
    path("update-book/<int:id>/", update_book, name="update"),
    path("soft-delete/<int:id>/", soft_delete, name="soft-delete"),
    path("active-books/", active_books, name="active-books"),
    path("inactive-books/", in_active_books, name="inactive-books"),
    path("restore-books/<int:id>/", restore_books, name="restore"),

# email app

    path("email-home/", subscribe_mail, name = "subscribe-email")

]

