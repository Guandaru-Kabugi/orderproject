from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','student_name','job_title','sent_date','due_date','completed','cancelled','page_count','word_count','additional_notes']