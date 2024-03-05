from django.test import TestCase

# Create your tests here.
from users.services import checkout_stripe_session

a = checkout_stripe_session("cs_test_a1F9E9nYBvC7AzmuNydX2X9FwzxPj5KysZinZaV8LXd6aiqwR5tYvrL9XV")

print(a['status'])
