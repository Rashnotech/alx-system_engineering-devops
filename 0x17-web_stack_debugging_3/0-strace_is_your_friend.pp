# puppet to fix apache returning 500 error

exec { 'remove extra p':
  command  => "sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => shell,
}
