# SlicerBackUp

## Why?

I semi-regularly wipe my computer to keep it running smoothly. However, I usually forget to backup my slicer profiles before doing so. This utility automatically backups your slicer profiles to a GitHub repository, similar to [Klipper-Backup](https://github.com/Staubgeborener/Klipper-Backup).

## Installation

> [!NOTE]
> This was written out of necessity and not originally intended to be a public project, so don't exactly expect [3MS](https://3ms.3dcoded.xyz/)-level documentation...

1. Install [Python](https://www.python.org/)
2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)
3. Clone this repository
4. Run `pipenv install` to install dependencies

## Configuration

Create a file `env.txt` in the same directory as `main.py`. Example contents:

```
# Determine config dir by going into slicer -> help -> show config folder -> user -> default -> copy path including "default" at the end
SLICERBACKUP_CONFIG_DIR='<SLICER PATH HERE>'
# GitHub repo to backup to
SLICERBACKUP_REPO_URL='<GITHUB REPO HERE>'
```

Ensure your Github access token is authenticated globally on your computer.

## Testing

Run in your terminal, in the repo directory:

```
pipenv run python main.py
```

If nothing is output, success! Check the repo you configured to be sure.

## Usage

In your slicer's post processing scripts section (for your most common profiles), add a line in the below format:

```
'<PYTHON INTERPRETER PATH>' '<SlicerBackUp main.py PATH>'
```

Now, whenever you export G-code or upload directly from the slicer, the repo will automatically be updated.
