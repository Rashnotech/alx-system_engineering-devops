# Installing nginx
include stdlib

package { 'nginx':
  ensure => installed,
}

# Ensure nginx is running

exec { 'install nginx':
  command  => 'sudo apt -y update && sudo apt-get -y install nginx',
  provider => shell,
}

# Configuration Nginx server for port 80

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    server_name _;
    root /var/www/html;
    location / {
      index index.html;
    }
    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
  }",
  require => Exec['install nginx'],
}

# Create a custom HTML file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Exec['install nginx'],
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => File['/etc/nginx/sites-available/default'],
}
