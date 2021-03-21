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
            label = Text(label, Text.PLAIN_TEXT, emoji=False, validate=False)

        if not isinstance(options, list):
            options = [options]

        super(OptionGroup, self).__init__(
            label=label,
            options=options
        )

        if validate:
            self.validate()

    def validate(self):
        if not isinstance(self, dict):
            raise ValueError('An \'OptionGroup\' element must be a dict object')

        # Validate Label field:
        label = self.get('label')
        try:
            Text.validate(label)
        except ValueError as err:
            raise ValueError(
                'The \'label\' parameter is not a valid \'Text\' element, '
                'see error:\n'
                f'{err}'
            )

        if len(label.get('text')) > 75:
            raise ValueError(
                'The \'label\' text object can have a \'text\' field no '
                'longer than 75 characters.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        if label.get('type') != Text.PLAIN_TEXT:
            raise ValueError(
                'The \'label\' text object must have a \'type\' field of '
                'type \'plain_text\'.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )

        # Validate Options:
        options = self.get('options')
        if not isinstance(options, list):
            raise ValueError(
                'The \'options\' parameter must be a list.\nSee https://api.'
                'slack.com/reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        if len(options) > 100:
            raise ValueError(
                'The \'options\' list can have no than 100 Option object '
                'elements.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#'
                'option_group__fields for more information.'
            )
        for element in options:
            try:
                Option.validate(element)
            except ValueError as err:
                raise ValueError(
                    'An element in the \'options\' list is not a valid '
                    f'\'Option\' element, see error:\n{err}'
                )
