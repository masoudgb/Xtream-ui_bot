<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xtream-UI Bot</title>
</head>
<body>
    <h1>Xtream-UI Bot</h1>
    <p><strong>A bot to automatically post movie and series posters and information from Xtream-UI server to Telegram channels.</strong></p>

    <hr>

    <h2>Features</h2>
    <ul>
        <li>Automatically posts newly added movies and series from your Xtream-UI server.</li>
        <li>Highly customizable for posting intervals and Telegram channels.</li>
        <li>Supports multiple channels with separate configurations.</li>
    </ul>

    <hr>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
cd /opt/xtream-ui_bot
        </code></pre>
        <li>Run the installation script:</li>
        <pre><code>python3 main.py</code></pre>
    </ol>

    <hr>

    <h2>Running the Bot</h2>
    <p>To start the bot, execute:</p>
    <pre><code>python3 /opt/xtream-ui_bot/main.py</code></pre>

    <hr>

    <h2>Configuration</h2>

    <h3>Telegram Setup</h3>
    <p>Provide these details during setup:</p>
    <ul>
        <li><strong>Xtream-UI API URL</strong>: Example: <code>http://yourserver:8080</code></li>
        <li><strong>API Username and Password</strong></li>
        <li><strong>Telegram Bot Token</strong>: Get from <a href="https://core.telegram.org/bots#botfather" target="_blank">BotFather</a></li>
        <li><strong>Channel IDs</strong>: Add public or private channels.</li>
    </ul>

    <h3>Default Posters</h3>
    <p>Configure fallback images for content missing custom covers.</p>

    <hr>

    <h2>Automating the Bot</h2>

    <h3>Systemd Integration</h3>
    <p>The bot includes a <strong>systemd</strong> service and timer:</p>
    <ul>
        <li><strong>Service</strong>: Runs the bot.</li>
        <li><strong>Timer</strong>: Automates posting at intervals (default: 30 minutes).</li>
    </ul>
    <p>Activated automatically during installation.</p>

    <hr>

    <h2>Updating the Bot</h2>
    <p>Run the following to update the bot:</p>
    <pre><code>python3 /opt/xtream-ui_bot/update.py</code></pre>

    <hr>

    <h2>Troubleshooting</h2>
    <ol>
        <li><strong>Incorrect Display on GitHub:</strong>
            <ul>
                <li>Ensure your file has the <code>.md</code> extension.</li>
                <li>Open the file in GitHub to confirm proper formatting.</li>
            </ul>
        </li>
        <li><strong>Broken Links:</strong>
            <ul>
                <li>Check syntax:
                    <pre><code>[Link Text](https://example.com)</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Font Issues:</strong>
            <ul>
                <li>Use a Markdown-compatible editor (e.g., <strong>Typora</strong>, <strong>Obsidian</strong>, or <strong>VSCode</strong>).</li>
            </ul>
        </li>
    </ol>

    <hr>

    <h2>Example Links in HTML:</h2>
    <ul>
        <li><a href="https://github.com/masoudgb" target="_blank">Xtream-UI GitHub</a></li>
        <li><a href="https://core.telegram.org/bots#botfather" target="_blank">Telegram BotFather</a></li>
    </ul>
</body>
</html>
