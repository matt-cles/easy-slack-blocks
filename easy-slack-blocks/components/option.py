from .text import text

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

class OptionGroup(dict):
    """Slack Option composition builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """
    def __init__(
        self,
        label,
        options,
    ):
        if isinstance(label, str):
            label = Text(label, Text.PLAIN_TEXT, emoji=False)

        if not isinstance(options, list):
            options = [options]

        ### TODO:
        ### add element validation

        super(OptionGroup, self).__init__(
            label=label,
            options=options
        )