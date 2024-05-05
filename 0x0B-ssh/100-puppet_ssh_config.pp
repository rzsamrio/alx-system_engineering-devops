# Updating the config file via puppet

file { '/etc/ssh/ssh_config' :
  ensure  => 'present',
  content => "Host alxserver-132327-web-01
        HostName 54.125.243.76
        User ubuntu
        IdentityFile ~/.ssh/school
        PubkeyAuthentication yes"
}
