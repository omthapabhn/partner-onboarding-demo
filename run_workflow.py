# @@@SNIPSTART run-workflow
import asyncio
import traceback
import uuid
import config
from run_worker import PartnerOnboarding
from temporalio.client import Client, WorkflowFailureError


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    data: config.PartnerDetails = config.PartnerDetails(
        partner_name="Test Partner",
        client_id="client_123",
        legal_entity_id=1,
        tenant_id="tenant_123",
        reference_id=str(uuid.uuid4()),
        contact_details=config.ContactDetails(
            address_1="123 Main St",
            address_2="Suite 100",
            address_type="Business",
            contact_type=1,
            contact_number="555-1234",
            email="test@example.com" 
        ),
        payment_details=config.PaymentDetails(
            account_number="123456789",
            bank_name="Test Bank",
            bank_code="TB123",
            payment_type="Credit",
            currency="USD",
            is_primary=True 
        )
    )

    try:
        # Execute a workflow
        result = await client.execute_workflow(
            PartnerOnboarding.run, 
            data, 
            id="onboarding-workflow", 
            task_queue=config.TASK_QUEUE_NAME
        )

        print(f"Result: Onboard Workflow completed successfully.")
    except WorkflowFailureError:
        print("Got expected exception: ", traceback.format_exc())

if __name__ == "__main__":
    asyncio.run(main())

# @@@SNIPEND