# -*- coding: utf-8 -*-
from logging import getLogger

from cms.management.commands.subcommands.base import SubcommandsCommand
from cms.models import CMSPlugin, Title
from cms.models.pagemodel import Page
from django.core.management.base import NoArgsCommand


log = getLogger('cms.management.moderator')

class ModeratorOnCommand(NoArgsCommand):
    help = 'Turn moderation on, run AFTER upgrading to 2.4'

    def handle_noargs(self, **options):
        """
        Ensure that the public pages look the same as their draft versions.
        This is done by checking the content of the public pages, and reverting
        the draft version to look the same.

        The second stage is to go through the draft pages and publish the ones
        marked as published.

        The end result should be that the public pages and their draft versions
        have the same plugins listed. If both versions exist and have content,
        the public page has precedence. Otherwise, the draft version is used.
        """
        log.info('Reverting drafts to public versions')
        for page in Page.objects.public():
            for language in page.get_languages():
                if CMSPlugin.objects.filter(placeholder__page=page, language=language).exists():
                    log.debug('Reverting page pk=%d' % (page.pk,))
                    page.publisher_draft.revert(language)

        log.info('Publishing all published drafts')
        for title in Title.objects.filter(publisher_is_draft=True, publisher_public_id__gt=0):
            try:
                title.page.publish(title.language)
                log.debug('Published page pk=%d in %s' % (page.pk, title.language))
            except Exception:
                log.exception('Error publishing page pk=%d in %s' % (page.pk, title.language))


class ModeratorCommand(SubcommandsCommand):
    help = 'Moderator utilities'
    subcommands = {
        'on': ModeratorOnCommand,
    }
