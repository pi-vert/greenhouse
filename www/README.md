# Web

## Installation 

     sudo apt-get install lighttpd


 edit /etc/lighttpd/lighttpd.conf

server.modules = (
        "mod_access",
        "mod_alias",
        "mod_compress",
        "mod_redirect",
        "mod_cgi",
)

$HTTP["url"] =~ "/cgi-bin/" {
 cgi.assign = ( ".py" => "/usr/bin/python3",".cgi"=> "/usr/bin/python3" )
}

sudo service lighttpd force-reload 

sudo lighty-enable-mod cgi


pi@vert:~/greenhouse/www/html $ sudo lighty-enable-mod cgi
Enabling cgi: ok
Run "service lighttpd force-reload" to enable changes

