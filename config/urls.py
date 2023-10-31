from django.contrib import admin
from django.urls import path

from app.views import near_hundred, String_Splosion, cat_dog, lone_sum
urlpatterns = [
    path('Logic-2/lone-sum/<int:a>/<int:b>/<int:c>', lone_sum),
    path('String-2/cat-dog/<x>', cat_dog),
    path('warmup-2/String-Splosion/<str:string>', String_Splosion),
    path('warmup-1/near-hundred/<int:n>', near_hundred),
    path("admin/", admin.site.urls),
]
