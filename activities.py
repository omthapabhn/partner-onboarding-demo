from temporalio import activity

@activity.defn
async def start_onboarding(name: str) -> str:
    return f"Started Partner Onboarding : {name}!"
