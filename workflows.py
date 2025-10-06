import asyncio
from datetime import timedelta
from activities import OnboardingActivities
from config import PartnerDetails

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import OnboardingActivities
    from config import PartnerDetails


@workflow.defn
class PartnerOnboarding:
    @workflow.run
    async def run(self, partner_details: PartnerDetails) -> str:
        retry_policy = RetryPolicy(
            maximum_attempts=3,
            maximum_interval=timedelta(seconds=2),
            non_retryable_error_types=["InvalidPartnerError", "InsufficientDataError"],
        )

        ### workflow for partner onboarding create Legacy Entity
        legal_entity_result = await workflow.execute_activity_method(
            OnboardingActivities.create_legacy_entity, 
            partner_details, 
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )

         ### workflow for partner onboarding create Client Entity
        client_entity_result = await workflow.execute_activity_method(
            OnboardingActivities.create_client_entity,
            partner_details,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )

         ### workflow for partner onboarding create Teanant Entity
        tenant_entity_result = await workflow.execute_activity_method(
            OnboardingActivities.create_tenant_entity,
            partner_details,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )

         ### workflow for partner onboarding create Account Entity
        future_result1 = workflow.execute_activity_method(
            OnboardingActivities.create_account_entity,
            partner_details,            
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )

         ### workflow for partner onboarding create Channel Entity
        future_result2 = workflow.execute_activity_method(
            OnboardingActivities.create_channel_entity,
            partner_details,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )

        ### Do other workflow logic while 2 and 3 run
        await workflow.sleep(2)

        # Wait for both to complete
        # await workflow.wait(future_result1)
        # await workflow.wait(future_result2)
        
        ### Wait for async activities to complete
        account_entity_result = await future_result1
        channel_entity_result = await future_result2

        ### Start multiple activities in parallel and wait for all
        # results = await asyncio.gather(
        # workflow.execute_activity_method(OnboardingActivities.create_account_entity, partner_details, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy),
        # workflow.execute_activity_method(OnboardingActivities.create_legacy_entity, partner_details, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy)
        # )

        # account_entity_result, legacy_entity_result = results