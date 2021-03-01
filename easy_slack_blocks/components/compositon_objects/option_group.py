from .text import Text

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
