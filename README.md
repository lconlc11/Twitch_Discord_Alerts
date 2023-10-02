# Discord to Twitch Alert Bot

This is a Discord bot that sends an alert to a specified Twitch channel when a user with a linked Twitch account joins a Discord server. It uses the Discord API and Twitch API for this functionality.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Listens for new members joining a Discord server.
- Checks if the new member has a linked Twitch account.
- Sends a custom alert message to a Twitch channel if the member has a linked Twitch account.

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Replace the placeholders in the script with your actual values:

   - `YOUR_DISCORD_BOT_TOKEN`: Replace with your Discord bot token.
   - `YOUR_TWITCH_CHANNEL`: Replace with your Twitch channel username.
   - `YOUR_TWITCH_ACCESS_TOKEN`: Replace with your Twitch API access token.
   - `YOUR_TWITCH_CLIENT_ID`: Replace with your Twitch client ID.
   - `YOUR_SERVER_CHANNEL_ID`: Replace with the channel ID in your Discord server where you want to notify new members.

4. Set up and configure your database connection (if needed). Replace `YOUR_DATABASE_CONNECTION` with your actual database connection details.

## Usage

1. Run the script using `python main.py`.
2. The bot will now listen for new members joining the Discord server.
3. If a new member has a linked Twitch account, the bot will send an alert to the specified Twitch channel.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
