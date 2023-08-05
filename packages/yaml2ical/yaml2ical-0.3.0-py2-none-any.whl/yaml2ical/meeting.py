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

import datetime
from io import StringIO
import os
import os.path
import yaml


from yaml2ical.recurrence import supported_recurrences


class Schedule(object):
    """A meeting schedule."""

    def __init__(self, meeting, sched_yaml):
        """Initialize schedule from yaml."""

        self.project = meeting.project
        self.filefrom = meeting.filefrom
        try:
            self.utc = sched_yaml['time']
            self.time = datetime.datetime.strptime(sched_yaml['time'], '%H%M')
            self.day = sched_yaml['day']
            self.irc = sched_yaml['irc']
            self.freq = sched_yaml['frequency']
            self.recurrence = supported_recurrences[sched_yaml['frequency']]
        except KeyError as e:
            print("Invalid YAML meeting schedule definition - missing "
                  "attribute '{0}'".format(e.args[0]))
            raise

    def conflicts(self, other):
        """Checks for conflicting schedules."""
        alternating = set(['biweekly-odd', 'biweekly-even'])
        return (
            ((self.day == other.day) and
             (abs(self.time - other.time) < datetime.timedelta(hours=1)) and
             (self.irc == other.irc)) and
            (set([self.freq, other.freq]) != alternating))


class Meeting(object):
    """An OpenStack meeting."""

    def __init__(self, data):
        """Initialize meeting from meeting yaml description."""

        yaml_obj = yaml.safe_load(data)

        try:
            self.chair = yaml_obj['chair']
            self.description = yaml_obj['description']
            self.project = yaml_obj['project']
        except KeyError as e:
            print("Invalid YAML meeting definition - missing "
                  "attribute '{0}'".format(e.args[0]))
            raise

        try:
            self.filefrom = os.path.basename(data.name)
        except AttributeError:
            self.filefrom = "stdin"

        self.schedules = []
        for sch in yaml_obj['schedule']:
            s = Schedule(self, sch)
            self.schedules.append(s)

    @classmethod
    def fromfile(cls, yaml_file):
        f = open(yaml_file, 'r')
        return cls(f)

    @classmethod
    def fromstring(cls, yaml_string):
        s = StringIO(yaml_string)
        return cls(s)


def load_meetings(yaml_source):
    """Build YAML object and load meeting data

    :param yaml_source: source data to load, which can be a directory or
                        stream.
    :returns: list of meeting objects
    """
    meetings = []
    # Determine what the yaml_source is. Files must have .yaml extension
    # to be considered valid.
    if os.path.isdir(yaml_source):
        for root, dirs, files in os.walk(yaml_source):
            for f in files:
                # Build the entire file path and append to the list of yaml
                # meetings
                if os.path.splitext(f)[1] == '.yaml':
                    yaml_file = os.path.join(root, f)
                    meetings.append(Meeting.fromfile(yaml_file))
    elif (os.path.isfile(yaml_source) and
          os.path.splitext(yaml_source)[1] == '.yaml'):
        meetings.append(Meeting.fromfile(yaml_source))
    elif isinstance(yaml_source, str):
        return [Meeting.fromstring(yaml_source)]

    if not meetings:
        # If we don't have a .yaml file, a directory of .yaml files, or any
        # YAML data fail out here.
        raise ValueError("No .yaml file, directory containing .yaml files, "
                         "or YAML data found.")
    else:
        return meetings


class MeetingConflictError(Exception):
    pass


def check_for_meeting_conflicts(meetings):
    """Check if a list of meetings have conflicts.

    :param meetings: list of Meeting objects

    """

    for i in range(len(meetings)):
        schedules = meetings[i].schedules
        for j in range(i + 1, len(meetings)):
            other_schedules = meetings[j].schedules
            for schedule in schedules:
                for other_schedule in other_schedules:
                    if schedule.conflicts(other_schedule):
                        msg_dict = {'one': schedule.filefrom,
                                    'two': other_schedule.filefrom}
                        raise MeetingConflictError(
                            "Conflict between %(one)s and %(two)s" % msg_dict)
