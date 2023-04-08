pipeline {
    agent any 
    stages {
        stage('Install Packages') { 
            steps {
                echo "welcome to buildstage"
            }
        }
        stage('Test') { 
            steps {
               sh 'pip install ncclient'
            }
        }
        stage('Deploy') { 
            steps {
                echo "welcome to Deploystage"
            }
        }
    }
}