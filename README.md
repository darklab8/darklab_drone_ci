# Description
Drone CI for k8s deployment to be attached to github

# Requirements
## to deploy you will need secrets.yaml with next values
```yml
rpc_secret: "make generate_rpc_secret"
github_client_id: "Create OAuth application in developer settings"
github_secret: "Create OAuth application in developer settings"
htpasswd: "generated nginx httpasswd"
```

# Deployment:
* add the secrets.yaml to k8s/drone_ci/secrets.yaml
* run `python3 install.py`