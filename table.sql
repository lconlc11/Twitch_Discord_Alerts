-- Create a table to store linked Twitch accounts
CREATE TABLE linked_twitch_accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    discord_user_id BIGINT NOT NULL,
    twitch_user_id VARCHAR(255) NOT NULL,
    CONSTRAINT unique_discord_twitch_pair UNIQUE (discord_user_id, twitch_user_id)
);

-- Index for faster lookup based on Discord user ID
CREATE INDEX discord_user_id_index ON linked_twitch_accounts (discord_user_id);
