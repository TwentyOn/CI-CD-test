pipeline {
    agent {
        docker {
            image 'python:3.14-alpine'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'python -m manage.py showmigrations'
            }
        }
    }
}