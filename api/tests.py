from django.test import TestCase
from api.models import Identifier

class QRTestCase(TestCase):
    obj1 = None
    obj2 = None
    def setUp(self):
        obj1=Identifier.QrCode.objects.create()
        obj2=Identifier.QrCode.objects.create()

    def test_QRcode_has_code(self):
        assertNotEqual(obj1.string, null)
        assertNotEqual(obj2.string, null)
