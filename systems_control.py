import subprocess


def shutdown_pi():
    subprocess.run(["sudo", "/sbin/shutdown", "now"])
