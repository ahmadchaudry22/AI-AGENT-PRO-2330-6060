# =========================
# agent_pro_demo.py
# =========================

from typing import List, Any, Dict


# ---------- 1. Simple agent ---------- #
class SimpleAgentPro:
    """A one-shot code generator (stub)."""

    def run(self, prompt: str) -> str:
        print(f"[SimpleAgentPro] Generating code for: “{prompt}”")

        # Hard-coded example payload
        if "fibonacci" in prompt.lower():
            code = (
                "def fibonacci(n):\n"
                "    a, b = 0, 1\n"
                "    for _ in range(n):\n"
                "        yield a\n"
                "        a, b = b, a + b\n"
            )
        else:
            code = "# TODO: implement code generation logic here"

        print("\n--- Generated Code ---\n" + code)
        return code


# ---------- 2. Tool abstractions ---------- #
class Tool:
    name: str = "base_tool"

    def __call__(self, query: str) -> Any:
        raise NotImplementedError


class CodeEngine(Tool):
    name = "code_engine"

    def __call__(self, query: str) -> str:
        return f"[CodeEngine] 🔧 Generated demo code for: “{query}”"


class SimplifiedSearchTool(Tool):
    name = "search"

    def __call__(self, query: str) -> Dict[str, Any]:
        return {
            "snippet": f"[Search] Top result for “{query}”.",
            "link": "https://example.com"
        }


class SlideGenerationTool(Tool):
    name = "slides"

    def __call__(self, query: str) -> str:
        return f"[Slides] 📊 Dummy slide deck created for: “{query}”"


# ---------- 3. ReAct-style multi-tool agent ---------- #
class AgentPro:
    """Very small ‘ReAct’-flavoured agent orchestrator (toy example)."""

    def __init__(self, tools: List[Tool]) -> None:
        self.lookup = {tool.name: tool for tool in tools}

    def _select_tool(self, prompt: str) -> Tool:
        """Naïve router: choose tool based on keywords."""
        if any(k in prompt.lower() for k in ["code", "function", "algorithm"]):
            return self.lookup["code_engine"]
        if "slide" in prompt.lower() or "visual" in prompt.lower():
            return self.lookup["slides"]
        return self.lookup["search"]

    def __call__(self, prompt: str) -> Any:
        tool = self._select_tool(prompt)
        print(f"[AgentPro] Delegating to {tool.name} …")
        return tool(prompt)


# ---------- 4. Interactive chatbot ---------- #
class ChatBot:
    """Bare-bones console chatbot; type 'exit' to quit."""

    def chat(self) -> None:
        print("🤖 ChatBot ready! (type 'exit' to leave)\n")
        while True:
            user = input("You > ")
            if user.strip().lower() == "exit":
                print("ChatBot > Bye!")
                break
            response = f"Echo: {user}"
            print(f"ChatBot > {response}")


# ---------- 5. Demo run ---------- #
if __name__ == "__main__":
    # 1. Simple code generation
    simple_agent = SimpleAgentPro()
    simple_agent.run("create a fibonacci function")

    # 2. ReAct agent with multiple tools
    agent = AgentPro(
        tools=[CodeEngine(), SimplifiedSearchTool(), SlideGenerationTool()]
    )
    result = agent("Create a visualization of sorting algorithms")
    print(result)

    # 3. Interactive chatbot (commented out for non-interactive runs)
    # chatbot = ChatBot()
    # chatbot.chat()
