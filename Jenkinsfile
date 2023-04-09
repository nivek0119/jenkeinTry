pipeline {
    agent any 
    stages {
        stage('Stage_1 - Install packages') { 
            steps {
               sh 'sudo pip install ncclient'
               sh 'sudo pip install pandas'
               sh 'sudo pip install ipaddress'
               sh 'sudo pip install netaddr'
               sh 'sudo pip install prettytable'
            }
        }
        stage('Stage_2 - Checking and Fixing Violations') { 
            steps {
                echo 'stage3-pylint'
                // sh "sudo pylint /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }

        stage('Stage_3 - Running the application') { 
            steps {
                sh "sudo python3 /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }
        stage('Stage_4 - Unit Testing') { 
            steps {

                echo "sudo python3 /home/kevin/Desktop/Lab9_Jenkins_Desktop/netman_netconf_obj2.py"
            }
        }
    
    }
    post {
        always {
            // emailext attachLog: true, body: '', subject: 'build status', to: 'kevin.chotaliya@colorado.edu'
            emailext attachLog: true, body: ' Your project named "$PROJECT_NAME" with Build Number "$BUILD_NUMBER" is "$BUILD_STATUS" \nTo see more, open below attached Log File', subject: 'Your New Build is $BUILD_STATUS', to: 'kevin.chotaliya@colorado.edu'
            // emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}