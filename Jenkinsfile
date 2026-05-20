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
            sh 'docker build -t ${DOCKER_USER}/si_${SERVICE_TAG} ./backend/'
        }
    }

    stage('Test') {
        steps {
            echo 'тестирование...'
            sh '''
                docker run --name sc_${SERVICE_TAG} --rm -d ${DOCKER_USER}/si_${SERVICE_TAG}
                docker exec sc_${SERVICE_TAG} python manage.py migrate
                docker exec sc_${SERVICE_TAG} python manage.py test
                docker stop sc_${SERVICE_TAG}
            '''
          }
    }

    stage('Deploy') {
        steps {
          echo 'развертывание...'
          sh 'docker push ${DOCKER_USER}/si_${SERVICE_TAG}:latest'
          sh '''
            ssh -i ~/.ssh/jenkins_key root@155.212.247.178 << EOF
            pwd
            ls
          '''
        }
      }
  }
  post {
    always {
        sh 'docker stop sc_service || true'
        sh 'docker rmi ${DOCKER_USER}/si_service || true'
    }
  }
}