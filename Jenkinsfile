pipeline {
    agent any

    stages {
        stage ('SCM') {
            steps {
                git branch: 'master', url: 'https://github.com/pythoncpp/jenkins-html-demo.git'
            }
        }
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_WutX3ighYn5leDCE1jYhdftLlxg | /usr/bin/docker login -u shrijeet99 --password-stdin'
            }
        }
        stage ('docker build image') {
            steps {
                sh '/usr/bin/docker image build -t shrijeet99/mywebsite .'
            }
        }
        stage ('docker push image') {
            steps {
                sh '/usr/bin/docker image push shrijeet99/mywebsite'
            }
        }
        stage ('docker remove service') {
            steps {
                sh '/usr/bin/docker service rm myservice'
            }
        }
        stage ('docker create service') {
            steps {
                sh '/usr/bin/docker service create --name myservice -p 9090:80 --replicas 5 shrijeet99/mywebsite'
            }
        }
    }
}

