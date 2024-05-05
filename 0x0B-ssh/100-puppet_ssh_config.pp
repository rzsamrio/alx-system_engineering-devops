# Updating the config file via puppet

include stdlib

file_line { 'Turn off passwd auth' :
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PubkeyAuthentication yes',
  match  => '^PubkeyAuthentication'
}

file_line {'Declare identity file' :
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile'
}
