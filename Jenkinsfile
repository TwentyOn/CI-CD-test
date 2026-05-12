pipeline {
  agent docker {
    image 'python:3.14-alpine'
  }
  stages {
    stage('build') {
      steps {
        echo 'building...'
        sh '''
            python manage.py migrate
            python manage.py test
        '''
      }
    }

  }
}