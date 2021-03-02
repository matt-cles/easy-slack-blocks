from easy_slack_blocks import BlockBuilder
from easy_slack_blocks.components import Button, Confirmation

block_builder = BlockBuilder()

block_builder.add_header('New work-order recieved!')
block_builder.add_divider()
block_builder.add_text('Please confirm the work-order proposal.')
block_builder.add_actions(
    [
        Button(
            text='Confirm', 
            action_id='action:confirm', 
            style=Button.GREEN,
        ),
        Button(
            text='Deny', 
            action_id='action:deny', 
            style=Button.RED, 
            confirm=Confirmation(
                title='Are you sure?',
                text='This will regect the proposal',
                confirm='Yes',
                deny='No',
                style=Confirmation.RED,
            ),
        )
    ],
)

block_builder.open_preview_in_browser()
