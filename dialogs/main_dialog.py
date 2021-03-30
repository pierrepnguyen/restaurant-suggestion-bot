# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.core import MessageFactory, UserState, CardFactory

from botbuilder.schema import Attachment, Activity, ActivityTypes

from data_models import UserProfile
from dialogs.top_level_dialog import TopLevelDialog

indian = "recources/IndianCard.json"
korean = "recources/KoreanCard.json"
french = "recources/FrenchCard.json"
italian = "recources/ItalianCard.json"

class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_state = user_state

        self.add_dialog(TopLevelDialog(TopLevelDialog.__name__))
        self.add_dialog(
            WaterfallDialog("WFDialog", [self.initial_step, self.final_step])
        )

        self.initial_dialog_id = "WFDialog"

    async def initial_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        return await step_context.begin_dialog(TopLevelDialog.__name__)

    async def final_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        user_info: UserProfile = step_context.result

        companies = (
            "no companies"
            if len(user_info.companies_to_review) == 0
            else " and ".join(user_info.companies_to_review)
        )
        status = f"Here is a list of your request for {companies} restaurants"

        await step_context.context.send_activity(MessageFactory.text(status))

        # Iterate through choices & create cards
        for result in user_info.companies_to_review:
            message = Activity(
                type = ActivityTypes.message,
                attachments = [self._create_adaptive_card_attachment(result)]
            )
            await step_context.context.send_activity(message)

        # store the UserProfile
        accessor = self.user_state.create_property("UserProfile")
        await accessor.set(step_context.context, user_info)

        return await step_context.end_dialog()

    def _create_adaptive_card_attachment(self, result) -> Attachment:

        if(result == "Indian"):
            result = indian
        elif(result == "Korean"):
            result = korean
        elif(result == "French"):
            result = french
        elif(result == "Italian"):
            result = italian
        card_path = os.path.join(os.getcwd(), result)
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)
        
        return CardFactory.adaptive_card(card_data)