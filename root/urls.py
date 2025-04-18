from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.http import HttpRequest, HttpResponse


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError as e:
        return HttpResponse("Xatolik yuz berdi: bo‘lish 0 ga mumkin emas.")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('sentry-debug/', trigger_error),

]
