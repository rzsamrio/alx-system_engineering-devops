# Configure the server via puppet

# Install nginx server
package { 'nginx' :
    ensure   => installed,
    provider => 'apt',
}


# Get rid of all html files
exec { 'remove' :
    command  => 'usr/bin/env rm -f /var/www/html/*',
    provider => absent,
}

# Create landing page 
file {'/var/www/html/index.html' :
    ensure  => present,
    content => 'Hello World!'
}

# Create the config file
file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html; 
    
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}'
}

# Ensure nginx is running
service { 'nginx' :
    ensure => running,
    name   => 'nginx'
}
