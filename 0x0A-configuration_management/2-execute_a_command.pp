# Running a command via Puppet

exec { 'pkill':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell'
}
