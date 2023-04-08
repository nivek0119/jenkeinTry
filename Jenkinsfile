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
               sh 'sudo pip install ncclient'
               sh 'sudo pip install pandas'
               sh 'sudo pip install ipaddress'
               sh 'sudo pip install netaddr'
               sh 'sudo pip install prettytable'
            }
        }
        stage('Deploy') { 
            steps {
                echo "welcome to Deploystage"
            }
        }
    }
}