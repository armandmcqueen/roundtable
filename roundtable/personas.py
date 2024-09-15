from pydantic import BaseModel
from roundtable.chat_message import ChatMessage
from llmlib import LLMClient, TextMessage, Role, print_stream
from pathlib import Path

USER_PERSONA_NAME = "USER"

BASE_SYSTEM_PROMPT = (Path(__file__).parent / "system_prompt.txt").read_text()

class Persona(BaseModel):
    name: str
    description: str = ""
    prompt: str

    def build_system_prompt(self) -> str:
        p = BASE_SYSTEM_PROMPT + "\n\n"
        p += f"You are named {self.name}. Description: {self.prompt}"
        return p

    def contribute(
            self,
            preceding_msgs: list[ChatMessage],
            llm_client: LLMClient
    ) -> ChatMessage:
        messages = []

        messages.append(TextMessage(content=self.build_system_prompt(), role=Role.SYSTEM))

        for msg in preceding_msgs:
            assert isinstance(msg, ChatMessage), "All preceding messages must be ChatMessage objects"
            prev_msg = f"{msg.sender}: {msg.text}\n\n"
            messages.append(TextMessage(content=prev_msg, role=Role.USER))
        messages.append(TextMessage(content=f"Please add {self.name}'s response. Return only the response itself.", role=Role.USER))

        stream = llm_client.chat_stream(messages=messages)
        print(f"[{self.name}]")
        content = print_stream(stream)

        msg = ChatMessage(
            text=content,
            sender=self.name
        )
        return msg

