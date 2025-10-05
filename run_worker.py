# @@@SNIPSTART run-worker
import asyncio
import config
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import OnboardingActivities
from workflows import PartnerOnboarding

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    activities = OnboardingActivities()
    worker = Worker(
        client, 
        task_queue=config.TASK_QUEUE_NAME, 
        workflows=[PartnerOnboarding], 
        activities=[activities.create_legacy_entity, 
                    activities.create_client_entity, 
                    activities.create_tenant_entity, 
                    activities.create_account_entity,
                    activities.create_channel_entity]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())

# @@@SNIPEND