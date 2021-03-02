class Image(dict):
    """Generate an Image element.

    See Slack documentation for the Image Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#image
    """
    def __init__(self, image_url, alt_text):
        super(Image, self).__init__(
            type='image', 
            image_url=image_url, 
            alt_text=alt_text,
        )
        