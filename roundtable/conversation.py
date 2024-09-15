from roundtable.personas import Persona, USER_PERSONA_NAME
from roundtable.chat_message import ChatMessage
import typer

app = typer.Typer()

PersonaName = str


class Conversation:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.participants: list[Persona] = []
        self.participant_map: dict[PersonaName, Persona] = {p.name: p for p in self.participants}
        self.messages: list[ChatMessage] = []

    def add_participant(self, participant: Persona):
        self.participants.append(participant)
        self.participant_map[participant.name] = participant

    def send_message(self, message: str):
        self.messages.append(ChatMessage(text=message, sender=USER_PERSONA_NAME))
        for p in self.participants:
            response = p.contribute(self.messages, self.llm_client)
            # print(f"{response.sender}: {response.text}\n")
            print("\n\n")
            self.messages.append(response)



if __name__ == '__main__':
    app()