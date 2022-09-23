pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
    }triggers {
        githubPush()
        cron '@hourly'
    }stages {
        stage('run tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pytest --browser firefox task3.1/toolsQAProject'
                    }else {
                        bat 'pytest --browser firefox task3.1/toolsQAProject'
                    }  
                }
            }
        }
    }
}