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

$index_cont = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body
</html>"


package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

-> file { '/data':
  ensure  => 'directory'
}

-> file { '/data/web_static':
  ensure => 'directory'
}

-> file { '/data/web_static/releases':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}

-> file { '/data/web_static/shared':
ensure => 'directory'
  }

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $index_cont
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

-> file { '/var/www/html':
  ensure => 'directory'
}

-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => $index_cont
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page"
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $config_nginx
}

-> exec { 'nginx restart':
  path => '/etc/init.d/'
}
