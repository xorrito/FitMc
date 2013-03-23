cd `dirname $0`
user=`whoami`
sudo chown -R root:root .
sudo dpkg --build FitMc .
sudo chown -R $user:$user .
