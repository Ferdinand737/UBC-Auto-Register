# UBC-Auto-Register
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
  
<br>

4. Make a free twilio account [here](https://www.twilio.com/)
    * twilio is only required if you want to receive a text upon registration for your courses

<br>

1. Edit these values in autoRegister.py with a text editor of your choice

    #List of classes you want to register in
    #eg. classes = ['COSC 315 101','SPAN 202 001', 'COSC 360 L02']
    classes = []

    #campus wide login
    #eg. cwl = "jsmith"
    #eg. pwd = "verySecurePassword"
    cwl = ""
    pwd = ""

    #leave blank if you did not make a twilio account
    twilio_account = ""
    twilio_token = ""

    #eg. twilio_phone_number = "+17786981234"
    twilio_phone_number = ""

    #eg. your_phone_number = "+17786980085"
    your_phone_number = ""
    ```
2.  Run autoRegister.py using your text editor/IDE or run this command
    ```
    python autoRegister.py
    ```
3. Done!, now just wait for the text message.
   * A chrome window will open and navigate to ubc course website
   * Chrome window does not need to be in the foreground for this to work
   * Chrome window needs to be maximized (not mobile page) so that the login button is visible
