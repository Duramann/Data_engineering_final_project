pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                bat 'docker-compose up --build -d'
            }
        }
        stage('Switching to release branch'){
            steps{
                bat 'git checkout release'
            }
        }
        stage('Deliver'){
            steps{
                withCredentials([usernamePassword(credentialsId: '40c32c2c-2d64-4582-98fb-edef62acg474', usernameVariable: 'Duramann', passwordVariable: 'Cocolea@01')]) {
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push'
            }
        }
    }
}
