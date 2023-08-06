from pathlib import Path
from typing import Any, Mapping

from aioworkers.core.config import ValueExtractor
from aioworkers.storage.http import Storage

BASE = Path(__file__).parent

configs = (BASE / "config.ini",)


class Client(Storage):
    _service: Mapping[str, Any]

    def set_config(self, config: ValueExtractor):
        url = config.get("prefix", "http://{host}/v1")
        url = url.format(host=config.get("host", "localhost:8500"))
        config = config.new_parent(
            set="put",
            format="json",
            prefix=url,
        )
        super().set_config(config)
        self._service = self.config.get("service")

    async def init(self) -> None:
        await super().init()
        if self._service is not None:
            self.context.on_start.append(self.register)
            self.context.on_stop.append(self.deregister)

    async def register(self) -> None:
        await self.set("agent/service/register", self._service)

    async def deregister(self) -> None:
        service = self._service.get("name")
        await self.set(f"agent/service/deregister/{service}", None)
