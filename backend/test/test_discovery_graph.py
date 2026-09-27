from langchain_core.messages import AIMessage, HumanMessage

from app.agents.discovery.state import BusinessDiscoveryState
from app.graphs.discovery_graph import build_discovery_graph


def test_discovery_graph():
    graph = build_discovery_graph()

    initial_state: BusinessDiscoveryState = {
        "messages": [
            HumanMessage(content="I run a bakery")
        ],
        "discovery_complete": False,
    }

    result = graph.invoke(initial_state)

    assert result["discovery_complete"] is False

    assert len(result["messages"]) == 2

    assert isinstance(result["messages"][0], HumanMessage)
    assert isinstance(result["messages"][1], AIMessage)

    assert result["messages"][1].content