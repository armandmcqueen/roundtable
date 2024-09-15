from llmlib import LLMClient, Provider, AnthropicModel
from roundtable.conversation import Conversation
from roundtable.personas import Persona

import os


def main():
    if "ANTHROPIC_API_KEY" not in os.environ:
        raise ValueError("Please set the ANTHROPIC_API_KEY environment")
    client = LLMClient(
        provider=Provider.ANTHROPIC,
        model=AnthropicModel.CLAUDE_3_5_SONNET,
        anthropic_key=os.environ["ANTHROPIC_API_KEY"],
    )
    worrier = Persona(
        name="Reliability Focused Software Engineer",
        prompt="""You are a strong staff software engineer who is always focused about how things can fail. You do not block progress, but you are always bringing up edge cases and potential problems. You give detailed and actionable advice, including code examples where appropriate or when requested. You exhaustively enumerate the ways that something can fail."""
    )
    lawyer = Persona(
        name="Lawyer",
        prompt="You are a lawyer who points out if there is a legal aspect to consider. You are careful to only contribute when there is a meaningful legal aspect to consider and not say anything when the legal considerations are minor or unlikely to actually come up. You are happy to say 'I have nothing to contribute' for many technical discussions."
    )
    distinguished = Persona(
        name="Distinguished Engineer",
        prompt="""You are a distinguished engineer who is experienced at both large companies and startups. You are realistic about what can be done, but ambitious, bold, thoughtful and confident in your ability. You give detailed and actionable advice, including code examples where appropriate or when requested. You are always looking for the best way to do things."""
    )
    simplifying_engineer = Persona(
        name="Simplifying Engineer",
        prompt="""You are a distinguished engineer who is experienced at startups. You are realistic about what can be done, but ambitious, bold, thoughtful and confident in your ability. You give detailed and actionable advice, including code examples where appropriate or when requested. You emphasize simplicity and achievability, fighting against the common software engineering habit of increasing complexity and scope."""
    )
    conversation = Conversation(client)
    # conversation.add_participant(worrier)
    conversation.add_participant(lawyer)
    conversation.add_participant(distinguished)
    conversation.add_participant(simplifying_engineer)

    # conversation.send_message("I want to build a simple AI tool that allows me to have a chat with multiple types of people. I want to be able to build a digital board of advisors that I can consult with. Over time I will build up a number of detailed, powerful prompts that I can use to get advice on a wide range of topics. Part of the goal is to get a wide perspective on things I am considering. Another is to encode a systematic approach to decision making that I can use to make better decisions. What should I consider when designing this tool? Please provide a detailed design.")
    # conversation.send_message("I accidentally deleted a bunch of kubernetes resource with `kubectl delete -k .` when I was at the root of the project. I don't want to do that again. Should I write a wrapper script to prevent this happening again? What might that look like? Please provide a basic implementation in Python. Each person should provide their own implementation.")
    # conversation.send_message("How do I create a CLI in Typescript with dynamic and modern output similar to what I can achieve with `rich` in Python?")
    conversation.send_message("How can I create a web ui for chatting with LLMs similar to claude? I want to use webcomponents, lit, and mobx. I want to support streaming output that is visible to the user. I want to make calls out to Claude using the Typescript SDK. Please provide an implementation in Typescript. Make it visually as close to claude.ai as possible. Include instructions for how to set up a project that is able to build this web ui. Each person should provide their own implementation.")
if __name__ == '__main__':
    main()