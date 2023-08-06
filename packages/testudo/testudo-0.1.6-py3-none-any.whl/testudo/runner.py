from functools import partial
from pathlib import Path
from shlex import split
from subprocess import STDOUT, Popen, PIPE
from threading import Event
from typing import List, Optional, Generator

from typeguard import typechecked

from testudo.config import TaskConfig
from testudo.log import log
from testudo.reporter import start_reporter_daemon
from testudo.task_manager import task_manager

@typechecked
def report_failure(db: Path, task_id: str, output: str, exit_code: int, stack_trace: Optional[str] = None) -> None:
    with task_manager(db) as tm:
        tm.report_failure(task_id, output, exit_code, stack_trace)


@typechecked
def report_success(db: Path, task_id: str, output: str) -> None:
    with task_manager(db) as tm:
        tm.report_success(task_id, output)

@typechecked
class OutputWindow:
    def __init__(self, limit: Optional[int] = None) -> None:
        self.limit = limit
        self.contents: List[str] = []

    def append(self, line: str) -> None:
        self.contents.append(line)
        if self.limit is not None:
            while len(self.contents) > self.limit:
                self.contents.pop(0)

    @property
    def output(self) -> str:
        joined = '\n'.join(self.contents)
        return joined

@typechecked
def run(db: Path, task_id: str, cmd: List[str]) -> bool:
    log.info(f"Running Task [{task_id}]...")
    out = OutputWindow(30)
    with Popen(cmd, stderr=STDOUT, stdout=PIPE) as proc:
        while proc.poll() is None:
            line = []
            if proc.stdout is None:  # pragma: no branch
                break  # pragma: no cover
            for byte in iter(partial(proc.stdout.read, 1), b''):
                char = byte.decode()
                if char not in {'\n', '\r', ''}:
                    line.append(char)
                else:
                    joined = "".join(line)
                    log.info(f'[{task_id}] OUTPUT: {joined}')
                    out.append(joined.rstrip())
                    line = []
        exit_code = proc.returncode
        if exit_code == 0:
            log.info(f"Task [{task_id}] successful!")
            report_success(db, task_id, out.output)
            return True
        log.warning(f"Task [{task_id}] failed!")
        report_failure(db, task_id, '\n'.join(out.output), exit_code)
        return False

@typechecked
def run_with_delay(db: Path, task_id: str,
                   cmd: List[str],
                   delay_seconds: float,
                   halt_flag: Event,
                   on_failure_delay_seconds: Optional[float] = None) -> Generator[bool, None, None]:
    on_failure_delay_seconds = on_failure_delay_seconds or delay_seconds
    while 42:
        success = run(db, task_id, cmd)
        yield success
        if halt_flag.wait(delay_seconds if success else on_failure_delay_seconds):
            break

@typechecked
def run_with_reporter(db: Path, config: TaskConfig, halt: Optional[Event] = None) -> None:
    first_run_complete = False
    _halt = halt or Event()
    for _ in run_with_delay(db, config.task_id, split(config.command),
                            delay_seconds=config.delay_seconds, halt_flag=_halt,
                            on_failure_delay_seconds=config.on_failure_delay_seconds):
        if not first_run_complete:
            first_run_complete = True
            start_reporter_daemon(db, config, halt=_halt)
