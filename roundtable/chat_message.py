from pydantic import BaseModel

PersonaName = str

class ChatMessage(BaseModel):
    text: str
    sender: PersonaName