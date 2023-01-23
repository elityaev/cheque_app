from django.db import models
from django.urls import reverse


class ProcessedCheckManager(models.Manager):
    def get_queryset(self):
        return super(ProcessedCheckManager, self).get_queryset().filter(processing=True)


class Receipt(models.Model):
    date = models.DateTimeField()
    organization = models.CharField(max_length=256)
    summa = models.FloatField()
    processing = models.BooleanField(default=False)
    objects = models.Manager()
    processed = ProcessedCheckManager()

    def get_absolute_url(self):
        return reverse('receipts:receipt_detail', args=[self.pk])

    def __str__(self):
        return f'{self.date}, {self.organization}, {self.summa}'


class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.FloatField()
    price = models.FloatField()
    sum = models.FloatField()
    sub_category = models.ForeignKey(
        'SubCategory',
        on_delete=models.DO_NOTHING,
        related_name='products',
        null=True,
        blank=True
    )
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_category'
    )

    def __str__(self):
        return self.name
