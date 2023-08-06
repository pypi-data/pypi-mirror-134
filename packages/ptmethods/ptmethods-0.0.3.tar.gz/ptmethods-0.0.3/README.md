![penterepTools](https://www.penterep.com/external/penterepToolsLogo.png)

# PTMETHODS
> HTTP Methods Testing Tool

- Script retrieves methods offered by server from *OPTIONS* request
- Script sends GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, TRACE, DEBUG headers and retrieves it's response.
- Script tests CONNECT method by connecting to url at ports 80, 443
- Script tests if domain can be used as proxy.

## Installation

```
pip install ptmethods
```

## Usage examples
Optimally use this script against homepage, any image and sources protected by HTTP authentication
```
ptmethods -u https://www.example.com/
ptmethods -u https://www.example.com/ -r
ptmethods -u https://www.example.com/index.php -sr -sh
ptmethods -u https://www.example.com/index.php -c PHPSESSID
ptmethods -f URL_list.txt
```

## Options
```
-u   --url            <url>           Test specified URL
-f   --file           <file>          Load list of URLs from file
-sh  --show-headers                   Show response headers
-sr  --show-response                  Show response text
-p   --proxy          <proxy>         Set proxy (e.g. http://127.0.0.1:8080)
-ua  --user-agent     <ua>            Set User-Agent header
-H   --headers        <header:value>  Set custom header(s)
-c   --cookie         <cookie>        Set cookie(s)
-r   --redirects                      Follow redirects (default False)
-j   --json                           Output in JSON format
-v   --version                        Show script version and exit
-h   --help                           Show this help message and exit
```

## Dependencies
```
requests
ptlibs
```

## Version History
    0.0.2
        - Implemented proxy test
        - Implemented CONNECT tests
    0.0.1 - 0.0.3
        Alpha releases

## Licence

Copyright (c) 2020 HACKER Consulting s.r.o.

ptmethods is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

ptmethods is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ptmethods. If not, see https://www.gnu.org/licenses/.

## Warning

You are only allowed to run the tool against the websites which
you have been given permission to pentest. We do not accept any
responsibility for any damage/harm that this application causes to your
computer, or your network. Penterep is not responsible for any illegal
or malicious use of this code. Be Ethical!