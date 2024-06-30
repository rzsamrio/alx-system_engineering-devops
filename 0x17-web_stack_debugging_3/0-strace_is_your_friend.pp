# Automate the fixing of an Apache server due to missing file

file {'/var/www/html/wp-includes/class-wp-locale.phpp':
    ensure => link,
    target => '/var/www/html/wp-includes/class-wp-locale.php',
}
