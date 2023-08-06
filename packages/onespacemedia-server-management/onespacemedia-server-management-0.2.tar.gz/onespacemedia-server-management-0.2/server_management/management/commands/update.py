from django.conf import settings as django_settings
from django.core.management.base import BaseCommand
from fabric.api import *
from fabvenv import virtualenv

from _core import load_config

import datetime
import json
import requests
import os
import sys


class Command(BaseCommand):

    endpoint = "https://hooks.slack.com/services/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"
    channel = '#commits'
    bot_name = "Update Bot"
    bot_emoji = ":neckbeard:"
    current_commit = os.popen("git rev-parse --short HEAD").read().strip()
    remote = os.popen("git config --get remote.origin.url").read().split(':')[1].split('.')[0]

    def _bitbucket_commit_url(self, commit):
        return "<https://bitbucket.org/{}/commits/{commit}|{commit}>".format(
            self.remote,
            commit=commit,
        )

    def _bitbucket_diff_url(self, commit1, commit2):
        return "<https://bitbucket.org/{}/branches/compare/{}..{}#diff|diff>".format(
            self.remote,
            commit1,
            commit2,
        )

    def _notify_start(self):
        self.start_time = datetime.datetime.now()

        requests.post(self.endpoint, data={
            'payload': json.dumps({
                'channel': self.channel,
                'username': self.bot_name,
                'icon_emoji': self.bot_emoji,
                'attachments': [{
                    'fallback': 'Update of {} has begun.'.format(django_settings.SITE_NAME),
                    'color': '#22A7F0',
                    'fields': [
                        {
                            'title': 'Project',
                            'value': django_settings.SITE_NAME,
                            'short': True,
                        },
                        {
                            'title': 'Update status',
                            'value': 'Started',
                            'short': True,
                        },
                        {
                            'title': 'Commit hash',
                            'value': self._bitbucket_commit_url(self.current_commit),
                            'short': True,
                        },
                        {
                            'title': 'User',
                            'value': os.popen("whoami").read().strip(),
                            'short': True,
                        }
                    ]
                }]
            })
        })

    def _notify_success(self):
        self.end_time = datetime.datetime.now()

        requests.post(self.endpoint, data={
            'payload': json.dumps({
                'channel': self.channel,
                'username': self.bot_name,
                'icon_emoji': self.bot_emoji,
                'attachments': [{
                    'fallback': 'Update of {} has completed successfully.'.format(django_settings.SITE_NAME),
                    'color': 'good',
                    'fields': [
                        {
                            'title': 'Project',
                            'value': django_settings.SITE_NAME,
                            'short': True,
                        },
                        {
                            'title': 'Update status',
                            'value': 'Successful',
                            'short': True,
                        },
                        {
                            'title': 'Duration',
                            'value': '{}.{} seconds'.format(
                                (self.end_time - self.start_time).seconds,
                                str((self.end_time - self.start_time).microseconds)[:2],
                            ),
                            'short': True,
                        },
                        {
                            'title': 'Commit range',
                            'value': '{} to {} ({})'.format(
                                self._bitbucket_commit_url(self.server_commit),
                                self._bitbucket_commit_url(self.current_commit),
                                self._bitbucket_diff_url(self.current_commit, self.server_commit)
                            ),
                            'short': True,
                        }
                    ]
                }]
            })
        })

    def _notify_failed(self, message):
        requests.post(self.endpoint, data={
            'payload': json.dumps({
                'channel': self.channel,
                'username': self.bot_name,

                'icon_emoji': self.bot_emoji,
                'attachments': [{
                    'fallback': 'Update of {} has failed'.format(
                        django_settings.SITE_NAME,
                    ),
                    'color': 'danger',
                    'fields': [
                        {
                            'title': 'Project',
                            'value': django_settings.SITE_NAME,
                            'short': True,
                        },
                        {
                            'title': 'Update status',
                            'value': 'Failed',
                            'short': True,
                        },
                        {
                            'title': 'Error message',
                            'value': message,
                        }
                    ]
                }]
            })
        })

    def handle_exception(self, exctype, value, traceback):
        self._notify_failed(str(value))
        sys.__excepthook__(exctype, value, traceback)

    def handle(self, *args, **options):
        self._notify_start()

        # Load server config from project
        config = load_config()

        # Define current host from settings in server config
        env.host_string = config['remote']['server']['ip']
        env.user = 'deploy'
        env.disable_known_hosts = True
        env.reject_unknown_hosts = False

        # Make sure we can connect to the server
        with hide('output', 'running', 'warnings'):
            with settings(warn_only=True):
                if not run('whoami'):
                    print "Failed to connect to remote server"
                    self._notify_failed("Failed to connect to remote server")
                    exit()

        # Set local project path
        local_project_path = django_settings.SITE_ROOT

        # Change into the local project folder
        with hide('output', 'running', 'warnings'):
            with lcd(local_project_path):

                project_folder = local("basename $( find {} -name 'wsgi.py' -not -path '*/.venv/*' -not -path '*/venv/*' | xargs -0 -n1 dirname )".format(
                    local_project_path
                ), capture=True)

        with settings(warn_only=True):
            with cd('/var/www/{}'.format(project_folder)):
                self.server_commit = run("git rev-parse --short HEAD")

                # Check which venv we need to use.
                result = run("bash -c '[ -d venv ]'")

                if result.return_code == 0:
                    venv = '/var/www/{}/venv/'.format(project_folder)
                else:
                    venv = '/var/www/{}/.venv/'.format(project_folder)

                with virtualenv(venv):
                    with shell_env(DJANGO_SETTINGS_MODULE="{}.settings.production".format(project_folder)):
                        sudo('chown {}:webapps -R /var/www/*'.format(project_folder))
                        sudo('chmod 775 -R /var/www/'.format(project_folder))

                        run('git pull')

                        run('[[ -e requirements.txt ]] && pip install -r requirements.txt')

                        sudo('[[ -e Gulpfile.js ]] && gulp styles')

                        sudo('./manage.py collectstatic -l --noinput', user=project_folder)

                        requirements = run('pip freeze')
                        compressor = False
                        watson = False
                        for line in requirements.split('\n'):
                            if line.startswith('django-compressor'):
                                compressor = True
                            if line.startswith('django-watson'):
                                watson = True

                        if not compressor:
                            sudo('./manage.py compileassets', user=project_folder)

                        sudo('./manage.py migrate', user=project_folder)

                        if watson:
                            sudo('./manage.py buildwatson', user=project_folder)

                        sudo('supervisorctl restart {}'.format(project_folder))
                        sudo('chown {}:webapps -R /var/www/*'.format(project_folder))
                        sudo('chmod 775 -R /var/www/'.format(project_folder))

        # Register the release with Opbeat.
        if 'opbeat' in config and config['opbeat']['app_id'] and config['opbeat']['secret_token']:
            with(lcd(local_project_path)):
                local('curl https://intake.opbeat.com/api/v1/organizations/{}/apps/{}/releases/'
                      ' -H "Authorization: Bearer {}"'
                      ' -d rev=`git log -n 1 --pretty=format:%H`'
                      ' -d branch=`git rev-parse --abbrev-ref HEAD`'
                      ' -d status=completed'.format(
                          config['opbeat']['organization_id'],
                          config['opbeat']['app_id'],
                          config['opbeat']['secret_token'],
                      ))

        self._notify_success()


sys.excepthook = Command().handle_exception
