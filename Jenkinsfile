pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git 'https://github.com/nileshMeera123/OpenCartV1.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest -s -v .\\testCases
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
        }
        failure {
            echo "Tests failed"
        }
    }
}
