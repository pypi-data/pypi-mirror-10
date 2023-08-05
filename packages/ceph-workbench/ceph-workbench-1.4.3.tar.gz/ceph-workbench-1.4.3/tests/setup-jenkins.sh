set -x
mkdir -p $(pwd)/data/jenkins
docker build -t ceph-jenkins data_files/jenkins-docker
docker run -d --name jenkins -p 50000:50000 -p 11080:8080 -p 5555:22 -v $(pwd)/data/jenkins:/var/jenkins_home ceph-jenkins
mkdir -p data/jenkins/.ssh
ssh-keygen -N '' -f data/jenkins/.ssh/id_rsa
cat data/jenkins/.ssh/id_rsa.pub >> data/jenkins/.ssh/authorized_keys
docker rmi ceph-jenkins-slave
docker rmi libguestfs
rm -fr ubuntu-14.04-i386
sleep 180
python tests/jenkins-define-credentials.py http://127.0.0.1:11080
