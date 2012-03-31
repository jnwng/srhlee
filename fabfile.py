from fabric.api import *
import fabric.contrib.project as project
import os
from os import path

DEST = 'ssh.phx.nearlyfreespeech.net'
DEST_PATH = '/home/public/'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'build')
env.activate='source ' + os.path.join(ROOT_PATH, 'bin/activate')
env.hosts = ["jnwng_srhlee@ssh.phx.nearlyfreespeech.net"]

def virtualenv(command):
    with cd(ROOT_PATH):
        local(env.activate + ' && ' + command)

def clean():
    local('rm -rf ./deploy')

def regen():
    virtualenv('wintersmith build')

def deploy():
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )

def serve():
    regen()
    virtualenv('wintersmith preview')



