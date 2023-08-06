"""
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  This file is part of the Smart Developer Hub Project:
    http://www.smartdeveloperhub.org
  Center for Open Middleware
        http://www.centeropenmiddleware.com/
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Copyright (C) 2015 Center for Open Middleware.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
            http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
"""

__author__ = 'Alejandro F. Carrera'

import gitlab
from settings import *
import time
import sys
from random import randint

if __name__ == '__main__':
    for arg in sys.argv:
        print arg
    print "--"
    git = gitlab.Gitlab(
        host="%s://%s:%d" % (
            GITLAB_PROT, GITLAB_IP, GITLAB_PORT
        ))
    git.login(user=GITLAB_USER, password=GITLAB_PASS)

    pag = 0
    number_page = 100
    git_users_len = -1
    git_users_em_id = {}
    while git_users_len is not 0:
        git_users = git.getusers(page=pag, per_page=number_page)
        git_users_len = len(git_users)
        [git_users_em_id.update({x.get('email'): '1'}) for x in git_users]
        pag += 1

    print "Creating Group: jenkins"
    group = git.creategroup("jenkins", "jenkins")
    time.sleep(15)
    print " - Done"

    visibility_levels = ['public', 'private', 'internal']
    projects = [
        {
            'git': "https://github.com/jenkinsci/docker-plugin.git",
            'name': 'docker-plugin',
        },
        {
            'git': "https://github.com/jenkinsci/maven-hpi-plugin.git",
            'name': 'maven-hpi-plugin',
        },
        {
            'git': "https://github.com/jenkinsci/gradle-jpi-plugin.git",
            'name': 'gradle-jpi-plugin',
        },
        {
            'git': "https://github.com/jenkinsci/docker-workflow-plugin.git",
            'name': 'docker-workflow-plugin',
        },
        {
            'git': "https://github.com/jenkinsci/github-pullrequest-plugin.git",
            'name': 'github-pullrequest-plugin',
        }
    ]

    for i in projects:
        print "Creating Project: " + i.get('name')
        v = randint(0, 2)
        if randint(0, 1) == 0:
            project = git.createproject(
                name=i.get('name'), visibility_level=visibility_levels[v], import_url=i.get('git')
            )
        else:
            project = git.createproject(
                name=i.get('name'), visibility_level=visibility_levels[v], import_url=i.get('git'), namespace_id=group.get('id')
            )
        time.sleep(45)
        git_branches = git.getbranches(project.get('id'))
        total_commits = 0
        total_users = 0
        git_commits_hash = {}
        print " - Branches: " + str(len(git_branches))
        for x in git_branches:
            pag = 0
            number_page = 10000
            git_commits_len = -1
            while git_commits_len is not 0:
                git_commits = git.getrepositorycommits(project.get('id'), x.get('name'), page=pag, per_page=number_page)
                git_commits_len = len(git_commits)
                total_commits += git_commits_len
                for w in git_commits:
                    if w.get('id') not in git_commits_hash:
                        git_commits_hash[w.get('id')] = '1'
                        if w.get('author_email') not in git_users_em_id:
                            git_users_em_id[w.get('author_email')] = '1'
                            us = w.get('author_email').split("@")[0] + "_" + str(randint(0, 5000))
                            r = git.createuser(us, us, "pass12345", w.get('author_email'))
                            time.sleep(10)
                            if r is False:
                                print "Error: " + us + ' - ' + w.get('author_email')
                            else:
                                print "Created: " + us + ' - ' + w.get('author_email')
                                total_users += 1
                pag += 1
        print " - Commits (All Branches): " + str(total_commits)
        print " - Commits (Unique): " + str(len(git_commits_hash.keys()))
        print " - New Users: " + str(total_users)
        print " - Done"
