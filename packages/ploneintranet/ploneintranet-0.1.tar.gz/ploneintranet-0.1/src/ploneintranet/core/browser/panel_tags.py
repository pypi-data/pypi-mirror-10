# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from ploneintranet.core.integration import PLONEINTRANET


class Tags(BrowserView):

    index = ViewPageTemplateFile('panel_tags.pt')
    selected_tags = []

    def tags(self):
        """ Get available tags, both from Plone's keyword index
            and the microblog utility

        Applies very basic text searching
        """
        catalog = api.portal.get_tool('portal_catalog')
        tags = set(catalog.uniqueValuesFor('Subject'))

        # TODO: Check if the user is actually allowed to view these tags
        tool = PLONEINTRANET.microblog
        if tool:
            tags.update(tool._tag_mapping.keys())

        search_string = self.request.form.get('tagsearch')
        self.selected_tags = [
            safe_unicode(tag) for tag in self.request.form.get('tags', [])]
        tags.update(self.selected_tags)
        tags = sorted(tags)
        if search_string:
            search_string = safe_unicode(search_string)
            lower_search_string = search_string.lower()
            tags = filter(lambda x: lower_search_string in x.lower(),
                          tags)
            if search_string not in tags:
                # add searched string as first item in list
                # if it doesn't exist
                tags = [search_string] + tags

        return tags
