import asyncio

from temporalio import activity

from bloom_service import BloomService, InvalidPartnerError, InsufficientDataError
from config import PartnerDetails

### Activities are where you perform the business logic for your application. 
### In the money transfer application, you have three Activity methods, withdraw(), deposit(), and refund(). 
class OnboardingActivities:
    def __init__(self):
        self.bloom = BloomService("api.bhnetwork.com")

    # @@@SNIPSTART create_legacy_entity
    @activity.defn
    async def create_legacy_entity(self, data: PartnerDetails) -> str:
        try:
            confirmation = await asyncio.to_thread(
                self.bloom.create_legacy_entity, data
            )
            return confirmation
        except InvalidPartnerError:
            raise
        except Exception:
            activity.logger.exception("InvalidPartnerError failed")
            raise
    # @@@SNIPEND

    # @@@SNIPSTART create_client_entity
    @activity.defn
    async def create_client_entity(self, data: PartnerDetails) -> str:
        
        try:
            confirmation = await asyncio.to_thread(
                self.bloom.create_client_entity, data
            )
            
            return confirmation
        except InvalidPartnerError:
            raise
        except Exception:
            activity.logger.exception("InvalidPartnerError failed")
            raise

    # @@@SNIPEND

    # @@@SNIPSTART create_tenant_entity
    @activity.defn
    async def create_tenant_entity(self, data: PartnerDetails) -> str:

        try:
            confirmation = await asyncio.to_thread(
                self.bloom.create_tenant_entity, data
            )
            return confirmation
        except InvalidPartnerError:
            raise
        except Exception:
            activity.logger.exception("InvalidPartnerError failed")
            raise

    # @@@SNIPEND

    # @@@SNIPSTART create_account_entity
    @activity.defn
    async def create_account_entity(self, data: PartnerDetails) -> str:
        
        try:
            confirmation = await asyncio.to_thread(
                self.bloom.create_account_entity, data
            )
            return confirmation
        except InsufficientDataError:
            raise
        except Exception:
            activity.logger.exception("InsufficientDataError failed")
            raise

    # @@@SNIPEND


    # @@@SNIPSTART create_channel_entity
    @activity.defn
    async def create_channel_entity(self, data: PartnerDetails) -> str:
        
        try:
            confirmation = await asyncio.to_thread(
                self.bloom.create_channel_entity, data
            )
            return confirmation
        except InsufficientDataError:
            raise
        except Exception:
            activity.logger.exception("InsufficientDataError failed")
            raise

    # @@@SNIPEND