# fix 500 error in apache
exec { 'usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
