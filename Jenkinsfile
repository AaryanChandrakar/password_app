pipeline {

    agent any

    triggers {
        pollSCM('* * * * *')
    }


    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from SCM...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat 'python password_app.py'
            }
        }


        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }


        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
