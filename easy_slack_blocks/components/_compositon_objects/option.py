from .text import Text

class Option(dict):
    """Slack Option composition builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#option"""
    def __init__(
        self,
        text,
        value,
        description=None,
        url=None,

    ):
        if isinstance(text, str):
            text = Text(text, Text.PLAIN_TEXT)

        if isinstance(description, str):
            description = Text(description, Text.PLAIN_TEXT, emoji=False)

        ### TODO:
        ### add element validation

        option = {
            'text': text,
            'value': value,
        }

        if description:
            option['description'] = description

        if url:
            option['url'] = url

        ### TODO:
        ### add element validation

        super(Option, self).__init__(option)
