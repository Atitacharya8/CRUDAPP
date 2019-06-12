from django.urls import path
from crudapp import views


urlpatterns = [
    path("",views.base),
    path("emp",views.emp),
    path("show",views.show),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),
]