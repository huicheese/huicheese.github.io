# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Books(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15, blank=True, null=False)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    yearpublished = models.IntegerField(db_column='yearPublished')  # Field name made lowercase.
    stock = models.IntegerField()
    price = models.TextField()  # This field type is a guess.
    format = models.CharField(max_length=9, blank=True, null=True)
    keywords = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Customers(models.Model):
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=30, blank=True, null=False)  # Field name made lowercase.
    pw = models.CharField(max_length=50)
    majorccn = models.CharField(db_column='majorCCN', max_length=19, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    phonenum = models.CharField(db_column='phoneNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Feedbacks(models.Model):
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=30)  # Field name made lowercase.
    loginid = models.ForeignKey('Customers', db_column='loginID')
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15)  # Field name made lowercase.
    isbn = models.ForeignKey('Books', db_column='ISBN')
    review = models.IntegerField(blank=True, null=True)
    optionalcomment = models.TextField(db_column='optionalComment', blank=True, null=True)  # Field name made lowercase.
    feedback_date = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedbacks'
        unique_together = (('loginid', 'isbn'),)


class OrderItems(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    isbn = models.ForeignKey('Books', db_column='ISBN')
    oid = models.ForeignKey('Orders', db_column='oid')
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_items'
        unique_together = (('isbn', 'oid'),)


class Orders(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=False)
    loginid = models.CharField(db_column='loginID', max_length=30)  # Field name made lowercase.
    loginid = models.ForeignKey('Customers', db_column='loginID')
    order_date = models.TimeField()
    order_status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Ratings(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15, blank=True, null=False)  # Field name made lowercase.
    isbn = models.ForeignKey('Books', db_column='ISBN')
    feedbackid = models.CharField(db_column='feedbackID', primary_key=True, max_length=30, blank=True, null=False)  # Field name made lowercase.
    feedbackid = models.ForeignKey('Feedbacks', db_column='feedbackID')
    ratingid = models.CharField(db_column='ratingID', primary_key=True, max_length=30, blank=True, null=False)  # Field name made lowercase.
    ratingid = models.ForeignKey('Customers', db_column='ratingID')
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'
        unique_together = (('isbn', 'feedbackid', 'ratingid'),)
