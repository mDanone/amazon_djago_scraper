from django.views.generic import TemplateView

from .models import Merchant


class MecrhantsListView(TemplateView):
    template_name = 'merchants.html'

    def get_context_data(request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merchants'] = Merchant.objects.all()
        return context
