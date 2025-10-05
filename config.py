# @@@SNIPSTART config details
from dataclasses import dataclass
from logging import config


TASK_QUEUE_NAME = "partner-onboarding-queue"

@dataclass
class PartnerDetails:
    partner_name: str
    client_id: str
    legal_entity_id: int
    tenant_id: str
    reference_id: str
    contact_details: 'ContactDetails'
    payment_details: 'PaymentDetails'

@dataclass
class ContactDetails:
    address_1: str
    address_2: str
    address_type: str
    contact_type: int
    contact_number: str
    email: str

@dataclass
class PaymentDetails:
    account_number: str
    bank_name: str
    bank_code: str
    payment_type: str
    currency: str
    is_primary: bool

# @@@SNIPEND