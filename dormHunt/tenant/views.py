from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
    )

# SECTION Import Model
from landlord.models import Property


# Create your views here.
class Tenant(TemplateView):
    template_name = 'tenant/tenant_home.html'

class TenantFavorites(TemplateView):
    template_name = 'tenant/tenant_favorites.html'

class TenantDormSearch(ListView):
    model = Property
    template_name = 'tenant/tenant_search.html'

class ViewPropertyDetailView(DetailView):
    model = Property
    template_name = 'tenant/view_property.html'