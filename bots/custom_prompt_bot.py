from botbuilder.core import (
  ActivityHandler,
  ConversationState,
  TurnContext,
  UserState,
  # MessageFactory,
)
# from botbuilder.schema import ChannelAccount

class CustomPromptBot(ActivityHandler):
    def __init__(self, conversation_state: ConversationState,
    user_state: UserState):
        if conversation_state is None:
            raise TypeError(
                "[CustomPromptBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[CustomPromptBot]: Missing parameter. user_state is required but None was given"
            )

        self.conversation_state = conversation_state
        self.user_state = user_state

