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
        text_type='mrkdwn', 
        *, 
        emoji=None, 
        verbatim=None,
        validate=True,
    ):
        text_dict = {
            'text': text,
            'type': text_type,
        }

        if emoji:
            text_dict['emoji'] = emoji

        if verbatim:
            text_dict['verbatim'] = verbatim

        if validate:
            if not isinstance(text, str):
                raise ValueError('The \'text\' parameter must be a String')

            if text_type == Text.MRKDWN:
                if emoji is not None:
                    raise ValueError(
                        'The \'emoji\' parameter is only usable when '
                        '\'text_type\' is \'plain_text\'.'
                    )
                if verbatim is not None and not isinstance(verbatim, bool):
                    raise ValueError(
                        'The \'verbatim\' parameter must be of type Boolean.'
                    )

            elif text_type == Text.PLAIN_TEXT:
                if verbatim is not None:
                    raise ValueError(
                        'The \'verbatim\' parameter is only usable when '
                        '\'text_type\' is \'mrkdwn\'.'
                    )
                if emoji is not None and not isinstance(emoji, bool):
                    raise ValueError(
                        'The \'emoji\' parameter must be of type Boolean.'
                    )
            else:
                raise ValueError(
                    'The \'text_type\' parameter must either be \'mrkdwn\' or '
                    '\'plain_text\''
                )

        super(Text, self).__init__(text_dict)
