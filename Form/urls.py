from django.urls import path
from .views import (
    FormsCatalogView,
    DemographicFormCreateView,
    Form2CreateView, Form3CreateView, Form4CreateView
)

app_name = "form"  # namespace

urlpatterns = [
    path("forms/", FormsCatalogView.as_view(), name="forms-catalog"),       # GET
    path("forms/form1/", DemographicFormCreateView.as_view(), name="form1"),# POST
    path("forms/form2/", Form2CreateView.as_view(), name="form2"),          # POST
    path("forms/form3/", Form3CreateView.as_view(), name="form3"),          # POST
    path("forms/form4/", Form4CreateView.as_view(), name="form4"),          # POST
]
