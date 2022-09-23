pipeline {
    options([[$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10']]]);
    agent any
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