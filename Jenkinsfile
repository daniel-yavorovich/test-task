podTemplate(
  label: 'app',
  containers: [
    containerTemplate(name: 'python', image: 'python:2', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker:1.11', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'helm', image: 'lachlanevenson/k8s-helm:latest', ttyEnabled: true, command: 'cat')
  ],
  volumes: [
    hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')
  ]
)
{
  node('app') {

    def repo = "flask-angular-app"
    def scmVars = checkout(scm)
    def commitHash = scmVars.GIT_COMMIT
    def tag = commitHash[0..6]

    withCredentials([usernamePassword(
      credentialsId: 'registry',
      passwordVariable: 'registry_password',
      usernameVariable: 'registry_user')])
    {
      stage('Checkout') {
        checkout(scm)
      }
      stage('Unit Test') {
        container('python') {
          sh "pip install -r app/requirements.txt"
          sh "python app/app_test.py"
        }
      }
      stage('Docker Build') {
        container('docker') {
          sh "docker build -t ${env.registry_user}/${repo}:${tag} ."
          sh "docker login -u ${env.registry_user} -p ${env.registry_password}"
          sh "docker push ${env.registry_user}/${repo}:${tag}"
        }
      }
      stage('Deploy Approval') {
        input "Deploy Application with Helm?"
      }
      stage('Helm Deploy') {
        container('helm') {
          sh "helm upgrade ${repo} ./${repo}/ --set image.repository=${env.registry_user}/${repo},image.tag=${tag} || helm install --name ${repo} ./${repo}/ --set service.type=ClusterIP,image.repository=${env.registry_user}/${repo},image.tag=${tag}"
          sh "helm history ${repo}"
        }
      }
    }
  }
}
