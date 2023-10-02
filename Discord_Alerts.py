import discord
import requests
import database_library  # Replace with the appropriate library for database interaction

client = discord.Client()

def check_twitch_link(member):
    # Assuming you have a database where Twitch account linking information is stored
    # Replace 'YOUR_DATABASE_CONNECTION' and 'linked_accounts' with actual database connection and table
    database_connection = YOUR_DATABASE_CONNECTION
    linked_accounts_table = database_connection.linked_accounts

    # Retrieve the user's Discord ID to check for Twitch linking
    discord_user_id = member.id

    # Check if the user's Discord ID is in the linked accounts database
    # Replace 'discord_id_column' and 'twitch_id_column' with actual column names
    result = linked_accounts_table.find_one({'discord_id_column': discord_user_id})

    if result and result['twitch_id_column']:
        # Twitch account is linked
        return True
    else:
        # Twitch account is not linked
        return False

def send_twitch_alert(member):
    # Replace 'YOUR_TWITCH_CHANNEL' with the Twitch channel username you want to send the alert to
    twitch_channel = 'YOUR_TWITCH_CHANNEL'
    
    # Replace 'YOUR_TWITCH_ACCESS_TOKEN' with your Twitch API access token
    twitch_access_token = 'YOUR_TWITCH_ACCESS_TOKEN'

    # Customize the message for the Twitch alert
    alert_message = f'{member.display_name} has joined the Discord server! Go say hello!'

    # Construct the Twitch chat message with the user's Twitch display name
    twitch_chat_message = f'PRIVMSG #{twitch_channel} :{alert_message}'

    # Twitch API endpoint to send chat messages
    twitch_api_url = f'https://api.twitch.tv/kraken/chat/{twitch_channel}/'

    # Twitch API headers with the required access token
    headers = {
        'Client-ID': 'YOUR_TWITCH_CLIENT_ID',
        'Authorization': f'Bearer {twitch_access_token}',
    }

    # Send the Twitch chat message using the Twitch API
    response = requests.post(twitch_api_url, headers=headers, data=twitch_chat_message)

    if response.status_code == 200:
        print('Twitch alert sent successfully!')
    else:
        print(f'Failed to send Twitch alert. Status code: {response.status_code}')

@client.event
async def on_member_join(member):
    # Check if the user has a Twitch account linked
    twitch_account_linked = check_twitch_link(member)

    if twitch_account_linked:
        # Send an alert to Twitch stream
        send_twitch_alert(member)
        await member.send("Welcome to the server! We've sent a Twitch alert to let everyone know you've joined.")

        # You can also notify the server channel about the new member
        channel = client.get_channel(YOUR_SERVER_CHANNEL_ID)  # Replace with your server's channel ID
        if channel:
            await channel.send(f"{member.mention} has joined the server! Let's give them a warm welcome.")
        else:
            print("Failed to find the specified channel.")

# Start the Discord bot
client.run('YOUR_DISCORD_BOT_TOKEN')
