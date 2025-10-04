import asyncio
import config
from run_worker import PartnerOnboarding
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        PartnerOnboarding.run, "Temporal", id="onboarding-workflow", task_queue=config.TASK_QUEUE_NAME
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())