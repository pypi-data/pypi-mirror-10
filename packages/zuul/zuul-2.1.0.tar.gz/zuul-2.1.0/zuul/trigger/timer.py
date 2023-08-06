# Copyright 2012 Hewlett-Packard Development Company, L.P.
# Copyright 2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import apscheduler.scheduler
import logging
from zuul.model import TriggerEvent


class Timer(object):
    name = 'timer'
    log = logging.getLogger("zuul.Timer")

    def __init__(self, config, sched):
        self.sched = sched
        self.config = config
        self.apsched = apscheduler.scheduler.Scheduler()
        self.apsched.start()

    def _onTrigger(self, pipeline_name, timespec):
        for project in self.sched.layout.projects.values():
            event = TriggerEvent()
            event.type = 'timer'
            event.timespec = timespec
            event.forced_pipeline = pipeline_name
            event.project_name = project.name
            self.log.debug("Adding event %s" % event)
            self.sched.addEvent(event)

    def stop(self):
        self.apsched.shutdown()

    def isMerged(self, change, head=None):
        raise Exception("Timer trigger does not support checking if "
                        "a change is merged.")

    def canMerge(self, change, allow_needs):
        raise Exception("Timer trigger does not support checking if "
                        "a change can merge.")

    def maintainCache(self, relevant):
        return

    def postConfig(self):
        for job in self.apsched.get_jobs():
            self.apsched.unschedule_job(job)
        for pipeline in self.sched.layout.pipelines.values():
            for ef in pipeline.manager.event_filters:
                if ef.trigger != self:
                    continue
                for timespec in ef.timespecs:
                    parts = timespec.split()
                    if len(parts) < 5 or len(parts) > 6:
                        self.log.error(
                            "Unable to parse time value '%s' "
                            "defined in pipeline %s" % (
                                timespec,
                                pipeline.name))
                        continue
                    minute, hour, dom, month, dow = parts[:5]
                    if len(parts) > 5:
                        second = parts[5]
                    else:
                        second = None
                    self.apsched.add_cron_job(self._onTrigger,
                                              day=dom,
                                              day_of_week=dow,
                                              hour=hour,
                                              minute=minute,
                                              second=second,
                                              args=(pipeline.name,
                                                    timespec,))

    def getChange(self, event, project):
        raise Exception("Timer trigger does not support changes.")

    def getGitUrl(self, project):
        raise Exception("Timer trigger does not support changes.")

    def getGitwebUrl(self, project, sha=None):
        raise Exception("Timer trigger does not support changes.")
