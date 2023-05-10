# Script to fix 500 error when a GET HTTP method is
# requested from the Apache server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
