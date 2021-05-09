from mycroft import MycroftSkill, intent_file_handler


class AwardExplainer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('explainer.award.intent')
    def handle_explainer_award(self, message):
        self.speak_dialog('explainer.award')


def create_skill():
    return AwardExplainer()

