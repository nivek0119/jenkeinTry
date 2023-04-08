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
        stage('Pylint') { 
            steps {
                sh "su kevin && whoami"
                // sh "whoami"
            }
        }

        stage('Running python Code') { 
            steps {
                echo "sudo python3 /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }
    }
}