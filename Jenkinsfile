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
                withCredentials([usernamePassword(credentialsId: 'GitHub', usernameVariable: 'user', passwordVariable: 'password')]) {
                    bat 'git add .'
                    bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                    bat 'git push https://${password}@github.com/Duramann/Data_engineering_final_project.git'
            }
        }
    }
}
}
