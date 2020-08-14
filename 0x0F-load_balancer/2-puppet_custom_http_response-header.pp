# set http header X-Served-By
exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
    ensure => installed,
}
-> file { '/var/www/html/index.html' :
    content => 'Holberton School!',
}
-> file_line { 'add header' :
    ensure => present,
    path   => 'etc/nginx/sites-available/default',
    line   => "add_header X-Served-By ${hostname}:",
    after  => 'listen 80 default_server',
}
-> service { 'nginx' :
    ensure => running,
}
