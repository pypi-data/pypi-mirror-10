# Copyright 2015: Mirantis Inc.
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import asyncio
from concurrent import futures
import logging

from rallyci.config import Config

LOG = logging.getLogger(__name__)


class Root:
    def __init__(self, loop):
        self.tasks = {}
        self.loop = loop
        self.streams = []
        self.status_monitors = []
        self.task_start_handlers = []
        self.task_end_handlers = []
        self.job_update_handlers = []

    def start_streams(self):
        for stream in self.config.get_instances("stream"):
            self.streams.append(stream)
            stream.start(self)

    def start_status_monitors(self):
        for status in self.config.get_instances("status"):
            self.status_monitors.append(status)
            status.start(self)

    def stop_services(self, container, wait=False):
        fs = []
        for service in container:
            fs.append(service.stop())
        if wait and fs:
            asyncio.wait(*fs, return_when=futures.ALL_COMPLETED)

    def load_config(self, filename):
        self.filename = filename
        self.config = Config(filename)
        self.start_streams()
        self.start_status_monitors()

    def reload(self):
        try:
            new_config = Config(self.filename)
        except Exception:
            LOG.exception("Error loading new config")
            return
        self.config = new_config
        self.stop_services(self.streams)
        self.stop_services(self.status_monitors)
        self.start_streams()

    def task_done(self, future):
        task = self.tasks[future]
        LOG.debug("Completed task: %s" % task)
        for cb in self.task_end_handlers:
            cb(task)
        del(self.tasks[future])

    def job_updated(self, job):
        for cb in self.job_update_handlers:
            cb(job)

    def handle(self, event):
        future = asyncio.async(event.run_jobs(), loop=self.loop)
        self.tasks[future] = event
        future.add_done_callback(self.task_done)
        for cb in self.task_start_handlers:
            cb(event)

    def stop(self):
        LOG.info("Interrupted.")
        self.stop_services(self.streams, True)
        tasks = list(self.tasks.keys())
        if tasks:
            LOG.info("Waiting for tasks %r." % tasks)
            yield from asyncio.gather(*tasks, return_exceptions=True)
            LOG.info("All tasks finished.")
        self.stop_services(self.status_monitors, True)
        self.loop.stop()
