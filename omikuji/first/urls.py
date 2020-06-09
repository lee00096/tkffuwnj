from django.urls import path
from first.views import definition, fortune, daegil, gil, sogil, margil, hyung


app_name = "first"
urlpatterns = [
    path('definition/',definition, name="definition"),


    path('fortune/',fortune, name="fortune"),


    path('daegil/',daegil, name="daegil"),


    path('gil/',gil, name="gil"),


    path('sogil/',sogil, name="sogil"),


    path('margil/',margil, name="margil"),


    path('hyung/',hyung, name="hyung"),
]