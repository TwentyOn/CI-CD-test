pipeline {
    agent {
        docker {
            image 'python:3.14-alpine'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'ls -a'
                sh 'pip install -r requirements.txt'
                sh 'python manage.py showmigrations'
            }
        }
    }
}