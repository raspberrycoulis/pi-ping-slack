# pi-ping-slack
A Python script that checks the HTTP status code of a website and reports the outcome via Slack

## Installation
This requires a few pre-requistes:
* pip
* requests

### pip
Install Python 2 and 3 versions in your command line with:

    $ sudo apt-get install -y python-pip python3-pip

### requests
Install in your command line with:

    $ sudo pip install requests

## Clone this repo
To clone this repo, run the following command in your command line:

    $ git clone https://github.com/raspberrycoulis/pi-ping-slack.git

### Usage
To use this script, you'll need to make a few changes to the variables used.

#### website
This is the website you want to check the status of. Replace `https://www.google.co.uk` with your chosen website.

#### sitename
The name of the website - this will form part of the Slack message and is really a vanity variable, but it's nice to use!

#### wait
The time to wait between status checks in seconds. By default this is set to 1800 seconds (which is 30 minutes), but you can adjust this if you prefer.

#### webhook
This will be your Slack incoming webhook - you can get a full walkthrough of this via [Slack's documentation](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks "Slack Incoming Webhooks").

Before running the script, make sure it is executable by running (assuming you have cloned this in your home directory):

    $ cd pi-ping-slack
    $ chmod +x pi-ping-slack.py

Test out the script by running:

    $ ./pi-ping-slack.py

If all goes well, you should have a Slack notification.

## Running on boot
The script is set to check the status of your set website every 30 minutes (1800 seconds), but to run this on boot you can do so using `systemd`:

### 1. Create Unit file
This will tell the Pi to run your script on boot:

    sudo nano /lib/systemd/system/pi-ping-slack.service

Then add the following text to your file (you may need to adjust the path for your `pi-ping-slack.py` script depending on where it is located (the part `/home/pi/Pi-Ping/pi-ping.py`):

    [Unit]
    Description=Pi-Ping via Slack service by Raspberry Coulis
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/usr/bin/python /home/pi/pi-ping-slack/pi-ping-slack.py

    [Install]
    WantedBy=multi-user.target

Exit, `ctrl + x`, and save `y` to create the service unit file.

### 2. Set the relevant permissions
Make sure that the permissions are set correctly:

    sudo chmod 644 /lib/systemd/system/pi-ping-slack.service

### 3. Configure systemd
Make sure that systemd can use your newly created unit file:

    sudo systemctl daemon-reload
    sudo systemctl enable pi-ping-slack.service

Reboot the Pi to test via `sudo reboot`.

### 4. Check on the status of your service
Check that the service has started by running:

    sudo systemctl status pi-ping-slack.service

If done correctly, you should see that your `pi-ping-slack.py` script is now running!
