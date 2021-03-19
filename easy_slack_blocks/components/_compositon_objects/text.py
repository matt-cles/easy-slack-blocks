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

    def validate(self):
        if not isinstance(self, dict):
            raise ValueError('A \'Text\' element must be a dict object')

        if not isinstance(self.get('text'), str):
            raise ValueError(
                'The \'text\' parameter must be a String\nSee https://api.'
                'slack.com/reference/block-kit/composition-objects#'
                'text__fields for more information'
            )

        if self.get('type') == Text.MRKDWN:
            if self.get('emoji') is not None:
                raise ValueError(
                    'The \'emoji\' parameter is only usable when '
                    '\'type\' is \'plain_text\'.\nSee https://api.slack.com/'
                    'reference/block-kit/composition-objects#text__fields '
                    'for more information'
                )
            verbatim = self.get('verbatim')
            if verbatim is not None and not isinstance(verbatim, bool):
                raise ValueError(
                    'The \'verbatim\' parameter must be a Boolean.\nSee '
                    'https://api.slack.com/reference/block-kit/composition-'
                    'objects#text__fields for more information'
                )

        elif self.get('type') == Text.PLAIN_TEXT:
            if self.get('verbatim') is not None:
                raise ValueError(
                    'The \'verbatim\' parameter is only usable when '
                    '\'type\' is \'mrkdwn\'.\nSee https://api.slack.com/'
                    'reference/block-kit/composition-objects#text__fields '
                    'for more information'
                )
            emoji = self.get('emoji')
            if emoji is not None and not isinstance(emoji, bool):
                raise ValueError(
                    'The \'emoji\' parameter must be a Boolean.\nSee https://'
                    'api.slack.com/reference/block-kit/composition-objects#'
                    'text__fields for more information'
                )
        else:
            raise ValueError(
                'The \'type\' parameter must be present and either be '
                '\'mrkdwn\' or \'plain_text\'\nSee https://api.slack.com/'
                'reference/block-kit/composition-objects#text__fields for '
                'more information'
            )
