from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import start_onboarding

@workflow.defn
class PartnerOnboarding:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            start_onboarding, name, start_to_close_timeout=timedelta(seconds=5)
        )