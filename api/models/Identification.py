from django.db import models


class Identification(models.Model):
    ACTIVE = 'AC'
    INACTIVE = 'IN'
    LOST = 'LO'
    DAMAGED = 'DA'

    TAG_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (LOST, 'Lost'),
        (DAMAGED, 'Damaged'),
    ]

    status = models.CharField(max_length=2,
        choices=TAG_STATUS,
        default=INACTIVE,)
