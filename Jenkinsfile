pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\galla\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\galla\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest --alluredir=results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '"C:\\allure\\allure-2.38.0\\allure-2.38.0\\bin\\allure.bat" generate results -o report --clean'
            }
        }
    }
}
