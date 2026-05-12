pipeline {
  agent none

  stages {
    stage('Test') {
        agent {
            docker {
                image 'python:3.14-alpine'
                }
        }
        steps {
            echo 'тестирование...'
            sh '''
                python -m venv .venv
                source .venv/bin/activate
                pip3 install -r requirements.txt
                python manage.py migrate
                python manage.py test
            '''
          }
    }

    stage('Build') {
      steps {
        echo 'сборка...'
      }
    }

    stage('Deploy') {
        agent any
        steps {
          echo 'развертывание...'
          sh '''
              ssh -i ~/.ssh/jenkins_key root@155.212.247.178
              exit
          '''
        }
      }
  }
}