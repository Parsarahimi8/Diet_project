from django.urls import path
from .views import (
    FormsCatalogView,
    DemographicView,
    PWIFormCreateView,FreeShoppingView
)

app_name = "form"  # namespace

urlpatterns = [
    path("forms/", FormsCatalogView.as_view(), name="forms-catalog"),        # GET
    path("forms/form1/", DemographicView.as_view(), name="form1"), # POST
    path("forms/form3/", PWIFormCreateView.as_view(), name="form2"),         # POST
    path("forms/form5/", FreeShoppingView.as_view(), name="form4"),          # POST
]

