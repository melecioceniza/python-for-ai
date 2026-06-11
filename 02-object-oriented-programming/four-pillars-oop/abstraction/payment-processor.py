# Abstraction focuses on hiding complex implementation details and showing only the necessary features of an object.

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via credit card")
        # complex credit card processing logi here


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Paypal")
        # complex PayPal processing logic here


# The abstract base class PaymentProcessor defines a common interface that all concrete payment processors must implement.
