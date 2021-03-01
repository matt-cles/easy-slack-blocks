from block_builder import BlockBuilder
from components import Text
from components import Button
from components import Image
from components import Confirmation

block_builder = BlockBuilder()

block_builder.add_header('Welcome to Easy-Slack-Blocks :wave:')
block_builder.add_image(
    image_url='https://source.unsplash.com/random/512x256/?block', 
    text_description='The world is your oyster.',
)
block_builder.add_text(
    '*Easy-Slack-Blocks* has been designed to help you format Slack Blocks '
    'in an easy and intuitive way.'
)
block_builder.add_section(
    fields=[
        Text(
            '*Simple Interface*\nBuild blocks quickly with a feature rich '
            'set of easy to use classes'
        ),
        Text(
            '*Plug and Play*\nEasy-Slack-Blocks classes are built to extend '
            'the object types that Slack\'s SDK expects for the blocks '
            'fields.'
        ),
    ]
)
block_builder.add_context('I hope this simple library is helpful to you!')
block_builder.add_actions(
    [
        Button('Confirm', 'action:confirm', style=Button.GREEN),
        Button(
            text='Deny', 
            action_id='action:deny', 
            style=Button.RED, 
            confirm=Confirmation(
                title='Are you sure?',
                text='This will regect the proposal',
                confirm='Yes',
                deny='No',
            ),
        )
    ],
)

block_builder.open_preview_in_browser()
# block_builder.add_divider(block_id='div-1')
# block_builder.add_context('this is context :nerd_face:')
# block_builder.add_divider()
# block_builder.add_context(
#     context= [
#         Text('Wow...'),
#         Image('http://placekitten.com/700/500', 'pic agian'),
#         Text('*hmmm*', Text.PLAIN_TEXT),
#     ]
# )
# block_builder.add_file('ABCD1')

# # This will open a new tab in your web browser to display the currenlty 
# # built Slack blocks in the Slack Block Kit Builder
# block_builder.open_preview_in_browser()

# # In the event that a new type of slack block is introduced, but this 
# # library has not yet been updated to include an easy way of adding the
# # new block type, they can still be added to the 
# block_builder.append(
#     {
#         'type': 'currently-unimplemented',
#         'text': {
#             'type': 'new-text-type',
#             'text': 'neat, I can still add a json type block!'
#         },
#         'fancy_new_feature_flag': True,
#     }
# )

# # Additionally, class method 'add_raw_block' can also be used to achieve 
# # the same effect, in most cases
# block_builder.add_raw_block(
#     block_type='currently-unimplemented',
#     text={
#         'type': 'new-text-type',
#         'text': 'neat, another way to add an unimplemented block!',
#     },
#     fancy_new_feature_flag=False,
#     block_id='new-feature-block-2'
# )

# for block in block_builder:
#     print(block)
