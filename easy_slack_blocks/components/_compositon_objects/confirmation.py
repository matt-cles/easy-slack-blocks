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
        *,
        validate=True,
    ):
        if isinstance(title, str):
            title = Text(title, Text.PLAIN_TEXT, emoji=False, validate=False)

        if isinstance(text, str):
            text = Text(text, validate=False)

        if isinstance(confirm, str):
            confirm = Text(
                text=confirm, 
                type=Text.PLAIN_TEXT, 
                emoji=False, 
                validate=False,
            )

        if isinstance(deny, str):
            deny = Text(deny, Text.PLAIN_TEXT, emoji=False, validate=False)

        super(Confirmation, self).__init__(
            title=title,
            text=text,
            confirm=confirm,
            deny=deny,
            style=style,
        )

        if validate:
            self.validate()

    def validate(self):
        if not isinstance(self, dict):
            raise ValueError(
                'A \'Confirmation\' element must be a dict object'
            )

        # Validate title field:
        title = self.get('title')
        Text.validate(
            self=title, 
            max_length=100, 
            required_type=Text.PLAIN_TEXT,
            element_name='title',
            reference_url=(
                'https://api.slack.com/reference/block-kit/composition-'
                'objects#confirm__fields'
            ),
        )
        # try:
        #     Text.validate(title)
        # except ValueError as err:
        #     raise ValueError(
        #         'The \'title\' parameter is not a valid \'Text\' element, '
        #         'see error:\n'
        #         f'{err}'
        #     )
        # if len(title.get('text')) > 100:
        #     raise ValueError(
        #         'The \'title\' text object can have a \'title\' field no '
        #         'longer than 100 characters.\nSee https://api.slack.com/'
        #         'reference/block-kit/composition-objects#confirm__fields for '
        #         'more information.'
        #     )
        # if title.get('type') != Text.PLAIN_TEXT:
        #     raise ValueError(
        #         'The \'title\' text object must have a \'type\' field of '
        #         'type \'plain_text\'.\nSee https://api.slack.com/reference/'
        #         'block-kit/composition-objects#confirm__fields for more '
        #         'information.'
        #     )

        # Validate text field:
        text = self.get('text')
        try:
            Text.validate(text)
        except ValueError as err:
            raise ValueError(
                'The \'text\' parameter is not a valid \'Text\' element, see '
                'error:\n'
                f'{err}'
            )
        if len(text.get('text')) > 300:
            raise ValueError(
                'The \'text\' text object can have a \'text\' field no '
                'longer than 300 characters.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#confirm__fields for '
                'more information.'
            )

        # Validate confirm field:
        confirm = self.get('confirm')
        try:
            Text.validate(confirm)
        except ValueError as err:
            raise ValueError(
                'The \'confirm\' parameter is not a valid \'Text\' element, '
                'see error:\n'
                f'{err}'
            )
        if len(confirm.get('text')) > 30:
            raise ValueError(
                'The \'confirm\' text object can have a \'text\' field no '
                'longer than 30 characters.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#confirm__fields for '
                'more information.'
            )
        if confirm.get('type') != Text.PLAIN_TEXT:
            raise ValueError(
                'The \'confirm\' text object must have a \'type\' field of '
                'type \'plain_text\'.\nSee https://api.slack.com/reference/'
                'block-kit/composition-objects#confirm__fields for more '
                'information.'
            )

        # Validate deny field:
        deny = self.get('deny')
        try:
            Text.validate(deny)
        except ValueError as err:
            raise ValueError(
                'The \'deny\' parameter is not a valid \'Text\' element, see '
                'error:\n'
                f'{err}'
            )
        if len(deny.get('text')) > 30:
            raise ValueError(
                'The \'deny\' text object can have a \'text\' field no '
                'longer than 30 characters.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#confirm__fields for '
                'more information.'
            )
        if deny.get('type') != Text.PLAIN_TEXT:
            raise ValueError(
                'The \'deny\' text object must have a \'type\' field of '
                'type \'plain_text\'.\nSee https://api.slack.com/reference/'
                'block-kit/composition-objects#confirm__fields for more '
                'information.'
            )

        # Validate Style, if present:
        style = self.get('style')
        if style:
            if style not in [Confirmation.DANGER, Confirmation.PRIMARY]:
                raise ValueError(
                    'The \'style\' parameter must be a String with a value '
                    f'of either {Confirmation.PRIMARY} or '
                    f'{Confirmation.DANGER}.\nSee https://api.slack.com/'
                    'reference/block-kit/composition-objects#confirm__fields '
                    'for more information.'
                )

