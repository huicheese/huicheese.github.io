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
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    yearpublished = models.IntegerField(db_column='yearPublished')  # Field name made lowercase.
    stock = models.IntegerField()
    price = models.FloatField()  
    format = models.CharField(max_length=9, blank=True, null=True)
    keywords = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Customers(models.Model):
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=30)  # Field name made lowercase.
    pw = models.CharField(max_length=50)
    majorccn = models.CharField(db_column='majorCCN', max_length=19, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    phonenum = models.CharField(db_column='phoneNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Feedback(models.Model):
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=30)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15)  # Field name made lowercase.
    review = models.IntegerField(blank=True, null=True)
    optionalcomment = models.TextField(db_column='optionalComment', blank=True, null=True)  # Field name made lowercase.
    feedback_date = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'
        unique_together = (('loginID', 'ISBN'),)


class Makeorder(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'makeorder'
        unique_together = (('oid', 'loginID'),)


class Orderitems(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15)  # Field name made lowercase.
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderitems'
        unique_together = (('ISBN', 'oid'),)


class Orders(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    order_date = models.TimeField()
    order_status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Ratings(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    feedbackid = models.CharField(db_column='feedbackID', primary_key=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    ratingid = models.CharField(db_column='ratingID', primary_key=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'
        unique_together = (('ISBN', 'feedbackID', 'ratingID'),)
