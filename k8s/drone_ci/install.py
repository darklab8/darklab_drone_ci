import os

def shell(cmd):
    print(cmd)
    status_code = os.system(cmd)

    if status_code != 0:
        exit(status_code)

shell("cd files; ./generate_ssl.sh")
shell(f'helm upgrade --install --create-namespace --namespace drone-ci drone-ci . --values=secrets.yaml')