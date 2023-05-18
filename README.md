# InstaFollowerAlert

The Instagram Follower Tracker is a Python script that allows you to track new followers of a specific Instagram account. It utilizes the Instagram Private API to retrieve follower information and compare it with the previous follower count.

**Prerequisites**


`Python 3.x`

`instagram-private-api library`

`fake_useragent library`

`bs4 (BeautifulSoup) library`

`requests library`


**Setup**


Install the required libraries:

`instagram-private-api`: A library for interacting with the Instagram Private API.

`fake_useragent`: A library for generating random User-Agent headers.

`bs4 (BeautifulSoup)`: A library for parsing HTML documents.

`requests`: A library for making HTTP requests.

Import the necessary libraries:

`instagram-private-api`: Import the Client class for interacting with the Instagram Private API.
`fake_useragent`: Import the UserAgent class for generating User-Agent headers.
`bs4 (BeautifulSoup)`: Import the BeautifulSoup class for parsing HTML documents.
`requests`: Import the requests module for making HTTP requests.


**Usage**
Specify the Instagram account credentials:

Set the username variable to your Instagram username.
Set the password variable to your Instagram password.
Specify the target Instagram account:

Set the target_username variable to the username of the Instagram account you want to track the followers of.
Specify the webhook URL:

Set the webhook_url variable to the URL of the webhook endpoint where you want to receive notifications about new followers.
Replace the placeholder URL with your own webhook URL.
Specify the JSON file path:

Set the json_file variable to the path where you want to store the JSON file that keeps track of followers.
If the file does not exist, the script will create it automatically.
Run the script:

Execute the script and it will start monitoring the follower count of the target Instagram account.
It will check for new followers every 60 seconds by default.
If a new follower is detected, it will record the username in the JSON file and send a notification to the specified webhook URL.
Stop the script:

To stop the script, you can terminate the program manually.



**Limitations**


The script relies on the Instagram Private API, which may be subject to changes and restrictions by Instagram. Please use it responsibly and in accordance with Instagram's terms of service.
The script does not handle exceptions or errors gracefully. Additional error handling and validation should be implemented for a more robust solution.
The script assumes that the JSON file is formatted as an array of follower usernames.


**Disclaimer**


Please be aware of the legal implications of using automated tools to interact with Instagram. Make sure to review and comply with Instagram's terms of service and API usage guidelines.
Use this script responsibly and in accordance with Instagram's terms of service and any applicable laws and regulations.




