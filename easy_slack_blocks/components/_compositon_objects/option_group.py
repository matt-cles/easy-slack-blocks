from .text import Text
from .option import Option

class OptionGroup(dict):
    """Slack Option composition builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """
    def __init__(
        self,
        label,
        options,
        *,
        validate=True
    ):
        if isinstance(label, str):
            label = Text(label, Text.PLAIN_TEXT, emoji=False)

        if not isinstance(options, list):
            options = [options]

        super(OptionGroup, self).__init__(
            label=label,
            options=options
        )

        if validate:
            self.validate()

    def validate(self):
        if len(self.get('label').get('text')) > 75:
            raise ValueError(
                'The \'label\' text object can have a \'text\' field no '
                'longer than 75 characters.\n See https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        if self.get('label').get('type') != Text.PLAIN_TEXT:
            raise ValueError(
                'The \'label\' text object must have a \'type\' field of '
                'type \'plain_text\'.\n See https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        if len(self.get('options')) > 100:
            raise ValueError(
                'The \'options\' list can have no than 100 Option object '
                'elements.\n See https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        for element in self.get('options'):
            try:
                Option.validate(element)
            except ValueError as err:
                print(err)

