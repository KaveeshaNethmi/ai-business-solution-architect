from pydantic import BaseModel, Field


class DiscoveryChatRequest(BaseModel):
    message: str = Field(
        ..., min_length=1,
        description="The business owner's message"
        )


class DiscoveryChatResponse(BaseModel):
    reply: str
    discovery_complete: bool = False


class DiscoveryResult(BaseModel):
    industry: str | None = None
    business_model: str | None = None
    employee_count: int | None = None

    order_channels: list[str] = Field(default_factory=list)
    pain_points: list[str] = Field(default_factory=list)

    reply: str
    discovery_complete: bool
