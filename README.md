## Development Environment

Install prerequisites:

* hypervisor
* kubectl
* minikube
* docker
* helm

Full setup instructions for different platfrom you can find [here](https://kubernetes.io/docs/tasks/tools/install-minikube/)

For example, local setup on OS X (minikube on VirtualBox with local Docker registry):
```
brew update
brew install kubectl
brew cask install docker minikube virtualbox
brew install kubernetes-helm
```

Run and check minikube (or just switch to minikube context if you have it already with `kubectl config use-context minikube`):
```
minikube start
minikube status
```

Enable Ingress support:
```
minikube addons enable ingress
```

Utilize docker daemon:
```
eval $(minikube docker-env)
```

Start/Configure helm:
```
helm init
```

Run local Docker registry (to access a private container registry, follow the [steps](https://kubernetes.io/docs/concepts/containers/images/):
```
docker run -d -p 5000:5000 --restart=always --name registry -v /tmp/registry:/var/lib/registry registry:2
```

Build and push application image:
```
docker build -t localhost:5000/flask-angular-app:0.1 .
docker push localhost:5000/flask-angular-app:0.1
```

Run unit test for Flask app:
```
python app/app_test.py
```

Deploy application via helm with shared volume support:
```
helm install ./flask-angular-app/ --set service.type=ClusterIP,volumes.enabled=true,volumes.path=$(pwd)/app
```

Add default `ingress.host` value into hosts:
```
echo "$(minikube ip) flask.angular.local" | sudo tee -a /etc/hosts
```

Check application and hello API is running:

http://flask.angular.local/

http://flask.angular.local/hello?name=Arilot


## Jenkins CI/CD


Install Jenkins in Minikube with [kubernetes plugin](https://github.com/jenkinsci/kubernetes-plugin) support:
```
helm install stable/jenkins --set Master.ServiceType=NodePort
```

Configure Jenkins:

* Set Docker Registry credentials (Manage Jenkins -> Configure System)
* Create and configure new Pipeline Job (Pipeline script from SCM, SCM credentials)
* Create Docker Registry credenstials with name `registry` (or update in Jenkinsfile)
* Configure required Build Triggers
