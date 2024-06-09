pipeline {
    agent { label 'builder' }
    environment {
        ARTIFACTS_BASEURL = 'http://artifactsrepo:8081/nexus/repository'
        ARTIFACTS_PUBLISHER = credentials('NEXUS_PUBLISHER_CREDENTIALS')
        CODE_COMMITTER = credentials('GITEA_CREDENTIALS')
        DISCORD_URL = 'https://discord.com/api/webhooks/1233451596676071527/iomVt3QPH4WLnWAO2hLmdKmW_QT-HgQpPyiQpxAWGic3wmztObLis33tHmPygCPbDX-_'
        TOOLS_DIR = '/home/jenkins/tools'
        VERSION = readFile(file: 'version.txt')
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
                sh '. ./venv/bin/activate && pip install -r ./requirements.txt build bump wheel && python -m build'
                sh 'mkdir -p ./dist/evidence'
            }
        }
        stage('Code and Artifact Scans') {
            parallel {
                stage('Generate SBOM') {
                    steps {
                        sh 'trivy fs . --format spdx-json --output ./dist/evidence/sbom.json'
                    }
                }
                stage('Find vulnerabilities') {
                    steps {
                        sh 'trivy fs . --format spdx-json --output ./dist/evidence/sbom.json'
                    }
                }
                stage('Find secrets') {
                    steps {
                        sh 'gitleaks detect -r ./dist/evidence/gitleaks.xml -f junit'
                    }
                }
            }
        }
        stage('Publish Artifacts') {
            steps {
                sh '''
                zip -r ./evidence.zip ./evidence
                curl -v -u $ARTIFACTS_PUBLISHER_USR:$ARTIFACTS_PUBLISHER_PSW --upload-file evidence.zip \
                    $ARTIFACTS_BASEURL/raw-hosted/cicdlab-flask-runner/$VERSION/cicdlab_flask_runner-$VERSION-evidence.zip
                twine upload -u $ARTIFACTS_PUBLISHER_USR -p $ARTIFACTS_PUBLISHER_PSW \
                    --repository-url $ARTIFACTS_BASEURL/pypi-hosted/ dist/*
                python -m bumpversion patch
                cat ./version.txt
                '''
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
                webhookURL: env.DISCORD_URL
            deleteDir()
        }
    }
}
