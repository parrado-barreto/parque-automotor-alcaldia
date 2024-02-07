from celery import shared_task
from panel.models import Vehiculos
from datetime import datetime
import datetime as dt
import logging


@shared_task
def soat():
    logger = logging.getLogger('soat')
    now = datetime.now()
    lapsus2 = dt.timedelta(days=1)
    now2 = now + lapsus2
    lapsus = dt.timedelta(days=3)
    future = now + lapsus
    vehiculosh = Vehiculos.objects.filter(soa_veh__fec_ven_soa__gte=now, soa_veh__fec_ven_soa__lte=now2)
    vehiculos = Vehiculos.objects.filter(soa_veh__fec_ven_soa__gte=now2,
                                         soa_veh__fec_ven_soa__lte=future)

