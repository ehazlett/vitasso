from fabric.api import local, task

@task
def deploy():
    local('hyde gen')
    local('vmc update')
