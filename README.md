# Imap2Gmail

This program fetches all unread messages from the given IMAP accounts, and transfers them
to the given email address. It is useful for fetching mail from IMAP accounts into Gmail.

## Requirements

* Python 3.x

## Setup

Supply needed information in settings.py file, and
add a crontab entry to execute it regularly. You can 
also use an output redirection for logging purpose.
 
### Crontab entry example

    */15 * * * * /usr/bin/python3 /usr/imap2gmail/imap2gmail.py >> /var/log/imap2gmail.log

## License

Copyright (c) Pier-Luc Brault

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
