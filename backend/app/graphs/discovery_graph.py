from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from app.agents.discovery.node import discovery_node
from app.agents.discovery.state import BusinessDiscoveryState

checkpointer = InMemorySaver()

def build_discovery_graph():
    builder = StateGraph(BusinessDiscoveryState)

    builder.add_node(
        "discovery_agent",
        discovery_node
    )

    builder.add_edge(
        START,
        "discovery_agent"
    )

    builder.add_edge(
        "discovery_agent",
        END
    )

    return builder.compile(
        checkpointer=checkpointer
    )
