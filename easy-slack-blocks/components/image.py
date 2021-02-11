class Image(dict):
    """docstring for Image.

    See https://api.slack.com/reference/block-kit/block-elements#image
    for more information.
    """
    def __init__(self, image_url, text_description):
        super(Image, self).__init__(
            type='image', 
            image_url=image_url, 
            alt_text=text_description,
        )
        