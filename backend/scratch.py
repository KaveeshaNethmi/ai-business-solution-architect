from typing import cast

from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from app.agents.discovery.state import BusinessDiscoveryState
from app.graphs.discovery_graph import build_discovery_graph


graph = build_discovery_graph()


config: RunnableConfig = {
    "configurable": {
        "thread_id": "business-001"
    }
}

second_config: RunnableConfig = {
    "configurable": {
        "thread_id": "business-002"
    }
}

# ==========================================
# TURN 1
# ==========================================

result = cast(
    BusinessDiscoveryState,
    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="I run a small bakery."
                )
            ]
        },
        config=config,
    ),
)


print("\n========== TURN 1 ==========")
print("Industry:", result.get("industry"))
print("Agent:", result["messages"][-1].content)

# ==========================================
# TURN 2
# ==========================================

result = cast(
    BusinessDiscoveryState,
    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "Most customers place orders through "
                        "WhatsApp and phone calls."
                    )
                )
            ]
        },
        config=config,
    ),
)


print("\n========== TURN 2 ==========")

print("Industry:", result.get("industry"))
print("Order channels:", result.get("order_channels"))
print("Agent:", result["messages"][-1].content)

# ==========================================
# TURN 3
# ==========================================

result = cast(
    BusinessDiscoveryState,
    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "We sell all the bakery items like bread, buns, pastries and cakes, cookies too "
                        "Also We write the orders in a notebook. "
                        "During busy periods we sometimes forget "
                        "to write an order down."
                    )
                )
            ]
        },
        config=config,
    ),
)


print("\n========== TURN 3 ==========")

print("Industry:", result.get("industry"))
print("Order channels:", result.get("order_channels"))
print("Business processes:", result.get("business_processes"))
print("Pain points:", result.get("pain_points"))
print("Discovery complete:", result.get("discovery_complete"))

print("\nAgent:")
print(result["messages"][-1].content)


second_result = cast(
    BusinessDiscoveryState,
    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "We have about 50 customers every day."
                    )
                )
            ]
        },
        config=second_config,
    ),
)
print("\n========== FULL CONVERSATION ==========")


for message in result["messages"]:
    print(
        f"{type(message).__name__}: "
        f"{message.content}"
    )

print("\n========== SECOND THREAD ==========")

for message in second_result["messages"]:
    print(
        f"{type(message).__name__}: "
        f"{message.content}"
    )