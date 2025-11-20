from django.urls import path
from .views import (
    FormsCatalogView,
    DemographicFormCreateView,
 Form4CreateView,MiddleFormCreateView,Form2CreateView,PrFoodCreateView
)

app_name = "form"  # namespace

urlpatterns = [
    path("forms/", FormsCatalogView.as_view(), name="forms-catalog"),       # GET
    path("forms/form1/", DemographicFormCreateView.as_view(), name="form1"),# POST
    path("forms/form2/", Form2CreateView.as_view(), name="form2"),  # POST  ⟵ اضافه شد

    path("forms/form5/", PrFoodCreateView.as_view(), name="form5"),          # POST  ⟵ جدید
    path("forms/form4/", Form4CreateView.as_view(), name="form4"),          # POST
    path("forms/middle/", MiddleFormCreateView.as_view(), name="middle"),  # POST
]
