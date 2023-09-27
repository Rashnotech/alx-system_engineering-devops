# Installing nginx

package { 'nginx':
  ensure => 'installed',
}

# Ensure nginx is running

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
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
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a custom HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
