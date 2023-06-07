from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        # fields = ['uid','todo_title','todo_description','is_done']
        fields = ['user','uid','title','impact','ease','confidence','description','score']

    def get_score(self,obj):
        imp = obj.impact
        eas = obj.ease
        conf = obj.confidence
        return int((imp+eas+conf)/3)


