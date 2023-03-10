"""Script to log network speeds to a file."""

from typing import Tuple
import logging
import time
import subprocess

import numpy as np


def get_speeds() -> Tuple[float, float]:

    """
    Run the speedtest-cli command and return the current download
    and upload speeds.
    """
    result = subprocess.run(
        ["speedtest-cli"], capture_output=True, check=True
    )

    output = result.stdout.decode()
    lines = output.split("\n")
    download_line = lines[-2]
    upload_line = lines[-4]
    download_speed = float(download_line.split()[1])
    upload_speed = float(upload_line.split()[1])
    return download_speed, upload_speed


if __name__ == "__main__":

    save_to = "/home/edgar/monitor-internet"

    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s,%(message)s',
        filename=f'{save_to}/speeds.log', filemode='a'
    )

    while True:

        down_speed, up_speed = get_speeds()
        logging.info("%f,%f", down_speed, up_speed)

        # sleep for 30-60 minutes before the next iteration
        sleep_for = np.random.randint(1800, 3600)
        print(f"Sleeping for {sleep_for} seconds...", end="\r")
        time.sleep(sleep_for)
