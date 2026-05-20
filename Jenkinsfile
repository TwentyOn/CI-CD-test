pipeline {
  agent any

  environment {
    SERVICE_TAG = 'service'
    DOCKER_USER = 'onec1'
    SERVER_IP = '155.212.247.178'
    SERVICE_USER = 'root'
  }

  stages {
    stage('Build') {
        steps {
            sh 'docker build -t si_service ./backend/'
        }
    }

    stage('Test') {
        steps {
            echo 'тестирование...'
            sh '''
                docker run --name sc_service --rm -d si_${SERVICE_TAG}
                docker exec sc_service python manage.py migrate
                docker exec sc_service python manage.py test
                docker stop sc_${SERVICE_TAG}
            '''
          }
    }

    stage('Deploy') {
        steps {
          echo 'развертывание...'
          sh 'docker push ${DOCKER_USER}/$sc_{SERVICE_TAG}'
          sh '''
            ssh -i ~/.ssh/jenkins_key root@155.212.247.178 'pwd'
          '''
        }
      }
  }
  post {
    always {
        sh 'docker stop sc_service || true'
        sh 'docker rmi si_service || true'
    }
  }
}