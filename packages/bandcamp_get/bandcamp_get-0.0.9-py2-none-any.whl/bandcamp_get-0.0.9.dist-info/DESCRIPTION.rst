# bandcamp-get

## automated downloading of bandcamp albums
bandcamp-get uses Selenium WebDriver to automate free album downloads from the music website Bandcamp. By default it creates a temporary email address using Guerrilla Mail, a free throwaway email service. Music sent to the inbox will be downloaded once all albums have been processed, no clicking necessary!

## Installation
* `pip install bandcamp-get`

## Usage
usage: bandcamp-get.py [-h] [-b BROWSER] [-e EMAIL] [-v] USER

automated downloading of bandcamp music

&nbsp;&nbsp;positional arguments:

&nbsp;&nbsp;&nbsp;&nbsp;USER            bandcamp user to download from


&nbsp;&nbsp;optional arguments:

&nbsp;&nbsp;&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;show this help message and exit

&nbsp;&nbsp;&nbsp;&nbsp;-b BROWSER, --browser BROWSER&nbsp;enter chrome or firefox, defaults to firefox

&nbsp;&nbsp;&nbsp;&nbsp;-e EMAIL, --email EMAIL&nbsp;&nbsp;use your own email instead of a throwaway

&nbsp;&nbsp;&nbsp;&nbsp;-v, --version&nbsp;&nbsp;&nbsp;display current version


## Author
* Hunter Hammond (huntrar@gmail.com)

## Notes
* If you choose to use a throwaway email (chosen by default unless --email flag is used), then all emails sent to the throwaway will be opened and the download links followed by the WebDriver. This occurs once all albums have been emailed/otherwise downloaded.

* Closing the bandcamp browser window before all albums have been downloaded is fine if you wish to stop it early! The ones which have been emailed to the throwaway so far will still be downloaded as long as the Guerrilla Mail window is left open.


News
====

0.0.9
------

 - updated some formatting and changed % to format()

0.0.8
------

 - Updated program description

0.0.7
------

 - Moved the check for straggler emails to auto_download rather than check_email

0.0.6
------

 - Firefox webdriver no longer asks before downloading .zip
 - Minor fix to download_link behavior

0.0.5
------

 - Added randomized user agent for requests and selenium drivers

0.0.4
------

 - Removed sys import

0.0.3
------

 - Made 0 or 1 positional arguments

0.0.2
------

 - Changed execution command to bandcamp-get

0.0.1
------

 - First entry




