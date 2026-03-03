from django.shortcuts import render
from faker import Faker


# Create your views here.

from django.http import JsonResponse

def personal_transactions(request):
    transactions_data = [
  {
    "id": "TXN-782910",
    "timestamp": "2026-03-01T10:15:30Z",
    "description": "Starbucks Coffee",
    "category": "Food & Drink",
    "amount": -6.50,
    "currency": "USD",
    "status": "completed",
    "merchant": "Starbucks #4421"
  },
  {
    "id": "TXN-782911",
    "timestamp": "2026-03-01T14:45:00Z",
    "description": "Salary Deposit",
    "category": "Income",
    "amount": 2500.00,
    "currency": "USD",
    "status": "completed",
    "merchant": "TechCorp Industries"
  },
  {
    "id": "TXN-782912",
    "timestamp": "2026-03-02T09:12:15Z",
    "description": "Monthly Rent",
    "category": "Housing",
    "amount": -1200.00,
    "currency": "USD",
    "status": "pending",
    "merchant": "Skyline Properties"
  },
  {
    "id": "TXN-782913",
    "timestamp": "2026-03-02T18:30:00Z",
    "description": "Amazon Prime Subs",
    "category": "Entertainment",
    "amount": -14.99,
    "currency": "USD",
    "status": "completed",
    "merchant": "Amazon.com"
  },
  {
    "id": "TXN-782914",
    "timestamp": "2026-03-03T11:05:45Z",
    "description": "Gas Station",
    "category": "Transport",
    "amount": -45.20,
    "currency": "USD",
    "status": "completed",
    "merchant": "Shell Oil"
  }
]
    
    return JsonResponse(transactions_data, safe=False)


def business_transactions(request):
    # Generate fake business transactions using Faker
    fake = Faker()
    business_transactions_data = []
    for _ in range(5):
        transaction = {
            "id": f"BUS-{fake.unique.random_number(digits=6)}",
            "timestamp": fake.iso8601(),
            "description": fake.catch_phrase(),
            "category": fake.bs(),
            "amount": round(fake.random_number(digits=4) + fake.random.random(), 2),
            "currency": "USD",
            "status": fake.random_element(elements=("completed", "pending", "failed")),
            "merchant": fake.company()
        }
        business_transactions_data.append(transaction)
    
    return JsonResponse(business_transactions_data, safe=False)
