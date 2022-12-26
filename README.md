# Motivation

Recently, I moved to a new place and contracted an internet service provider. To my surprise, they didn't deliver the internet speed I was paying for. I contacted them, and they solved it. However, the next day they dropped my bandwidth again.

The idea of this repository is to have a script that allows me to check my download and upload speeds and log them to a text file. With this information at hand, if the internet provider doesn't fulfill its responsibility, I have proof to hold them accountable.

# The script

The script logs network speeds (download and upload speeds) to a file at iregular intervals. It uses the speedtest-cli command to measure the current download and upload speeds, and logs them to a file using the Python logging module. The log file contains timestamps and the recorded speeds.

The script waits for a random interval of time between 30 and 60 minutes before logging the speeds again. You can adjust this interval by changing the code.

You can use the pandas library to read the log file and analyze the recorded speeds. For example, you can plot the time series data or compute summary statistics for the data.

# Data analysis

To read the log file into a pandas dataframe and plot the time series data, you can use the following code:


```python
import pandas as pd
import matplotlib.pyplot as plt

# Read the log file into a pandas dataframe

df = pd.read_csv("network_speeds.log", names=["timestamp", "download", "upload"])

# Parse the timestamp column as a datetime and set it as the index
df["timestamp"] = pd.to_datetime(df["timestamp"])

df.set_index("timestamp", inplace=True)

# Convert the download and upload columns to float

df[["download", "upload"]] = df[["download", "upload"]].astype(float)

# Plot the time series data

df[["download", "upload"]].plot()
plt.show()
```
This will read the log file into a pandas dataframe, parse the timestamp column as a datetime and set it as the index, and split the data into download and upload columns. It will then convert the download and upload columns to float, and plot the time series data using the matplotlib library.

Note that the log file is assumed to be in the format '%(asctime)s,%(message)s', with the asctime being the timestamp of the log entry and the message being a string containing the download and upload speeds.

# Running at start up

You've run the script, but after you turn off the computer, it stops. If you want the script to run constantly, you need to follow these steps to make it run in the background at start up:

Create the rc.local file with a text editor, such as nano:
```bash
sudo nano /etc/rc.local
```
Add the following line to the file:
```bash
#!/bin/bash
# Run the startup script on startup
python3 /path/to/script/network_speeds.py &
```
Save the file and exit the text editor.
Enable the rc.local service with the following command:
```bash
sudo systemctl enable rc-local
```
After completing these steps, the script should run in the background at start up, so it will continue running even after you turn off the computer.

This process is specific to Ubuntu 22.04, but it may be similar on other Linux distributions.

# Acknowledgments 

Finally, I'm grateful to the OpenAI chatGPT tool, which allowed me to quickly develop this script.