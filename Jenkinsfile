pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --alluredir=results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate results -o report --clean'
            }
        }
    }
}
