## Drive CLI

Access and Navigate  Google Drive via the command line using Unix/Unix-like commands.

## Setup

Start by creating a new project in the [Google Cloud Console](https://console.cloud.google.com/). Follow the instructions for [configuring an OAuth client](https://developers.google.com/android-publisher/getting_started). Once configured, click on `Download OAuth client` and download the `credentials.json` file. Navigate to the `Audience` tab and add the email(s) that will be used.

```sh
# Clone the repo
git clone https://github.com/eeldarrb/drive_cli
cd drive_cli
```
>[!IMPORTANT]
>
>Move `credential.json` into the project directory `/drive_cli/credentials.json`

```sh
uv sync
source .venv/bin/activate
```

## Usage

> [!NOTE]
>It may take some time when starting the tool depending on the amount of files in the drive

```sh
uv run src/main.py
```

### Commands
- cd
- ls
- mkdir
- download
- upload
- rm

## TODO
- [ ] Add tab completion
- [ ] Command flags
- [ ] Auto-refresh + caching
- [ ] Error Log
- [ ] Handle files not in main drive (shared)
- [ ] Create docs for commands
