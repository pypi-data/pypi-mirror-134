import os
import socket
import subprocess
from contextlib import closing
from pathlib import Path
from uuid import uuid4

import attr
from levo_commons.providers import ZaproxyProvider as ZaproxyProviderInterface

from levocli.logger import get_logger

logger = get_logger(name="ZAPROXY")


def get_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


@attr.s(slots=True, repr=False)
class ZaproxyProvider(ZaproxyProviderInterface):
    ip: str = attr.ib(default="127.0.0.1")
    port: int = attr.ib(default=get_port())
    home_directory: Path = attr.ib(default=Path(f"/tmp/levo.zap.{uuid4()}"))
    api_key: str = attr.ib(default=str(uuid4()))
    process: subprocess.Popen[bytes] = attr.ib(init=False)

    def start(self) -> None:
        self.home_directory.mkdir(parents=True, exist_ok=True)
        zap_sh = Path(
            os.getenv("ZAP_INSTALL_DIR", "/modules/zaproxy/"), "zap.sh"
        ).resolve()
        start_command: list[str] = [
            str(zap_sh),
            "-daemon",
            "-host",
            self.ip,
            "-port",
            str(self.port),
            "-dir",
            str(self.home_directory.resolve()),
            "-config",
            f"api.key={self.api_key}",
        ]
        self.process = subprocess.Popen(start_command, shell=False)
        logger.info(f"Started ZAP at {self.ip}:{self.port}.")

    def stop(self) -> None:
        logger.info("Shutting down ZAP.")
        self.process.terminate()
        self.process.wait()
        logger.info(f"Shut down ZAP.")

    def is_running(self) -> bool:
        # TODO: Does this need some more tests?
        poll = self.process.poll()
        return poll is None
