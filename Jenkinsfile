pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                bat 'docker-compose up --build -d'
            }
        }
        stage('Lauching Test inside of Docker Image'){
		    steps{
                bat 'docker exec flask-app-project python test_web_app.py --verbose'
            } 
	}
    }
}

