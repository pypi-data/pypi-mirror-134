from typing import List, Optional

from ..domain.job import Job
from ..pyzio_logger import PyzioLogger


class LocalJobRepository:
    def __init__(self, logger: PyzioLogger):
        self._logger = logger
        self._job_q: List[Job] = []

    def update_jobs(self, jobs: List[Job]) -> None:
        sorted_jobs = sorted(jobs, key=lambda j: j.sequence_number)
        self._job_q = sorted_jobs

    def peek_job_from_queue(self) -> Job:
        return self._job_q[0]

    def peek_job_by_id(self, id: str) -> Optional[Job]:
        for job in self._job_q:
            if job.job_id == id:
                return job
        return None

    def remove_job_by_id(self, id: str) -> None:
        for job in self._job_q:
            if job.job_id == id:
                self._job_q.remove(job)
                break

    def is_queue_empty(self):
        return len(self._job_q) == 0
