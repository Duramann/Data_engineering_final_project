pipeline {
    agent any
    stages{
        stage('Switching to release branch'){
            steps{
                bat 'git checkout release'
            }
        }
        stage('Build Docker Image'){
            steps{
                bat 'docker-compose down'
                bat 'docker-compose up --build -d'
            }
        }
        stage('Execute Tests'){
            steps{
                bat 'pytest'
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
}