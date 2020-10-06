#up the holberton user open file limit

exec { 'hard file limit':
  command => "sed -i 's/hard nofile 5/hard nofile 4000/g' /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'soft file limit':
  command => "sed -i 's/soft nofile 4/soft nofile 4000/g' /etc/security/limits.conf",
  path    => '/bin'
}
