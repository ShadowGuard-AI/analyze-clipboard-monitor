import argparse
import logging
import sys
import time
import re

# This guard runs at import time, not inside main, so importing this
# module on a machine without pyperclip ends the interpreter before any
# caller code runs. For a one file tool I accept that: there is no mode
# of this program that works without clipboard access anyway.
try:
    import pyperclip
except ImportError:
    print("Pyperclip module not found. Please install it: pip install pyperclip")
    sys.exit(1)

# Patterns are compiled once at import. The monitor loop below calls the
# detector every second for the life of the process, so paying re.compile
# on every clipboard change would be pure repetition.
PATTERNS = [
    (re.compile(r"\b(?:\d[ -]*?){13,16}\b"), "Credit Card Number (Possible)"),
    (re.compile(r"\b(?:API_KEY|apikey)=[\w-]+\b"), "API Key (Possible)"),
    (re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"), "Email address (Possible)"),
]


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def setup_argparse():
    """
    Sets up the argument parser for the command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Monitors the system clipboard for sensitive data and alerts the user."
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level.",
    )
    return parser.parse_args()


def detect_sensitive_data(text):
    """
    Detects sensitive data in the given text using regular expressions.

    Args:
        text (str): The text to analyze.

    Returns:
        list: A list of detected sensitive data types. Empty if none are found.
    """
    # Only the labels come out of here, never the matched text. The
    # alert tells the user what kind of thing was seen without writing
    # the secret itself into a log file, which would defeat the point.
    # The card pattern is a shape check only: 13 to 16 digits with optional
    # separators. It does not run a Luhn check, so plenty of innocent long
    # numbers trip it. That bias toward false alarms is intentional here;
    # the alert is a prompt to look, not a verdict.
    return [label for pattern, label in PATTERNS if pattern.search(text)]


def main():
    """
    Main function to monitor the clipboard and detect sensitive data.
    """
    args = setup_argparse()

    logging.getLogger().setLevel(args.log_level)

    logging.info("Clipboard monitor started. Press Ctrl+C to stop.")

    previous_clipboard_content = ""

    try:
        while True:
            try:
                clipboard_content = pyperclip.paste()
            except pyperclip.PyperclipException as e:
                logging.error(f"Error accessing clipboard: {e}")
                logging.error("Ensure you have the required dependencies installed (e.g., xclip/xsel on Linux).")
                # Breaking here ends the whole program, and it ends with
                # exit code 0 because nothing re-raises. On a headless
                # box with no clipboard mechanism this tool therefore
                # looks like it ran fine. The two error lines above are
                # the only sign it monitored nothing.
                break # Exit loop if clipboard access fails

            # Comparison is only against the immediately previous
            # content, so copying the same secret again after copying
            # anything else alerts again, while re-copying it twice in
            # a row alerts once. Starting previous as an empty string
            # also means an empty clipboard at launch is never a change.
            if clipboard_content != previous_clipboard_content:
                logging.debug("Clipboard content changed.")
                previous_clipboard_content = clipboard_content

                sensitive_data = detect_sensitive_data(clipboard_content)

                if sensitive_data:
                    logging.warning(f"Sensitive data detected in clipboard: {sensitive_data}")
                    print(f"Alert! Potential sensitive data found: {sensitive_data}")


            time.sleep(1)  # Check every 1 second (adjust as needed)

    except KeyboardInterrupt:
        logging.info("Clipboard monitor stopped.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()