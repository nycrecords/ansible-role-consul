import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

def test_consul_is_installed(host):
    consul = host.file("/usr/local/bin/consul")

    assert consul.is_symlink
    with host.sudo():
        assert "/opt/consul/consul" == consul.linked_to

def test_dnsmasq_is_installed(host):
    dnsmasq = host.file("/usr/sbin/dnsmasq")

    assert dnsmasq.exists


def test_dnsmasq_is_running(host):
    dnsmasq = host.service("dnsmasq")

    assert dnsmasq.is_running
    assert dnsmasq.is_enabled
