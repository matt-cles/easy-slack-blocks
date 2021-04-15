class Text(dict):
    """docstring for Text.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#text
    """
    MRKDWN = MARKDOWN = RICH = 'mrkdwn'
    PLAIN_TEXT = PLAIN = 'plain_text'

    def __init__(
        self, 
        text, 
        type='mrkdwn', 
        *, 
        emoji=None, 
        verbatim=None,
        validate=True,
    ):
        text_dict = {
            'text': text,
            'type': type,
        }

        if emoji:
            text_dict['emoji'] = emoji

        if verbatim:
            text_dict['verbatim'] = verbatim

        super(Text, self).__init__(text_dict)

        if validate:
            self.validate()

    def validate(
        self,
        max_length=None,
        required_type=None,
        element_name=None,
        reference_url=(
            'https://api.slack.com/reference/block-kit/composition-objects#'
            'text__fields'
        ),
    ):
        # Preformat error message start/end
        if element_name:
            element = f'The \'{element_name}\' Text object'
        else:
            element = f'A Text object'
        error_tag_line = (
            f'\nSee {reference_url} for more information'
        )

        if not isinstance(self, dict):
            raise ValueError(
                f'{element} must be a dict object{error_tag_line}'
            )

        # Validate text
        text = self.get('text')
        if not isinstance(text, str) or len(text) <= 0:
            raise ValueError(
                f'{element} \'text\' parameter must be a non-empty String'
                f'{error_tag_line}'
            )
        # Validate type, and remaining parameters based on type
        text_type = self.get('type')
        if text_type == Text.MRKDWN:
            if self.get('emoji') is not None:
                raise ValueError(
                    f'{element} \'emoji\' parameter is only usable when '
                    f'\'type\' is \'plain_text\'.{error_tag_line}'
                )
            verbatim = self.get('verbatim')
            if verbatim is not None and not isinstance(verbatim, bool):
                raise ValueError(
                    f'{element} \'verbatim\' parameter must be a Boolean if '
                    f'included.{error_tag_line}'
                )
        elif text_type == Text.PLAIN_TEXT:
            if self.get('verbatim') is not None:
                raise ValueError(
                    f'{element} \'verbatim\' parameter is only usable when '
                    f'\'type\' is \'mrkdwn\'.{error_tag_line}'
                )
            emoji = self.get('emoji')
            if emoji is not None and not isinstance(emoji, bool):
                raise ValueError(
                    f'{element} \'emoji\' parameter must be a Boolean if '
                    f'included.{error_tag_line}'
                )
        else:
            raise ValueError(
                f'{element} \'type\' parameter must be present and either be '
                f'\'mrkdwn\' or \'plain_text\'{error_tag_line}'
            )

        if max_length:
            if len(text) > max_length:
                raise ValueError(
                    f'{element} \'text\' parameter can be no longer than '
                    f'{max_length} characters.{error_tag_line}'
                )

        if required_type:
            if text_type != required_type:
                raise ValueError(
                    f'{element} \'type\' parameter must be {required_type}.'
                    f'{error_tag_line}'
                )
