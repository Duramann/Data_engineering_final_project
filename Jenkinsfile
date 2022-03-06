pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                bat 'docker-compose up --build -d'
            }
        stage('Testing'){
		    steps{
                bat 'docker exec flask-app python app_test.py --verbose'
            } 
	}
    }
}
}

