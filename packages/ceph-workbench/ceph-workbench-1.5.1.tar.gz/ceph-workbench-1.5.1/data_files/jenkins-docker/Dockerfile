FROM jenkins
USER root
RUN apt-get update && apt-get install -y openssh-server
# Standard SSH port
EXPOSE 22

RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

RUN ( echo '#!/bin/bash' ; echo /usr/sbin/sshd ; echo /usr/local/bin/jenkins.sh ) > /usr/local/bin/jenkins-and-ssh.sh ; chmod +x /usr/local/bin/jenkins-and-ssh.sh

ENTRYPOINT ["/usr/local/bin/jenkins-and-ssh.sh"]
