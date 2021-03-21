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
        *,
        validate=True,
    ):
        if isinstance(text, str):
            text = Text(text, Text.PLAIN_TEXT, validate=False)

        if isinstance(description, str):
            description = Text(
                description, 
                Text.PLAIN_TEXT, 
                emoji=False, 
                validate=False,
            )

        option = {
            'text': text,
            'value': value,
        }

        if description:
            option['description'] = description

        if url:
            option['url'] = url

        super(Option, self).__init__(option)

        if validate:
            self.validate()


    def validate(self):
        if not isinstance(self, dict):
            raise ValueError('An \'Option\' element must be a dict object')

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
        if len(text.get('text')) > 75:
            raise ValueError(
                'The \'text\' text object can have a \'text\' field no '
                'longer than 75 characters.\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#option__fields for '
                'more information.'
            )

        # Validate value field:
        value = self.get('value')
        if not isinstance(value, str):
            raise ValueError(
                'The \'value\' parameter must be a String\nSee https://api.'
                'slack.com/reference/block-kit/composition-objects#'
                'option__fields for more information'
            )
        if len(value) > 75:
            raise ValueError(
                'The \'value\' string can be no longer than 75 characters.\n'
                'See https://api.slack.com/reference/block-kit/composition-'
                'objects#option__fields for more information.'
            )

        # Validate description field, if present:
        description = self.get('description')
        if description:
            try:
                Text.validate(description)
            except ValueError as err:
                raise ValueError(
                    'The \'description\' parameter is not a valid \'Text\' '
                    'element, see error:\n'
                    f'{err}'
                )
            if len(description.get('text')) > 75:
                raise ValueError(
                    'The \'description\' text object can have a \'text\' '
                    'field no longer than 75 characters.\nSee https://api.'
                    'slack.com/reference/block-kit/composition-objects#'
                    'option__fields for more information.'
                )
            if description.get('type') != Text.PLAIN_TEXT:
                raise ValueError(
                    'The \'description\' text object must have a \'type\' '
                    'field of type \'plain_text\'.\nSee https://api.slack.'
                    'com/reference/block-kit/composition-objects#'
                    'option__fields for more information.'
                )

        # Validate url field, if present:
        url = self.get('url')
        if url:
            if not isinstance(url, str):
                raise ValueError(
                    'The \'url\' parameter must be a String\nSee https://api.'
                    'slack.com/reference/block-kit/composition-objects#'
                    'option__fields for more information'
                )
            if len(url) > 3000:
                raise ValueError(
                    'The \'url\' string can be no longer than 3000 '
                    'characters.\nSee https://api.slack.com/reference/block-'
                    'kit/composition-objects#option__fields for more '
                    'information.'
                )
