# This puppet manifest is used to set up web static for both servers

$config_nginx = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Serverd-By ${hostname};
    root /var/www/html;
    index index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        autoindex off;
    }
    location /redirect_me {
        return 301 https://youtube.com;
    }
    error_page 404 /custom_404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}"

# Ensure package manager is up to date
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
}

# Ensure nginx is installed
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

# Ensure the directories exists
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Ensure index.html exists correctly
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Ensure symbolic links exists
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Ensure error page present
file { '/var/www/html/custom_404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
}

# Ensure nginx config is ok
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $config_nginx,
}

# ensure nginx is running
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
}
