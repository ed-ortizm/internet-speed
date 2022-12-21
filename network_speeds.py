"""Script to log network speeds to a file."""

from typing import Tuple

import logging
import time
import subprocess

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(message)s',
    filename='network_speeds.log', filemode='w'
)


def get_speeds() -> Tuple[float, float]:

    """
    Run the speedtest-cli command and return the current download
    and upload speeds.
    """
    result = subprocess.run(["speedtest-cli"], capture_output=True)
    output = result.stdout.decode()
    lines = output.split("\n")
    download_line = lines[-2]
    upload_line = lines[-4]
    download_speed = float(download_line.split()[1])
    upload_speed = float(upload_line.split()[1])
    return download_speed, upload_speed


while True:
    download_speed, upload_speed = get_speeds()
    logging.info(f"Download speed: {download_speed} Mbps")
    logging.info(f"Upload speed: {upload_speed} Mbps")
    time.sleep(3600)  # pause for 1 hour before the next iteration
