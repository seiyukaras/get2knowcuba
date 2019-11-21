from django.views.generic.list import ListView
from destinos.models import Paquete

# Create your views here.

class homeListView(ListView):
    model = Paquete
    template_name = 'core/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(home=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tips = Paquete.objects.order_by('?')[:1]
        context['tips_list'] = tips
        round = Paquete.objects.exclude(round=False)
        context['round_list'] = round
        oferta = Paquete.objects.exclude(oferta=False)
        context['oferta_list'] = oferta
        return context