![Intro scenery: two hands at a wall of kraft clipboards, one steadying the centre board while the other pins a small red flag through the top corner of its fresh white sheet, ranked boards on every side](intro-banner.png)


# analyze-clipboard-monitor

![Wordmark banner: a wall covered in a neat grid of kraft clipboards, each holding one blank white sheet under a steel clip, with a single small red flag pin on one board near the centre while all the others stand plain](banner.png)

![Animated roundup: the herd ring turns, an animal pauses at the chute, and one ice cyan notch lights once in a long loop](scene.svg)

![analyze-clipboard-monitor logo: one kraft clipboard straight on against a pale wall, its steel clip holding a single clean white sheet with one small red flag pin stuck through its top right corner](logo.png)

Monitors the system clipboard for sensitive data shapes (credit card numbers, API keys, email addresses) and alerts the user when one appears: it logs a warning and prints an `Alert!` line. It polls the clipboard once per second and runs until Ctrl+C. Detection is shape only: the card pattern checks 13 to 16 digits with optional separators and does not run a Luhn check, so innocent long numbers can trip it. An alert is a prompt to look, not a verdict.

> **Tally slate, A Shape Is Not a Verdict:** detection is shape only, the card pattern checks 13 to 16 digits with optional separators and does not run a Luhn check, so innocent long numbers can trip it. An alert is a prompt to look, not a verdict.

![Frost fern separator spreading the full width](sep-heavy.svg)

## Install

```sh
git clone https://github.com/ShadowGuard-AI/analyze-clipboard-monitor
cd analyze-clipboard-monitor
pip install -r requirements.txt
```

The only dependency is `pyperclip` (see `requirements.txt`). On Linux a clipboard backend such as xclip or xsel is also needed for pyperclip to reach the clipboard.

> **Tally slate, the Linux backend:** on Linux a clipboard backend such as xclip or xsel is also needed for pyperclip to reach the clipboard.

![Frost fern separator spreading the full width](sep-heavy.svg)

## Usage

```sh
python3 main.py [--log-level LEVEL]
```

- `--log-level`: one of DEBUG, INFO, WARNING, ERROR, CRITICAL (default: INFO)
- `-h` / `--help`: show help and exit

If pyperclip is not installed, the tool prints an install message and exits 1 before monitoring starts.

> **Tally slate, The Chart Is Missing: Install pyperclip:** if pyperclip is not installed, the tool prints an install message and exits 1 before monitoring starts.

![Short frost fern separator](sep-light.svg)

## License

Copyright (c) ShadowGuard-AI
