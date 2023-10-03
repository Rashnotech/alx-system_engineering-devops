# a puppet script to creat a custom HTTP header response
include stdlib

package { 'nginx':
  ensure => installed,
}

exec { 'install nginx':
  command  => 'sudo apt update && sudo apt -y install nginx',
  provider => shell,
}

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    server_name _;
    add_header X-Served-By $hostname;
    root /var/www/html;
    location / {
      index index.html;
    }
    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    error_page 404 /404.html;
    location /404.html {
      root /var/www/html;
      internal;
    }
  }",
  require => Exec['install nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Exec['install nginx']
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Exec['install nginx']
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => File['/etc/nginx/sites-available/default'],
}
