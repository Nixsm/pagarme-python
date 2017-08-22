# -*- coding: utf-8 -*-

from tests.resources.dictionaries import card_dictionary
from tests.resources.dictionaries import customer_dictionary
from tests.resources.dictionaries import recipient_dictionary
from tests.resources import pagarme_test
from pagarme import recipient

BOLETO_TRANSACTION = {
    'amount': '1000000',
    'payment_method': 'boleto',
    'postback_url': pagarme_test.create_postback_url()
}

CALCULATE_INTALLMENTS_AMOUNT = {'amount': '10000', 'free_installments': "1", 'interest_rate': '13',
                                'max_installments': '12'}

PAY_BOLETO = {'status': 'paid'}

REFUNDED_OR_CAPTURE_TRANSACTION = {'amount': '1000000'}

DEFAULT_RECIPIENT = recipient.default_recipient()['test']

RECIPIENT = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)

SPLIT_RULE_AMOUNT = [{'recipient_id': DEFAULT_RECIPIENT, 'amount': 500000, 'liable': 'true',
                          'charge_processing_fee': 'true'},
                         {'recipient_id': RECIPIENT['id'], 'amount': 500000, 'liable': 'true',
                          'charge_processing_fee': 'true'}]

SPLIT_RULE_PERCENTAGE = [{'recipient_id': DEFAULT_RECIPIENT, 'percentage': 50, 'liable': 'true',
                          'charge_processing_fee': 'true'},
                         {'recipient_id': RECIPIENT['id'], 'percentage': 50, 'liable': 'true',
                          'charge_processing_fee': 'true'}]

BOLETO_TRANSACTION_SPLIT_RULE_PERCENTAGE = {'amount': BOLETO_TRANSACTION['amount'], 'payment_method': BOLETO_TRANSACTION['payment_method'],
                            'split_rules': SPLIT_RULE_PERCENTAGE}

INVALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'amount': '1000000',
'card_number': card_dictionary.INVALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.INVALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.INVALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.INVALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY}

INVALID_REQUEST ={
    'amount': '1',
    'payment_method': BOLETO_TRANSACTION['payment_method']
}

VALID_CREDIT_CARD_TRANSACTION_CAPTURE_FALSE_DICTIONARY = {'amount': '1000000', 'capture': 'false',
'card_number': card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'amount': '1000000',
'card_number': card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY, 'installments': '12'}

VALID_CREDIT_CARD_TRANSACTION__WITH_POSTBACK_DICTIONARY = {'amount': '1000000',
'card_number': card_dictionary.VALID_CARD_DICTIONARY['card_number'], 'postback_url': pagarme_test.create_postback_url(),
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY_WITH_SPLIT_RULE_AMOUNT = {'amount': '1000000',
'card_number': card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY, 'split_rules': SPLIT_RULE_AMOUNT}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY_WITH_SPLIT_RULE_PERCENTAGE = {'amount': '1000000',
'card_number': card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv': card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date': card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY, 'split_rules': SPLIT_RULE_PERCENTAGE}
