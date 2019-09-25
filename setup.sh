cd ~/
wget http://archive.ubuntu.com/ubuntu/pool/universe/o/openssl098/libssl0.9.8_0.9.8o-7ubuntu3.2.14.04.1_i386.deb
dpkg -i *.deb
rm *.deb
git clone https://github.com/jlgaddis/iou2net.git
ln -s /usr/lib/i386-linux-gnu/libcrypto.so.0.9.8 /usr/lib/libcrypto.so.4
chmod +x /root/iou2net/iou2net.pl
