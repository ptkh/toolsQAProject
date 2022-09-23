pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr:'10'))
        disableConcurrentBuilds()
    }agent any
    triggers {
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