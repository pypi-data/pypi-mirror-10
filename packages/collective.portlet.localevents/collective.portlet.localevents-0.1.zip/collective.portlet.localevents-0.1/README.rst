==============================
collective.portlet.localevents
==============================

Customization of the default event portlet (``portlets.Events``) provided by ``plone.app.portlets``
that does not search for events in the whole portal (or `INavigationRoot`) but only in
the context of the portlet.

When creating a portlet you can decide if events shall be searched in

* the context the portlet has been assigned or

* the context the portlet is shown in


Our usecase for this portlet was a section `team` with folders for different team members in it.
(no INavigationRoot can be set on those, since we don't want to limit the navigation, search, etc
just on this folder)

Each Team member can now easily add an event portlet only listing the events within his/her folder.

  

