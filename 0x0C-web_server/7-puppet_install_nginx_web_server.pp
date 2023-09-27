# Installing nginx
include stdlib

package { 'nginx':
}

# Ensure nginx is running

exec { 'install nginx':
  command = 'apt -y update; apt-get -y install',
  provide => shell,
}

# Configuration Nginx server for port 80

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    server_name _;
    
    location / {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4
    }
    location /redirect_me {
    }
  }"
  require => Exec['install nginx'],
}

# Create a custom HTML file
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Exec['install nginx'],
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
