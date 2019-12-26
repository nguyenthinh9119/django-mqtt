from rest_framework.serializers import ModelSerializer
# from .models import Emp
from .models import ACL

class EmpSerializer(ModelSerializer):
    class Meta:
        model = ACL
        fields = "__all__"