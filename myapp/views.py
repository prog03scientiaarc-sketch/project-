from django.http import HttpResponse
from .models import Item

def home_view(request):
    # Fetch all records from PostgreSQL
    items = Item.objects.all()
    
    if items.exists():
        item_names = ", ".join([item.name for item in items])
        return HttpResponse(f"Items in Database: {item_names}")
    else:
        return HttpResponse("Database connected successfully! No items found yet.")