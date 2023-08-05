import docker

from shell_as_service.client import get_service_port, execute_api_call


def _test():
    from cloudshell.shell.core.driver_context import ReservationContextDetails

    _context = ReservationContextDetails(
        "env_name",
        "env_path",
        "domain",
        "desc",
        "owner_user",
        "owner_email",
        "res_id",
        "",
        "",
        "",
    )
    docker_host = "192.168.85.60"
    docker_user = "root"
    shell_name = "DutShell2G"
    _kwargs = {"context": _context}
    image_name = "saklar13/dut-shell"
    command_name = "shutdown"
    docker_client = docker.DockerClient(
        base_url=f"ssh://{docker_user}@{docker_host}", tls=True
    )
    port = get_service_port(docker_host, docker_client, shell_name, image_name)
    res = execute_api_call(docker_host, port, command_name, _kwargs)
    print(f"result = {res}")  # noqa


if __name__ == '__main__':
    _test()
