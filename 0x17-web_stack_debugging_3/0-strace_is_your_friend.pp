# strace on apache process running on user www-data with curl for localhost
# showed no file present named '...<.phpp>' indicating typo

exec { 'sed php line':
  command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php',
  path    => '/bin'
}
