from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense

@api_view(['GET'])
def expense_summary(request):
    summary = Expense.objects.values('category__name').annotate(
        total_amount=Sum('amount')
    ).order_by('category__name')
    
    result = {item['category__name']: float(item['total_amount']) for item in summary}
    
    return Response(result)
