from random import choices, randint
from string import ascii_letters, digits
from faker import Faker

fake = Faker(4321)

account_chars: str = digits + ascii_letters

currency = ['EUR', 'USD', 'GBP']

countries = ['US', 'UK', 'DE']

payment_method = ['VISA', 'PAYPAL', 'MASTERCARD']


def _random_date() -> str:
    """Return a random date"""
    return "".join(str(fake.date_time_between(start_date="-30d", end_date="now")))


def _random_name() -> str:
    """Return a random name"""
    return fake.name()


def _random_country() -> str:
    """Return a random country name from a list"""
    return "".join(choices(countries, k=1))


def _random_currency() -> str:
    """Return a random currency code"""
    return "".join(choices(currency, k=1))


def _random_cc_exp() -> str:
    """Return a random credit card expiration date"""
    return fake.credit_card_expire()


def _random_amount() -> float:
    """Return a random amount between 1.00 and 1000.00"""
    return randint(100, 1000000) / 100


def _random_cc_provider() -> str:
    """Return a random credit card provider"""
    return "".join(choices(payment_method, k=1))


def _random_account_id() -> str:
    """Return a random account number made of 12 characters"""
    return "".join(choices(digits, k=4))


def _random_address() -> str:
    """Return a random address"""
    return fake.address()


def create_random_transaction() -> dict:
    """Create a fake randomised transaction."""
    return {
        "id": _random_account_id(),
        "date": _random_date(),
        "name": _random_name(),
        "country": _random_country(),
        "currency": _random_currency(),
        "amount": _random_amount(),
        "payment_method": _random_cc_provider(),
        "exp": _random_cc_exp(),
        "address": _random_address(),

    }
