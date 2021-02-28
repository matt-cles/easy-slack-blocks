from .text import Text

class Confirmation(dict):
    """Slack Confirmation composition builder.

    A Slack Confirmation is a simple pop-up modal that can easily be 
    added to an action, such as a button.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#confirm
    """

    PRIMARY = CONFIRM = GREEN = 'primary'
    DANGER = DENY = RED = 'danger'


    def __init__(
        self, 
        title,
        text,
        confirm,
        deny,
        style='primary',
    ):
        if isinstance(title, str):
            title = Text(title, Text.PLAIN_TEXT, emoji=False)

        if isinstance(text, str):
            text = Text(text)

        if isinstance(confirm, str):
            confirm = Text(confirm, Text.PLAIN_TEXT, emoji=False)

        if isinstance(deny, str):
            deny = Text(deny, Text.PLAIN_TEXT, emoji=False)

        ### TODO:
        ### add element validation

        super(Confirmation, self).__init__(
            title=title,
            text=text,
            confirm=confirm,
            deny=deny,
            style=style,
        )
        