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
                echo 'stage3-pylint'
                // sh "sudo pylint /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }

        stage('Running python Code') { 
            steps {
                echo "sudo python3 /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }
    }
    post {
        always {
            // emailext attachLog: true, body: '', subject: 'build status', to: 'kevin.chotaliya@colorado.edu'
            emailext attachLog: true, body: ' Your project named "$PROJECT_NAME" with Build Number "$BUILD_NUMBER" is "$BUILD_STATUS" \nTo see more, open below attached Log File', subject: 'Your New Build Status', to: 'kevin.chotaliya@colorado.edu'
            // emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}