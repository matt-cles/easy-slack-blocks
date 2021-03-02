from easy_slack_blocks import BlockBuilder
from easy_slack_blocks.components import Text

block_builder = BlockBuilder()

block_builder.add_header('Welcome to easy-slack-blocks :wave:')
block_builder.add_image(
    image_url='https://source.unsplash.com/random/512x256/?block', 
    text_description='The world is your oyster.',
)
block_builder.add_text(
    '*easy-slack-blocks* is a python module designed to make it easy and '
    'intuitive to build the Slack Block json objects that the Slack API uses '
    'to display messages from Slack Bots.'
)
block_builder.add_section(
     fields=[
        Text(
            '*Simple Interface*\nBuild blocks quickly with a feature rich '
            'set of easy to use classes.'
        ),
        Text(
            '*Plug and Play*\neasy-slack-blocks classes are built to extend '
            'the object types that work naitivly with Slack frameworks, '
            'such as slack_bolt.'
        ),
    ],
)
block_builder.add_context('I hope this library is helpful to you!')

block_builder.open_preview_in_browser()
