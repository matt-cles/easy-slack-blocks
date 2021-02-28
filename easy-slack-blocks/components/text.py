class Text(dict):
    """docstring for Text.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#text
    """
    MRKDWN = MARKDOWN = RICH = 'mrkdwn'
    PLAIN_TEXT = PLAIN = 'plain_text'

    def __init__(self, text, text_type='mrkdwn', *, emoji=None, verbatim=None):
        if text_type == Text.MRKDWN:
            if emoji is not None:
                raise ValueError(
                    'The \'emoji\' parameter is only usable when '
                    '\'text_type\' is \'plain_text\'.'
                )
            # Set default 'verbatim' value if none was passed
            if verbatim is None:
                verbatim = False
            super(Text, self).__init__(
                text=text, 
                type=text_type, 
                verbatim=verbatim,
            )
        elif text_type == Text.PLAIN_TEXT:
            if verbatim is not None:
                raise ValueError(
                    'The \'verbatim\' parameter is only usable when '
                    '\'text_type\' is \'mrkdwn\'.'
                )
            # Set default 'emoji' value if none was passed
            if emoji is None:
                emoji = True
            super(Text, self).__init__(
                text=text,
                type=text_type,
                emoji=emoji,
            )
        else:
            raise ValueError(
                'The \'text_type\' parameter must either be \'mrkdwn\' or '
                '\'plain_text\''
            )
