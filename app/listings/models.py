from django.db import models
from datetime import datetime, timedelta
from foremen.models import Foreman


class Listing(models.Model):
    """Docstring for Instrument."""
    id = models.AutoField(primary_key=True)
    foreman = models.ForeignKey(Foreman, on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=50)
    unit = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=50)
    lrv = models.DecimalField(max_digits=10, decimal_places=2)
    urv = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    serial_no = models.CharField(max_length=50, blank=True)
    interval = models.IntegerField()  # Διάστημα σε ημέρες
    last_checked = models.DateTimeField(default=datetime.now,
                                        blank=True)
    is_active = models.BooleanField(default=True)
    history = models.TextField()
    data_sheet = models.FileField(upload_to="data_sheets/",
                                  blank=True, null=True)  # Ανέβασμα αρχείου PDF
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)

    @property
    def next_check(self):
        """Υπολογισμός της επόμενης επιθεώρησης ως last_checked + interval"""
        if self.last_checked and self.interval:
            return self.last_checked + timedelta(days=self.interval)
        return None

    def __str__(self):
        return self.tag
