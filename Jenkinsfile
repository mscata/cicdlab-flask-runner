node {
    def toolsDir = '/home/jenkins/tools'
    def discordWebHookUrl = 'https://discord.com/api/webhooks/1233451596676071527/iomVt3QPH4WLnWAO2hLmdKmW_QT-HgQpPyiQpxAWGic3wmztObLis33tHmPygCPbDX-_'
    sh 'printenv | sort -h'
    stage('Check out Git repo') {
        scm checkout
    }
    stage('Build and Test') {
        dir('cicdlab-flask-runner') {
            sh 'python3 -m venv ./venv'
            sh '. ./venv/bin/activate && pip install -r ./requirements.txt build && python -m build'
        }
    }
    stage('Code and Artifact Scans') {
        parallel(
            'Dependency Check': {
                stage('Dependency Check') {
                    def toolLocation = tool 'Dependency Check'
                    sh "$toolLocation/bin/dependency-check.sh -n -s ./cicdlab-flask-runner -f HTML -f JSON --prettyPrint"
                }
            },
            'Trivy': {
                stage('Trivy') {
                    sh 'trivy fs ./cicdlab-flask-runner'
                }
            }
        )
    }
    stage('Publish Artifacts') {
        dir('cicdlab-flask-runner') {
            sh 'twine upload --repository-url http://artifactsrepo:8081/nexus/repository/pypi-hosted/simple dist/*'
        }
    }
    stage('Send Notification') {
        parallel(
            'Discord': {
                stage('Discord') {
                    discordSend description: "CI/CD Lab Build: Flask Runner",
                        footer: "Marco's CI/CD Lab",
                        link: "",
                        result: currentBuild.currentResult,
                        title: currentBuild.fullDisplayName,
                        webhookURL: discordWebHookUrl
                }
            }
        )
    }
}
