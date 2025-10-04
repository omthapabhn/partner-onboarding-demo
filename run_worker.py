import asyncio
import config
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import start_onboarding
from workflows import PartnerOnboarding

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue=config.TASK_QUEUE_NAME, workflows=[PartnerOnboarding], activities=[start_onboarding]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())