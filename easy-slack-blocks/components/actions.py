class Action(dict):
    """A simple subclass of dict.
    
    The purpose of this class is to have a single object that all actions 
    """
    def __init__(self, *args, **kwargs):
        super(Action, self).__init__(*args, **kwargs)


class Button(Action):
    """docstring for Button"""
    DEFAULT = STANDARD = GREY = 'default'
    PRIMARY = CONFIRM = GREEN = 'primary'
    DANGER = DENY = RED = 'danger'

    def __init__(self, arg):
        super(Button, self).__init__()
        self.arg = arg
        