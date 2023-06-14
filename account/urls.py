from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="account-index-page"),
    path("create/",views.registration, name="account-registration-page"),
    path("create/thank_you/",views.thank_you, name="thank_you-page"),
    path("login/",views.Login, name="login-page"),
    path("logout/",views.logout, name="logout"),
    path("prifile/<slug:slug>",views.profile,name="profile-details-page")

]
