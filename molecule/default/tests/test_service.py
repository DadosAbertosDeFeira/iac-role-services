import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_if_container_is_running(host):
    container = host.docker("tika-server")

    assert container.is_running

def test_if_container_is_listening_on_container(host):
    cmd = host.run("docker run --network dokku_services ubuntu sh -c 'apt-get update && apt-get install curl -y && curl tika-server:9998'")

    assert cmd.rc == 0

def test_if_container_is_listening_on_host(host):
    container = host.socket("tcp://0.0.0.0:9998")

    assert container.is_listening == False
