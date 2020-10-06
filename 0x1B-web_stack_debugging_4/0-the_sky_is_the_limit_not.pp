#script to raise worker limits for nginx

exec { 'change ulimit':
  command => 'sed -i s/15/2000/g /etc/default/nginx',
  path    => '/bin'
}
exec { 'nginx reload':
  command => 'service nginx restart'
}
