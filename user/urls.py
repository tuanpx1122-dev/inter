from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# ...
from user.views import OrderFruitAPIView

urlpatterns = [
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^order/', OrderFruitAPIView.as_view(), name='order fruits')
]
