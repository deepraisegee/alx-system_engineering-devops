# install flask from pip3.

$deps = ['python3', 'python3-pip']

package { $deps:
    ensure  => 'installed',
}

exec { 'install flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
}
