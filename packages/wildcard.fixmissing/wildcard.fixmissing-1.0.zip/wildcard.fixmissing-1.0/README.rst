Introduction
============

This package allows you to fix problems with missing classes
when packages do not properly uninstall.

To define which classes or interfaces need to be fixed, you need
to specify them as environment variables in your buildout file.

The format for replacement classes is `MISSING_<Class Name> <module name>`

For instance::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    environment-vars =
        MISSING_ICatalog zc.relation.interfaces
        MISSING_IQueue collective.pdfpeek.async
        MISSING_Queue collective.pdfpeek.async
        MISSING_IPDFpeekLayer collective.pdfpeek.browser.interfaces
    ...


You can also define a replacement module to use instead of having
wildcard.fixmissing automatically create it for you.

Example::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    environment-vars =
        MISSING_ICatalog zc.relation.interfaces=my.module.interfaces
    ...
