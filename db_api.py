class User:
    _id: int = None,
    last_text: str = ''
    last_prompt_time: int = 0

    def __init__(self, _id: int,
                 last_text='',
                 last_prompt_time=0):
        self.id = _id
        self.last_text = last_text
        self.last_prompt_time = last_prompt_time

    def lookup_in_db(self):
        # TODO implement
        # user = users.get(id, {'id': id, 'last_text': '', 'last_prompt_time': 0})
        # users[id] = user
        pass

    def is_in_db(self):
        # TODO everything
        # query db if user is there
        return False

    def clear_context(self):
        self.last_text = ''
        self.last_prompt_time = 0
        # TODO pass this to db


