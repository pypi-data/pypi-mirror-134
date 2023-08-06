This is just a bit more verbose version of httprobe fully written in python3. 

# Installation
    pip install httprobe
# Usage
    cat domains_or_urls.txt | httprobe
```
usage: httprobe [-h] [-H HEADER [HEADER ...]] [-L] [-X METHOD] [-d DATA] [--connect-timeout CONNECT_TIMEOUT] [--read-timeout READ_TIMEOUT] [-c THREADS] [-p DELAY] [-o OUTPUT_FILE] [-l]  
  
optional arguments:  
  -h, --help            show this help message and exit  
  -H HEADER [HEADER ...], --header HEADER [HEADER ...]  
                        Header to include in the request (default: None)  
  -L, --follow-redirects  
                        Follow redirections (default: False)  
  -X METHOD, --method METHOD  
                        HTTP method to use for the requests (default: GET)  
  -d DATA, --data DATA  Body data to include in request (default: None)  
  --connect-timeout CONNECT_TIMEOUT, --ct CONNECT_TIMEOUT  
                        Connection timeout (default: 15)  
  --read-timeout READ_TIMEOUT, --rt READ_TIMEOUT  
                        Read timeout (default: 15)  
  -c THREADS, -t THREADS, --threads THREADS  
                        Number of concurrent requests (default: 20)  
  -p DELAY, -s DELAY, --delay DELAY  
                        Delay in seconds to wait between requests (default: 0)  
  -o OUTPUT_FILE, --output-file OUTPUT_FILE  
                        Write output to file (default: None)  
  -l, --list            Only show urls, do not probe (default: False)  
```
