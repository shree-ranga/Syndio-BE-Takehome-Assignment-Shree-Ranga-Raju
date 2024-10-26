from django.urls import path

from mathapp.views import GetPValue

urlpatterns = [
    path("pvalue", GetPValue.as_view(), name="get_p_value"),
]
