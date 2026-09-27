from typing import Annotated, NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class BusinessDiscoveryState(TypedDict):
    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]

    industry: NotRequired[str | None]
    business_model: NotRequired[str | None]
    employee_count: NotRequired[int | None]

    order_channels: NotRequired[list[str]]
    business_processes: NotRequired[list[str]]
    pain_points: NotRequired[list[str]]

    discovery_complete: NotRequired[bool]