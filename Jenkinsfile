pipeline {
  agent any

  stages {
    stage('Test') {
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