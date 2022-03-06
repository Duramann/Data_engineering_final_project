pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                bat 'docker-compose up --build -d'
            }
        }
        stage('Execute Test') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                bat 'pip install --user -r requirements.txt'
                bat 'python -m pytest test_web_app.py'
                }
            }
        stage('Switching to release branch'){
            steps{
                bat 'git checkout release'
            }
        }
        stage('Deliver'){
            steps{
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push'
            }
        }
    }
}
