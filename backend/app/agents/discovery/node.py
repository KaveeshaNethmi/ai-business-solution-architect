from typing import cast

from langchain_core.messages import BaseMessage, AIMessage, SystemMessage

from app.agents.discovery.state import BusinessDiscoveryState
from app.services.llm import get_llm
from app.schemas.discovery import DiscoveryResult
from app.agents.discovery.prompts import DISCOVERY_SYSTEM_PROMPT


def discovery_node(
    state: BusinessDiscoveryState,
) -> BusinessDiscoveryState:

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        DiscoveryResult
    )
    # print("structured_llm", structured_llm)

    messages: list[BaseMessage] = [
        SystemMessage(content=DISCOVERY_SYSTEM_PROMPT),
        *state.get("messages", []),
    ]
    # print("result 1", structured_llm.invoke(messages))

    result = cast(
        DiscoveryResult,
        structured_llm.invoke(messages)
    )
    # print("result", result)

    return {
        "messages": [
            AIMessage(content=result.reply)
        ],
        "industry": result.industry,
        "business_model": result.business_model,
        "employee_count": result.employee_count,
        "order_channels": result.order_channels,
        "pain_points": result.pain_points,
        "discovery_complete": result.discovery_complete,
    }