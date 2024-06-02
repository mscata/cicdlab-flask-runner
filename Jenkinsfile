pipeline {
    agent {
        docker {
            image 'mscata/cicdlabs-ciagent'
        }
    }
    environment {
        TOOLS_DIR = '/home/jenkins/tools'
        DISCORD_URL = 'https://discord.com/api/webhooks/1233451596676071527/iomVt3QPH4WLnWAO2hLmdKmW_QT-HgQpPyiQpxAWGic3wmztObLis33tHmPygCPbDX-_'
        NEXUS_PUBLISHER = credentials('NEXUS_PUBLISHER_CREDENTIALS')
    }
    stages {
        stage('Check out code') {
            steps {
                sh 'printenv | sort -h'
                checkout scm
            }
        }
        stage('Build and Test') {
            steps {
                sh 'python3 -m venv ./venv'
                sh '. ./venv/bin/activate && pip install -r ./requirements.txt build && python -m build'
            }
        }
        stage('Code and Artifact Scans') {
            parallel {
                stage('Dependency Check') {
                    environment {
                        DC_HOME = tool 'Dependency Check'
                    }
                    steps {
                        sh "$DC_HOME/bin/dependency-check.sh -n -s ./cicdlab-flask-runner -f HTML -f JSON --prettyPrint"
                    }
                }
                stage('Trivy') {
                    steps {
                        sh 'trivy fs ./cicdlab-flask-runner'
                    }
                }
            }
        }
        stage('Publish Artifacts') {
            steps {
                sh 'twine upload -u $NEXUS_PUBLISHER_USR -p $NEXUS_PUBLISHER_PSW --repository-url http://artifactsrepo:8081/nexus/repository/pypi-hosted/ dist/*'
            }
        }
    }
    post {
        always {
            discordSend description: "CI/CD Lab Build: Flask Runner",
                footer: "Marco's CI/CD Lab",
                link: "",
                result: currentBuild.currentResult,
                title: currentBuild.fullDisplayName,
                webhookURL: discordWebHookUrl
            deleteDir()
        }
    }
}
