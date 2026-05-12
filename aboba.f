pipeline {
    agent {
        docker {
            image 'python:3.14-alpine'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    ls -a
                    python -m venv .venv
                    source .venv/bin/activate
                    pip install -r requirements.txt
                    python manage.py showmigrations
                '''
            }
        }
    }
}