# Use Debian 12 (Bookworm) as the base image
FROM debian:12

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    apt-transport-https \
    perl \
    libnet-ssleay-perl \
    openssl \
    libauthen-pam-perl \
    libpam-runtime \
    libio-pty-perl \
    shared-mime-info \
    net-tools \
    libxml-parser-perl \
    && rm -rf /var/lib/apt/lists/*

# Add Webmin repository
RUN curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh
RUN chmod +x ./setup-repos.sh && echo y | ./setup-repos.sh

# Install Webmin
RUN apt-get install -y webmin --install-recommends && rm -rf /var/lib/apt/lists/*

# Expose Webmin port
EXPOSE 10000

RUN echo '#!/bin/bash\n\
if [ -n "$WEBMIN_PASSWORD" ]; then\n\
    /usr/share/webmin/changepass.pl /etc/webmin root "$WEBMIN_PASSWORD"\n\
    echo "Webmin password has been set."\n\
else\n\
    echo "WEBMIN_PASSWORD environment variable is not set. Using default password."\n\
fi\n\
echo "Starting Webmin..."\n\
/usr/bin/perl /usr/share/webmin/miniserv.pl /etc/webmin/miniserv.conf &> /var/log/webmin.log &\n\
tail -f /var/log/webmin.log\n\
' > /start-webmin.sh && chmod +x /start-webmin.sh

# Start Webmin using the startup script
CMD ["/start-webmin.sh"]
