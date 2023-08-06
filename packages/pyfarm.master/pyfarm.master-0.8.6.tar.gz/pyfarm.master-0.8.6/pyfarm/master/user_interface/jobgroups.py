# No shebang line, this module is meant to be imported
#
# Copyright 2015 Ambient Entertainment GmbH & Co. KG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from httplib import BAD_REQUEST
except ImportError:  # pragma: no cover
    from http.client import BAD_REQUEST

from flask import render_template, request

from sqlalchemy import func, or_, and_, distinct, desc, asc

from pyfarm.core.enums import WorkState, AgentState

from pyfarm.master.application import db
from pyfarm.models.job import Job
from pyfarm.models.jobtype import JobType, JobTypeVersion
from pyfarm.models.task import Task
from pyfarm.models.agent import Agent
from pyfarm.models.user import User
from pyfarm.models.jobgroup import JobGroup


def jobgroups():
    agent_count_query = db.session.query(
        Job.job_group_id,
        func.count(distinct(Task.agent_id)).label('agent_count')).\
            join(Task, Task.job_id == Job.id).\
            filter(Job.job_group_id != None).\
            filter(Task.agent_id != None, or_(Task.state == None,
                                              Task.state == WorkState.RUNNING),
                   Task.agent.has(Agent.state != AgentState.OFFLINE)).\
                group_by(Job.job_group_id).subquery()
    submit_time_query = db.session.query(
        Job.job_group_id,
        func.min(Job.time_submitted).label('time_submitted')).\
            group_by(Job.job_group_id).subquery()
    jobs_queued_query = db.session.query(
        Job.job_group_id, func.count('*').label('j_queued')).\
            filter(Job.state == None).group_by(Job.job_group_id).subquery()
    jobs_paused_query = db.session.query(
        Job.job_group_id, func.count('*').label('j_paused')).\
            filter(Job.state == WorkState.PAUSED).\
                group_by(Job.job_group_id).subquery()
    jobs_running_query = db.session.query(
        Job.job_group_id, func.count('*').label('j_running')).\
            filter(Job.state == WorkState.RUNNING).\
                group_by(Job.job_group_id).subquery()
    jobs_done_query = db.session.query(
        Job.job_group_id, func.count('*').label('j_done')).\
            filter(Job.state == WorkState.DONE).\
                group_by(Job.job_group_id).subquery()
    jobs_failed_query = db.session.query(
        Job.job_group_id, func.count('*').label('j_failed')).\
            filter(Job.state == WorkState.FAILED).\
                group_by(Job.job_group_id).subquery()
    tasks_queued_query = db.session.query(
        func.count(Task.id).label("t_queued"), Job.job_group_id).\
            join(Job, Task.job_id == Job.id).\
            filter(Task.state == None).group_by(Job.job_group_id).subquery()
    tasks_running_query = db.session.query(
        func.count(Task.id).label('t_running'), Job.job_group_id).\
            join(Job, Task.job_id == Job.id).\
            filter(Task.state == WorkState.RUNNING).\
                group_by(Job.job_group_id).subquery()
    tasks_done_query = db.session.query(
        func.count(Task.id).label('t_done'), Job.job_group_id).\
            join(Job, Task.job_id == Job.id).\
            filter(Task.state == WorkState.DONE).\
                group_by(Job.job_group_id).subquery()
    tasks_failed_query = db.session.query(
        func.count(Task.id).label('t_failed'), Job.job_group_id).\
            join(Job, Task.job_id == Job.id).\
            filter(Task.state == WorkState.FAILED).\
                group_by(Job.job_group_id).subquery()
    jobgroups_query = db.session.query(JobGroup,
                                       User.username,
                                       JobType.name.label("main_jobtype_name"),
                                       func.coalesce(
                                           agent_count_query.c.agent_count,
                                           0).label("agent_count"),
                                       submit_time_query.c.time_submitted.\
                                           label("time_submitted"),
                                       func.coalesce(
                                           tasks_queued_query.c.t_queued,
                                           0).label("t_queued"),
                                       func.coalesce(
                                           tasks_running_query.c.t_running,
                                           0).label("t_running"),
                                       func.coalesce(
                                           tasks_done_query.c.t_done,
                                           0).label("t_done"),
                                       func.coalesce(
                                           tasks_failed_query.c.t_failed,
                                           0).label("t_failed")
                                       ).\
        join(JobType, JobGroup.main_jobtype_id == JobType.id).\
        outerjoin(jobs_queued_query,
                  JobGroup.id == jobs_queued_query.c.job_group_id).\
        outerjoin(jobs_paused_query,
                  JobGroup.id == jobs_paused_query.c.job_group_id).\
        outerjoin(jobs_running_query,
                  JobGroup.id == jobs_running_query.c.job_group_id).\
        outerjoin(jobs_done_query,
                  JobGroup.id == jobs_done_query.c.job_group_id).\
        outerjoin(jobs_failed_query,
                  JobGroup.id == jobs_failed_query.c.job_group_id).\
        outerjoin(tasks_queued_query,
                  JobGroup.id == tasks_queued_query.c.job_group_id).\
        outerjoin(tasks_running_query,
                  JobGroup.id == tasks_running_query.c.job_group_id).\
        outerjoin(tasks_done_query,
                  JobGroup.id == tasks_done_query.c.job_group_id).\
        outerjoin(tasks_failed_query,
                  JobGroup.id == tasks_failed_query.c.job_group_id).\
        outerjoin(User, JobGroup.user_id == User.id).\
        outerjoin(agent_count_query,
                  JobGroup.id == agent_count_query.c.job_group_id).\
        outerjoin(submit_time_query,
                  JobGroup.id == submit_time_query.c.job_group_id)

    filters = {
        "st_queued": ("st_queued" in request.args and
                       request.args["st_queued"].lower() == "true"),
        "st_paused": ("st_paused" in request.args and
                      request.args["st_paused"].lower() == "true"),
        "st_running": ("st_running" in request.args and
                       request.args["st_running"].lower() == "true"),
        "st_failed": ("st_failed" in request.args and
                      request.args["st_failed"].lower() == "true"),
        "st_any_done": ("st_any_done" in request.args and
                        request.args["st_any_done"].lower() == "true"),
        "st_all_done": ("st_all_done" in request.args and
                        request.args["st_all_done"].lower() == "true")}
    no_state_filters = True
    if (any(filters.values())):
        no_state_filters = False
        conditions = []
        if filters["st_queued"]:
            conditions.append(and_(jobs_running_query.c.j_running == None,
                                   jobs_paused_query.c.j_paused == None,
                                   jobs_done_query.c.j_done == None,
                                   jobs_failed_query.c.j_failed == None))
        if filters["st_paused"]:
            conditions.append(jobs_paused_query.c.j_paused != None)
        if filters["st_running"]:
            conditions.append(jobs_running_query.c.j_running != None)
        if filters["st_failed"]:
            conditions.append(jobs_failed_query.c.j_failed != None)
        if filters["st_any_done"]:
            conditions.append(jobs_done_query.c.j_done != None)
        if filters["st_all_done"]:
            conditions.append(and_(jobs_queued_query.c.j_queued == None,
                                   jobs_running_query.c.j_running == None,
                                   jobs_paused_query.c.j_paused == None,
                                   jobs_failed_query.c.j_failed == None))
        jobgroups_query = jobgroups_query.filter(or_(*conditions))

    filters["no_user"] = ("no_user" in request.args and
                          request.args["no_user"].lower == "true")
    if "u" in request.args or filters["no_user"]:
        user_ids = request.args.getlist("u")
        user_ids = [int(x) for x in user_ids]
        jobgroups_query = jobgroups_query.filter(JobGroup.user_id.in_(user_ids))
        filters["u"] = user_ids

    if "jt" in request.args:
        jobtype_ids = request.args.getlist("jt")
        jobtype_ids = [int(x) for x in jobtype_ids]
        jobgroups_query = jobgroups_query.filter(
            JobGroup.main_jobtype_id.in_(jobtype_ids))
        filters["jt"] = jobtype_ids

    exists_query = jobgroups_query.filter(Job.job_group_id == JobGroup.id).\
        exists()
    jobs_query = db.session.query(Job.job_group_id,
                                  Job,
                                  JobType.name.label('jobtype_name')).\
        join(JobTypeVersion, Job.jobtype_version_id == JobTypeVersion.id).\
        join(JobType, JobTypeVersion.jobtype_id == JobType.id).\
        filter(exists_query)

    jobs_by_group = {}
    for group_id, job, jobtype_name in jobs_query:
        if group_id in jobs_by_group:
            jobs_by_group[group_id].append(job)
        else:
            jobs_by_group[group_id] = [(job, jobtype_name)]

    order_dir = "desc"
    order_by = "time_submitted"
    if "order_by" in request.args:
        order_by = request.args.get("order_by")
    if order_by not in ["title", "time_submitted", "username",
                        "main_jobtype_name", "agent_count", "j_queued",
                        "j_running", "j_failed", "j_done", "t_queued",
                        "t_running", "t_failed", "t_done"]:
        return (render_template(
            "pyfarm/error.html",
            error="Unknown order key %r. Options are 'title', "
                  "'main_jobtype_name' 'time_submitted', 'username', "
                  "'agent_count', 'j_queued', 'j_running', 'j_failed', "
                  "'j_done', 't_queued', 't_running', 't_failed', 't_done'" %
                  order_by),
                BAD_REQUEST)
    if "order_dir" in request.args:
        order_dir = request.args.get("order_dir")
        if order_dir not in ["asc", "desc"]:
            return (render_template(
            "pyfarm/error.html",
            error="Unknown order direction %r. Options are 'asc' or 'desc'" %
                  order_dir),
            BAD_REQUEST)
    jobgroups_query = jobgroups_query.order_by("%s %s" % (order_by, order_dir))

    users_query = User.query.order_by(User.username)
    jobtypes_query = JobType.query

    return render_template("pyfarm/user_interface/jobgroups.html",
                           jobgroups=jobgroups_query,
                           jobs_by_group=jobs_by_group, filters=filters,
                           order_dir=order_dir, order_by=order_by,
                           users=users_query, jobtypes=jobtypes_query)
