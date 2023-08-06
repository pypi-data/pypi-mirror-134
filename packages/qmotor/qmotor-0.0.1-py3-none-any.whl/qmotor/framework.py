from abc import ABC, abstractmethod
import asyncio
from collections import namedtuple
import json
from typing import List, Tuple, overload
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.util import _Undefined
from .robot.ws import WSRoBot, WSCtx, WebSocketConn

undefined = _Undefined()

ScheduleJobArgs = namedtuple(
    "ScheduleJobArgs",
    [
        "trigger",
        "args",
        "kwargs",
        "id",
        "name",
        "misfire_grace_time",
        "coalesce",
        "max_instances",
        "next_run_time",
        "jobstore",
        "executor",
        "trigger_args",
    ],
)


class RobotScheduler(AsyncIOScheduler):
    def __init__(self, gconfig=..., **options):
        super(RobotScheduler, self).__init__(gconfig=gconfig, **options)

    def register(self, jobs):
        if len(jobs) > 0:
            for j in jobs:
                func = j[0]
                args: ScheduleJobArgs = j[1]
                self.scheduler.add_job(
                    func,
                    trigger=args.trigger,
                    args=args.args,
                    kwargs=args.kwargs,
                    id=args.id,
                    name=args.name,
                    misfire_grace_time=args.misfire_grace_time,
                    coalesce=args.coalesce,
                    max_instances=args.max_instances,
                    next_run_time=args.next_run_time,
                    jobstore=args.jobstore,
                    executor=args.executor,
                    replace_existing=True,
                    **args.trigger_args
                )

    @overload
    def start(self, jobs=None):
        if jobs:
            self.register(jobs)
        return super().start()


class Handler(ABC):
    @abstractmethod
    def couldHandle(self, ctx):
        pass

    @abstractmethod
    async def handle(self, ctx):
        pass


class FunctionalHandler(Handler):
    def __init__(self, matcher, func) -> None:
        self.matcher = matcher
        self.func = func

    def couldHandle(self, ctx):
        return self.matcher.match(ctx)

    async def handle(self, ctx):
        return await self.func(ctx)


class QBot:
    handlers: List[Handler]
    jobs: List[Tuple]
    scheduler: RobotScheduler
    ws_bot: WSRoBot

    def __init__(
        self,
        ws_url=None,
        robot_qq=None,
        verify_key=None,
        channel="all",
        ws_bot=None,
        scheduler=None,
    ) -> None:
        self.handlers = []
        self.jobs = []
        self.scheduler = scheduler or RobotScheduler()
        self.ws_bot = ws_bot or WSRoBot(ws_url, robot_qq, verify_key, channel)

    def handler(self, cls, **kwargs):
        matcher = cls(**kwargs)

        def h_func_wrapper(func):
            self.handlers.append(FunctionalHandler(matcher, func))
            return func

        return h_func_wrapper

    def scheduled_job(
        self,
        trigger,
        args=None,
        kwargs=None,
        id=None,
        name=None,
        misfire_grace_time=undefined,
        coalesce=undefined,
        max_instances=undefined,
        next_run_time=undefined,
        jobstore="default",
        executor="default",
        **trigger_args
    ):
        def s_func_wrapper(func):
            self.jobs.append(
                (
                    func,
                    ScheduleJobArgs(
                        trigger,
                        args,
                        kwargs,
                        id,
                        name,
                        misfire_grace_time,
                        coalesce,
                        max_instances,
                        next_run_time,
                        jobstore,
                        executor,
                        trigger_args,
                    ),
                )
            )
            return func

        return s_func_wrapper

    def register_handler(self, handler):
        self.handlers.append(handler)

    def register_job(self, job):
        self.jobs.append(job)

    async def listen(self):
        async with self.ws_bot as conn:
            data = json.loads((await conn.receive()).data)
            session = data["data"]["session"]
            conn = WebSocketConn(conn, session)
            while True:
                msg = json.loads((await conn.receive()).data)
                if msg.get("data", None):
                    ctx = WSCtx(self, self.robot_qq, conn, session, msg["data"])
                    for h in self.handlers:
                        if h.couldHandle(ctx):
                            await h.handle(ctx)
                            break

    def run(self, loop=None):
        loop = loop or asyncio.get_event_loop()
        self.scheduler.start(self.jobs)
        loop.create_task(self.listen())
        loop.run_forever()
