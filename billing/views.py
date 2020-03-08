from django.views.generic.edit import CreateView
from destinos.models import Paquete
from .models import billing
from .forms import BillingForm
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage

from django.template.loader import get_template
import pdfkit

# Create your views here.

class billing(CreateView):
    model = billing
    form_class = BillingForm
    template_name = 'billing/form.html'
    success_url = '/destinations'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        self.paquete = request.POST.get('paquete')
        if form.is_valid():
            url = self.form_valid(form).url
            self.save_and_send_email(self.object)
            return JsonResponse({
                'url': url,
                'message': 'Su presupuesto se ha creado. Hemos enviado un email con los detalles.'
            })
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paquete'] = Paquete.objects.get(slug=self.paquete)
        return context

    def save_and_send_email(self, billing):
        filename = 'billing_' + str(billing.pk) + '_' + self.paquete + '.pdf'
        filepath = settings.MEDIA_ROOT + '/' + filename
        identificacion = billing.id
        compania = [c[1] for c in billing.tipo_compania if c[0] == billing.compania][0]
        adultos = billing.adultos if billing.adultos is not None else 0
        ninos = billing.ninos if billing.ninos is not None else 0
        alojamiento = [a[1] for a in billing.tipo_alojamiento if a[0] == billing.alojamiento][0]
        texto = billing.text
        paquete = billing.titulo
        creado = billing.created
        por_persona = billing.titulo.precio
        descuento = por_persona * 0.05

        if adultos > 2 or ninos > 0:
            # Descuento solo para mas de 3 adultos
            por_persona = por_persona - (descuento*adultos)
            # Descuento por niño
            por_persona = por_persona - (descuento*ninos)
            # Multiplicamos la suma de las personas por el valor unitario
            total = (adultos + ninos) * por_persona
        else:
            # Minimo es de dos adultos
            total = (por_persona * 2)
        

        template = get_template("billing/invoice.html")
        html = template.render({'compania': compania,'adultos':adultos,
            'ninos':ninos, 'alojamiento':alojamiento, 'texto':texto,
            'paquete':paquete,'creado':creado, 'identificacion':identificacion,
            'por_persona':por_persona, 'total':total})
        
        options = {
            'quiet': '',
            'page-size': 'Letter',
            'encoding': "UTF-8",
        }
        pdfkit.from_string(
            html,
            filepath,
            options
        )

        billing.comprobante_presupuesto = filename
        billing.save()

        # por defecto el remitente es settings.DEFAULT_FROM_EMAIL
        destinatarios = settings.ADMINS.append((billing.email, billing.email))
        message = EmailMessage(
            'Presupuesto de Get2KnowCuba',
            '\
                <b>Gracias por usar los servicios de Get2KnowCuba</b><br/> \
                Por favor chequee el fichero adjunto con los detalles de su presupuesto.<br/><br/> \
                Atentamente, equipo de Get2KnowCuba. \
            ',
            settings.DEFAULT_FROM_EMAIL,
            [billing.email,]

        )
        message.attach_file(filepath)
        message.content_subtype = "html"
        message.send(fail_silently=True)
        # para ver los errores en consola usar message.send(fail_silently=True)
