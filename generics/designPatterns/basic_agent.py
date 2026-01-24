from typing import List, Dict, Callable
import json

class AgentState:
    def __init__(self, goal: str):
        self.goal = goal
        self.memory: List[str] = []
        self.step = 0


def search_tool(query: str) -> str:
    # placeholder for a real search API
    return f"Search results for: {query}"

def think_tool(thought: str) -> str:
    return f"Thought recorded: {thought}"

TOOLS: Dict[str, Callable[[str], str]] = {
    "search": search_tool,
    "think": think_tool,
}


def llm_decide(goal: str, memory: List[str]) -> Dict:
    """
    Normally this would be an LLM call.
    Returns structured action + input.
    """
    if not memory:
        return {"action": "think", "input": f"I should research how to achieve: {goal}"}
    else:
        return {"action": "search", "input": goal}


def run_agent(goal: str, max_steps: int = 3):
    """
    Agent loop
    """
    state = AgentState(goal)

    while state.step < max_steps:
        print(f"\n--- Step {state.step} ---")

        decision = llm_decide(state.goal, state.memory)
        action = decision["action"]
        action_input = decision["input"]

        print("Decision:", decision)

        result = TOOLS[action](action_input)
        print("Action Result:", result)

        state.memory.append(result)
        state.step += 1

    print("\nFinal Memory:")
    for m in state.memory:
        print("-", m)


if __name__ == "__main__":
    run_agent("Learn the basics of reinforcement learning")