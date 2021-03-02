from .. import Text

class Button(dict):
    """Generate a Button element.

    See Slack documentation for the Button Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#button
    """
    DEFAULT = STANDARD = GREY = 'default'
    PRIMARY = CONFIRM = GREEN = 'primary'
    DANGER = DENY = RED = 'danger'

    def __init__(
        self, 
        text,
        action_id,
        *,
        url=None,
        value=None,
        style=None,
        confirm=None,
    ):
        if isinstance(text, str):
            text = Text(text, Text.PLAIN_TEXT)

        button = {
            'type': 'button',
            'text': text,
            'action_id': action_id,
        }

        if url:
            button['url'] = url

        if value:
            button['value'] = value

        if style:
            button['style'] = style

        if confirm:
            button['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(Button, self).__init__(button)
        