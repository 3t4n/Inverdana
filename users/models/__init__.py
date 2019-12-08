from django.db.models.signals import pre_save
from . import Suggestions,Event,Feed,Organization,Clan
from api.models import Push
import requests 

def Event_receiver(sender, instance, *args, **kwargs):
	for obj in Push.PushToken.objects.all():
		data = {'to':obj.token, 'title':"Nuevo Evento:"+instance.name, 'body':instance.info}
		requests.post(url = "https://exp.host/--/api/v2/push/send", data = data) 
 

pre_save.connect(Event_receiver, sender=Event.Event)

       