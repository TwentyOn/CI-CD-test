pipeline {
  agent {
    docker {
    image 'python:3.14-alpine'

    }
  }
  stages {
    stage('Test') {
      steps {
        echo 'building...'
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
        echo 'building...'
      }
    }

    stage('Deploy') {
      steps {
        echo 'deploying...'
        sh '''
            ssh -i ~/.ssh/jenkins_key root@155.212.247.178
            exit
        '''
      }
    }

  }
}