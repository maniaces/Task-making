from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key= True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank= True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    impact = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=5)
    ease = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=5)
    confidence = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=5)
    is_done = models.BooleanField(default=False)
