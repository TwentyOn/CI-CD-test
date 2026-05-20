pipeline {
  agent none

  environment {
    DOCKER_IMAGE = 'onec1/drf-app'
    SERVER_IP = '155.212.247.178'
    SERVICE_USER = 'root'
  }

  stages {
    stage('Build') {
        agent { dockerfile { dir 'backend' } }
        steps {
            sh 'docker ps -a'
        }
    }

    stage('Test') {
        agent {
            docker {
                image 'python:3.14-alpine'
                }
        }
        steps {
            echo 'тестирование...'
            sh '''
                cd backend
                python -m venv .venv
                source .venv/bin/activate
                pip3 install -r requirements.txt
                python manage.py migrate
                python manage.py test
            '''
          }
    }

    stage('Deploy') {
        agent any
        steps {
          echo 'развертывание...'
          sh '''
            ssh -i ~/.ssh/jenkins_key root@155.212.247.178 'pwd'
          '''
        }
      }
  }
}