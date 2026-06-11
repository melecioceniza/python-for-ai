# The factory pattern creates objects without specifying the exact class of object to be created

class PaymentMethod:
    def process_payment(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self,amount):
        return f"Processing ${amount} via credit card"

class PayPalPayment(PaymentMethod)
    def process_payment(self, amount):
        return f"Processing ${amount}  via PayPal"

class ApplePayPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via Apple Pay"
    
class PaymentFactory:
    @staticmethod
    def create_payment_method(method_type):
        if method_type == "credit_card":
            return CreditCardPayment()
        elif method_type == "paypal":
            return PayPalPayment()
        elif method_type == "apple_pay":
            return ApplePayPayment()
        else:
            raise ValueError(f"Unknown payment method: {method_type}")
        
#Client code
payment_method = PaymentFactory.create_payment_method("credit_card")
print(payment_method.process_payment(100))
#output: Processing $100 via Credit Card