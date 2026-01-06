import logging

from requests import post

from semirandom import semi_random
from tips import random_tip


logger = logging.getLogger(__name__)


def read_topic_name() -> str:
    """Read the topic name from the .topic file."""
    with open(".topic", "r") as file:
        return file.readline().strip()


def send_message(message: str) -> None:
    """Send a message using ntfy to the topic in the file .topic."""
    topic_name = read_topic_name()
    notify_url = f"https://ntfy.sh/{topic_name}"
    utf8_bytes = message.encode(encoding="utf-8")
    post(notify_url, data=utf8_bytes)


def main():
    logging.basicConfig(
        filename="cleaning-tips.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    logger.info("Running")
    if semi_random():
        logging.info("Sending notification")
        send_message(random_tip())


if __name__ == "__main__":
    main()
