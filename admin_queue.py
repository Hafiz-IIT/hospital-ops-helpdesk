from __future__ import annotations

from dataclasses import dataclass, field
import heapq

from hospital_ops_helpdesk import HelpRequest, route


@dataclass(order=True)
class QueueItem:
    priority: int
    sequence: int
    request: HelpRequest = field(compare=False)
    routing: dict = field(compare=False)


class AdministrativeQueue:
    """Queue routine administrative requests only.

    Requests escalated as emergencies are returned immediately and are never
    converted into routine queue items.
    """

    PRIORITY = {
        "records": 1,
        "billing": 2,
        "appointment": 3,
        "facilities": 4,
    }

    def __init__(self):
        self._items: list[QueueItem] = []
        self._sequence = 0

    def submit(self, request: HelpRequest) -> dict:
        routing = route(request)
        if routing["status"] != "ROUTE":
            return routing

        self._sequence += 1
        item = QueueItem(
            self.PRIORITY.get(request.category, 10),
            self._sequence,
            request,
            routing,
        )
        heapq.heappush(self._items, item)
        return {"status": "QUEUED", "route": routing["route"]}

    def pop_next(self) -> QueueItem | None:
        return heapq.heappop(self._items) if self._items else None

    def __len__(self) -> int:
        return len(self._items)
