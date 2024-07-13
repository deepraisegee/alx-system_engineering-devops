# puppet agent

node '52.73.38.28' {
  package { 'nginx':
    ensure    => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasstatus  => true,
    hasrestart => true,
  }

  file { '/etc/nginx/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/html/404.html':
    ensure  => file,
    content => "Ceci n'est pas une page",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => @("END"),
		  server {
			  listen		80 default_server;
			  listen		[::]:80 default_server;
			  root			/etc/nginx/html;
			  index			index.html;

			  error_page	404 /404.html;

			  location		/redirect_me {
				  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
			  }

			  location /404 {
				  root /etc/nginx/html;
				  internal;
			  }
		  }
	END
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => link,
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

}
