""" This code simulates a client for a hypothetical bloom service.
It supports all the functionalities for partner onboarding, and generates a random transaction ID for each request.

Tip: You can modify these functions to introduce delays or errors, allowing you to experiment with failures and timeouts.
"""
import uuid
from dataclasses import dataclass
from typing import NoReturn
from config import PartnerDetails

### Custom exception classes for handling bloom errors.

@dataclass
class InvalidPartnerError(Exception):
    """Exception for invalid partner details.

    Attributes:
        message: The message to display.

    Args:
        message: The message to display.

    """

    def __init__(self, message) -> None:
        self.message: str = message
        super().__init__(self.message)


@dataclass
class InsufficientDataError(Exception):
    """Exception for handling insufficient data.

    Attributes:
        message: The message to display.

    Args:
        message: The message to display.

    """

    def __init__(self, message) -> None:
        self.message: str = message
        super().__init__(self.message)



### A mock implementation of a bloom API.

@dataclass
class BloomService:
    """
    A mock implementation of a bloom API.

    The BloomService class provides methods for simulating parnter onboarding APIs.

    Attributes:
        hostname: The hostname of the bloom API service.
    """

    def __init__(self, hostname: str) -> None:
        """
        Constructs a new BloomService object with the given hostname.

        Args:
            hostname: The hostname of the bloom API service.
        """
        self.hostname: str = hostname

    def create_legacy_entity(self, partner_details: PartnerDetails) -> str:
        """
        Simulates the creation of a legacy entity for a partner.

        Args:
            partner_details: The details of the partner.

        Returns:
            A transaction ID.
        """
        return self.generate_transaction_id("LE")

    def create_client_entity(self, partner_details: PartnerDetails) -> str:
        """
        Simulates the creation of a client entity for a partner.

        Args:
            partner_details: The details of the partner.

        Returns:
            A transaction ID.
        """
        return self.generate_transaction_id("CE")

    def create_tenant_entity(self, partner_details: PartnerDetails) -> str:
        """
        Simulates the creation of a tenant entity for a partner.

        Args:
            partner_details: The details of the partner.

        Returns:
            A transaction ID.
        """
        return self.generate_transaction_id("TE")

    def create_account_entity(self, partner_details: PartnerDetails) -> str:
        """
        Simulates the creation of an account entity for a partner.

        Args:
            partner_details: The details of the partner.

        Returns:
            A transaction ID.
        """
        return self.generate_transaction_id("AE")

    def create_channel_entity(self, partner_details: PartnerDetails) -> str:
        """
        Simulates the creation of a channel entity for a partner.

        Args:
            partner_details: The details of the partner.

        Returns:
            A transaction ID.
        """
        return self.generate_transaction_id("CHE")

    def generate_transaction_id(self, prefix: str) -> str:
        """
        Generates a transaction ID we can send back.

        Args:
            prefix: A prefix so you can identify the type of transaction.

        Returns:
            The transaction id.
        """
        return f"{prefix}-{uuid.uuid4()}"