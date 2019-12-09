from django.views.generic.edit import CreateView
from destinos.models import Paquete
from .models import billing
from .forms import BillingForm


# Create your views here.

class billing(CreateView):
    model = billing
    form_class = BillingForm
    template_name = 'billing/form.html'
    success_url = 'Destinations'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        self.paquete = request.POST.get('paquete')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paquete'] = Paquete.objects.get(slug=self.paquete)
        return context
