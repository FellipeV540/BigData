from botbuilder.core import MessageFactory, UserState
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.dialogs.prompts import ChoicePrompt, PromptOptions
from botbuilder.dialogs.choices import Choice

class MainDialog(ComponentDialog):

    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__("MainDialog")

        # Guarda onde o usuário parou no diálogo
        self.user_state = user_state

        #prompt para escolher as opçoes de atendimento
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))

        #conversação Sequencial (Steps)
        self.add_dialog(
            WaterfallDialog(
                "MainDialog",
                [
                    self.prompt_option_step,
                    self.process_option_step
                ]

            )
        )

        self.initial_dialog_id = "MainDialog"

    async def prompt_option_step(self, step_context: WaterfallStepContext):
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Escolha a opção desejada:"),
                choices =[
                    Choice("Consultar Matricula"),
                    Choice("Enturmar Aluno"),
                    Choice("Quadro de Horario"),
                    Choice("Ajuda")
                ]
            )
        )
    async def process_option_step(self, step_context: WaterfallStepContext):
        #Recebe opção do usuário
        option = step_context.result.value

        if (option == "Consultar Matricula"):
            return await step_context.context.send_activity(
                MessageFactory.text(
                    "Voce escolheu a opção consultar matricula"
                )
            )
        elif (option == "Enturmar Aluno"):
            return await step_context.context.send_activity(
                MessageFactory.text(
                    "Voce escolheu a opção enturmar aluno"
                )
            )
        elif (option == "Quadro de Horario"):
            return await step_context.context.send_activity(
                MessageFactory.text(
                    "Voce escolheu a opção quadro de horario"
                )
            )
        elif (option == "Ajuda"):
            return await step_context.context.send_activity(
                MessageFactory.text(
                    "Voce escolheu a opção ajuda"
                )
            )