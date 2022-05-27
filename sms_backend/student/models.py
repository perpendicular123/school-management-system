from msilib.schema import AdminExecuteSequence
from posixpath import supports_unicode_filenames
from unicodedata import name
from django.db import models

# Create your models here.
1  admin@admin@gmail.com


baseUserModel(models.Model):
 name
 surname 
 email
 address
 

student(baseUserModel):
documents 
