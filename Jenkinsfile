pipeline {
  agent {
    docker {
    image 'python:3.14-alpine'

    }
  }
  stages {
    stage('build') {
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

  }
}