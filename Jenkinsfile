pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'onec1/drf-app'
    SERVER_IP = '155.212.247.178'
    SERVICE_USER = 'root'
  }

  stages {
    stage('Build') {
        steps {
            sh 'docker build -t service .'
        }
    }

    stage('Test') {
        steps {
            echo 'тестирование...'
            sh '''
                docker run --rm service
                docker exec -it service python manage.py migrate
                docker exec -it service python manage.py test
                docker stop service
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