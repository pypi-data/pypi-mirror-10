# -*- coding: utf-8 -*-
import logging
from django.db import transaction
from client import NfsaasClient
from models import EnvironmentAttr, PlanAttr, HostAttr
from time import sleep

LOG = logging.getLogger(__name__)


class NfsaasProvider(object):

    @classmethod
    def get_credentials(self, environment):
        LOG.info("Getting credentials...")
        from dbaas_credentials.credential import Credential
        from dbaas_credentials.models import CredentialType
        integration = CredentialType.objects.get(type=CredentialType.NFSAAS)

        return Credential.get_credentials(environment=environment, integration=integration)

    @classmethod
    def auth(self, environment, base_url=None):
        LOG.info("Conecting with nfsaas...")
        credentials = self.get_credentials(environment=environment)

        base_url = base_url or credentials.endpoint

        return NfsaasClient(baseurl=base_url,
                            teamid=credentials.team,
                            projectid=credentials.project,
                            username=credentials.user,
                            password=credentials.password)

    @classmethod
    @transaction.commit_on_success
    def grant_access(self, environment, plan, host, export_id):

        LOG.info("Creating access!")

        nfsaas = self.auth(environment=environment)
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment

        access = nfsaas.create_access(environmentid=nfsaas_environmentid,
                                      sizeid=nfsaas_planid,
                                      exportid=export_id,
                                      host=host.address)

        LOG.info("Access created: %s" % access)

    @classmethod
    @transaction.commit_on_success
    def revoke_access(self, environment, plan, host, export_id):

        LOG.info("Removing access on export (id=%s) from host %s" % (export_id, host))
        nfsaas = self.auth(environment=environment)
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan

        accesses = nfsaas.list_access(environmentid=nfsaas_environmentid,
                                      sizeid=nfsaas_planid,
                                      exportid=export_id)

        for access in accesses:
            host_nfs = access["hosts"]
            host_network = nfsaas.change_ip(host.address)
            if host_nfs == host_network:
                LOG.info("Removing access on export (id=%s) from host %s" % (export_id, host))
                nfsaas.drop_access(environmentid=nfsaas_environmentid,
                                   sizeid=nfsaas_planid,
                                   exportid=export_id,
                                   accessid=access['id'])
                LOG.info("Access deleted: %s" % access)
                break

    @classmethod
    @transaction.commit_on_success
    def create_disk(self, environment, plan, host):

        nfsaas = self.auth(environment=environment)
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment

        LOG.info("Creating export on environmen %s and size %s" % (nfsaas_environmentid, nfsaas_planid))
        export = nfsaas.create_export(environmentid=nfsaas_environmentid, sizeid=nfsaas_planid)
        LOG.info("Export created: %s" % export)

        self.grant_access(environment, plan, host, export['id'])

        LOG.info("Saving export info on nfsaas host attr")
        hostattr = HostAttr(host=host, nfsaas_export_id=export['id'], nfsaas_path=export['path'])
        hostattr.save()

        return export

    @classmethod
    @transaction.commit_on_success
    def destroy_disk(self, environment, plan, host):

        if not HostAttr.objects.filter(host=host).exists():
            LOG.info("There is no HostAttr for this host %s. It may be an arbiter." % (host))
            return True

        nfsaas = self.auth(environment=environment)
        deleted_exports = []

        hostattrs = HostAttr.objects.filter(host=host)

        for hostattr in hostattrs:
            export_id = hostattr.nfsaas_export_id
            nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
            nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan

            accesses = nfsaas.list_access(environmentid=nfsaas_environmentid,
                                          sizeid=nfsaas_planid,
                                          exportid=export_id)

            for access in accesses:
                LOG.info("Removing access on export (id=%s) from host %s" % (export_id, host))
                nfsaas.drop_access(environmentid=nfsaas_environmentid,
                                   sizeid=nfsaas_planid,
                                   exportid=export_id,
                                   accessid=access['id'])
                LOG.info("Access deleted: %s" % access)

            LOG.info("Deleting register from nfsaas host attr")
            hostattr.delete()

            try:
                LOG.info("Env: %s, size: %s, export: %s" % (nfsaas_environmentid,
                         nfsaas_planid, export_id))
                deleted_export = nfsaas.drop_export(environmentid=nfsaas_environmentid,
                                                    sizeid=nfsaas_planid,
                                                    exportid=export_id)
                LOG.info("Export deleted: %s" % deleted_export)
                deleted_exports.append(deleted_export)
            except Exception, e:
                print e
                return None

        return deleted_exports

    @classmethod
    def create_snapshot(self, environment, plan, host):
        nfsaas = self.auth(environment=environment)

        hostattr = HostAttr.objects.get(host=host, is_active=True)
        export_id = hostattr.nfsaas_export_id
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan

        snapshot = nfsaas.create_snapshot(environmentid=nfsaas_environmentid,
                                          sizeid=nfsaas_planid,
                                          exportid=export_id)

        return snapshot

    @classmethod
    def remove_snapshot(self, environment, plan, host_attr, snapshot_id):
        export_id = hostattr.nfsaas_export_id
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan
        nfsaas = self.auth(environment=environment)
        nfsaas.drop_snapshot(environmentid=nfsaas_environmentid,
                             sizeid=nfsaas_planid,
                             exportid=export_id,
                             snapshotid=snapshot_id)

    @classmethod
    def restore_snapshot(self, environment, plan, export_id, snapshot_id):
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan
        base_url = self.get_credentials(environment=environment).get_parameter_by_name('new_api_url')
        nfsaas = self.auth(environment=environment, base_url=base_url)
        return nfsaas.restore_snapshot(environmentid=nfsaas_environmentid,
                                       sizeid=nfsaas_planid, exportid=export_id,
                                       snapshotid=snapshot_id)

    @classmethod
    def check_restore_nfsaas_job(self, environment, job_id,
                                 expected_status='finished', retries=50,
                                 interval=30):

        base_url = self.get_credentials(environment=environment).get_parameter_by_name('new_api_url')
        nfsaas = self.auth(environment=environment, base_url=base_url)
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment

        for attempt in range(retries):
            result = nfsaas.get_restore_job(base_url=base_url,
                                            environmentid=nfsaas_environmentid,
                                            job_id=job_id)

            if result.get('status') == expected_status:
                return result

            sleep(interval)

    @classmethod
    def drop_export(self, environment, plan, export_id):
        nfsaas = self.auth(environment=environment)
        nfsaas_planid = PlanAttr.objects.get(dbaas_plan=plan).nfsaas_plan
        nfsaas_environmentid = EnvironmentAttr.objects.get(dbaas_environment=environment).nfsaas_environment
        deleted_export = nfsaas.drop_export(environmentid=nfsaas_environmentid,
                                            sizeid=nfsaas_planid,
                                            exportid=export_id)
        LOG.info("Export deleted: %s" % deleted_export)

        return deleted_export
