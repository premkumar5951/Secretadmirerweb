
from django.urls import path
from django.conf.urls import include
from secretmsgapp import views
import random
rand1=random.randint(999,9999)
urlpatterns = [
    path("",views.loginpage,name="loginpage"),
    path("signup/",views.signup,name="signup"),
    path("profile/",views.profile,name="profile"),
    path("logout/",views.logmeout,name="logout"),
    path("about/",views.aboutus,name="aboutus"),
    path("feedback/",views.feed,name="feed"),
    path("user/810384<int:Id>095757/$msgs/",views.sendmsg,name="sendmsg"),

]





