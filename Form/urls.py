from django.urls import path
from .views import (
    DemographicView,
    TablemateView,
    PWIFormCreateView,FreeShoppingView
)

app_name = "form"

urlpatterns = [
    path("forms/form1/", DemographicView.as_view(), name="form1"),
    path("forms/form2/", TablemateView.as_view(), name="form2"),
    path("forms/form3/", PWIFormCreateView.as_view(), name="form3"),
    path("forms/form5/", FreeShoppingView.as_view(), name="form4"),
]

