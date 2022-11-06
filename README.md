# UBC-Auto_Register
## Automatically registers the user in classes at UBC

## How to run this code
1. Install Python [here](https://www.python.org/downloads/).
2. Install packages, you might need to install pip [here](https://pip.pypa.io/en/stable/installation/)
    ```
    pip install selenium
    ```
    and
    ```
    pip install twilio
    ```
3. Download the correct version of chromedriver for your system [here](https://chromedriver.chromium.org/downloads).
    * Chromedriver must the the same version as chrome on your device
    * Windows chromedriver is included in this repository
4. Make a free twilio account [here](https://www.twilio.com/)
5. Edit these values in autoRegister.py with a text editor of your choice
    ```
    #List of classes you want to register in
    #eg. classes = ['COSC 315 101','SPAN 202 001', 'COSC 360 L02']
    classes = []

    #campus wide login
    #eg. cwl = "ljohnson"
    #eg. pwd = "verySecurePassword"
    cwl = ""
    pwd = ""

    twilio_account = ""
    twilio_token = ""

    #eg. twilio_phone_number = "+17786981234"
    twilio_phone_number = ""

    #eg. your_phone_number = "+17786980085"
    your_phone_number = ""
    ```
6.  Run autoRegister.py using your text editor or IDE or run in the terminal
    ```
    python autoRegister.py
    ```
7. Done!, now just wait for the text message.
