class Investor:
    def __init__(self, name, email, context):
        self.name = name
        self.email = email
        self.context = context

    def update_context(self, new_context):
        self.context = new_context

    def get_context(self):
        return self.context
