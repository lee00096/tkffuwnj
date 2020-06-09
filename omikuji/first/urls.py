from django.urls import path
from .views import definition, fortune

app_name = "first"
urlpatterns = [
    path('definition/',definition, name="definition"),


    path('fortune/',fortune, name="fortune"),


    path('daegil/',daegil, name="daegil"),


    path('gil/',gil, name="gil"),


    path('sogil/',sogil, name="sogil"),


    path('margil/',fortune, name="margil"),


    path('hyung/',fortune, name="hyung"),
]