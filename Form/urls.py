from django.urls import path
from .views import (
    FormsCatalogView,
    DemographicFormCreateView,
    MiddleFormCreateView,PWIFormCreateView,PrFoodCreateView,FreeShoppingView
)

app_name = "form"  # namespace

urlpatterns = [
    path("forms/", FormsCatalogView.as_view(), name="forms-catalog"),        # GET
    path("forms/form1/", DemographicFormCreateView.as_view(), name="form1"), # POST
    path("forms/middle/", MiddleFormCreateView.as_view(), name="middle"),    # POST
    path("forms/form3/", PWIFormCreateView.as_view(), name="form2"),         # POST
    path("forms/form4/", PrFoodCreateView.as_view(), name="form5"),          # POST  ⟵
    path("forms/form5/", FreeShoppingView.as_view(), name="form4"),          # POST
]

