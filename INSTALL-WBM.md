## Turtlefirewall Webmin Module

Download source.
```
cd /tmp
wget https://github.com/netcons/turtlefirewall/archive/master.zip -O turtlefirewall-master.zip
unzip turtlefirewall-master.zip
cd turtlefirewall-master
```

Build source.
```
chmod +x build-wbm
./build-wbm
```

Install RHEL.
```
dnf -y install perl-XML-Parser perl-Net-CIDR-Lite perl-Text-CSV_XS ipset conntrack-tools rsyslog wget dos2unix awk
/usr/libexec/webmin/install-module.pl /tmp/turtlefirewall-master/build/turtlefirewall-*.wbm.gz
```

Install Debian.
```
apt-get -y install libxml-parser-perl libnet-cidr-lite-perl libtext-csv-xs-perl ipset conntrack rsyslog wget dos2unix gawk
/usr/share/webmin/install-module.pl /tmp/turtlefirewall-master/build/turtlefirewall-*.wbm.gz
```

## Kernel Module Build Requirements

RHEL.
```
dnf -y install kernel-devel kernel-headers
dnf -y install iptables-devel libpcap-devel json-c-devel libgcrypt-devel perl-File-Path
dnf -y install autoconf automake libtool
dnf -y install dkms
dnf enable dkms --now
```

Debian.
```
apt-get -y install libxtables-dev libpcap-dev libjson-c-dev libgcrypt-dev libmodule-path-perl
apt-get -y install autoconf automake libtool
apt-get -y install dkms
```

## IPT Ratelimit Kernel Module

Download source.
```
cd /usr/src
wget https://github.com/aabc/ipt-ratelimit/archive/master.zip -O ipt-ratelimit-master.zip
unzip ipt-ratelimit-master.zip
mv ipt-ratelimit-master ipt-ratelimit-0.3.3
rm -rf ipt-ratelimit-master.zip
cd ipt-ratelimit-0.3.3
```

Install module.
```
wget https://raw.githubusercontent.com/netcons/turtlefirewall/master/dkms-ipt-ratelimit.conf -O ./dkms.conf
dkms add -m ipt-ratelimit -v 0.3.3
dkms build -m ipt-ratelimit -v 0.3.3
dkms install -m ipt-ratelimit -v 0.3.3
```

Install library.
```
make all install
```

## XTables Addons Kernel Module.

Download source.
```
cd /usr/src
wget https://inai.de/files/xtables-addons/xtables-addons-3.26.tar.xz -O xtables-addons-3.26.tar.xz
tar -xvf xtables-addons-3.26.tar.xz
rm -rf xtables-addons-3.26.tar.xz
cd xtables-addons-3.26
```

Install module.
```
wget https://raw.githubusercontent.com/netcons/turtlefirewall/master/dkms-xtables-addons.conf -O ./dkms.conf
dkms add -m xtables-addons -v 3.26
dkms build -m xtables-addons -v 3.26
dkms install -m xtables-addons -v 3.26 
```

Install library.
```
./configure --without-kbuild --prefix=/usr
make
make install
```

Download database.
```
/etc/cron.daily/xt_geoip_update
```

## nDPI Netfilter Kernel Module

Download source.
```
cd /usr/src
wget https://github.com/vel21ripn/nDPI/archive/master.zip -O nDPI-flow_info-4.zip
unzip nDPI-flow_info-4.zip
mv nDPI-flow_info-4 ndpi-netfilter-4.11.0
rm -rf nDPI-flow_info-4.zip
cd ndpi-netfilter-4.11.0
rm -rf windows
```

Install module.
```
wget https://raw.githubusercontent.com/netcons/turtlefirewall/master/dkms-ndpi-netfilter.conf -O ./dkms.conf
dkms add -m ndpi-netfilter -v 4.11.0
dkms build -m ndpi-netfilter -v 4.11.0
dkms install -m ndpi-netfilter -v 4.11.0
```

Install library.
```
./autogen.sh
cd ndpi-netfilter
make
make install
```