#!/usr/bin/python

from oslo_log import log as logging
LOG = logging.getLogger(__name__)

class HookCreate (object):

    def pre(self, *args, **kwargs):
        LOG.info("start pre-start hook")

        # Object from /usr/lib/python2.7/site-packages/nova/openstack/common/context.py
        context = args[1]  # nova.context.RequestContext object
        context_dict = context.to_dict()
        user_name  = context_dict['user_name']  # who is using this service?
        project_name = context_dict['project_name'] # what project is it under?
        LOG.info(user_name)
        LOG.info(project_name)

        kwargs.get('metadata').update({
            'user_name': user_name,
            'project_name': project_name
        })

        LOG.info("end pre-start hook")

    def post(self, *args, **kwargs):
        LOG.info("start post-start hook") 
        for k, v in kwargs.items():
            LOG.info('%s %s' % (k, v))
        LOG.info("stop post-start hook")

class HookDelete (object):

    def pre(self, *args, **kwargs):
        LOG.info("start pre-destroy hook")
        for k, v in kwargs.items():
            LOG.info('%s %s' % (k, v))
        LOG.info("start pre-destroy hook")

    def post(self, *args, **kwargs):
        LOG.info("start post-destroy hook")
        for k, v in kwargs.items():
            LOG.info('%s %s' % (k, v))
        LOG.info("stop post-destroy hook")
