Roboto Notebook
===============

A [Mezzanine](http://mezzanine.jupo.org/) theme intended for publishing a personal blog with a
minimalist design typeset with Google’s [Roboto](https://www.google.com/fonts/specimen/Roboto) typeface.

In initial development.

Installation
------------

1.  Install the Roboto Notebook theme from the Python Package Index
    (PyPI): `pip install robotonotebook`.
2.  Add `"robotonotebook",` to the top of the list of `INSTALLED_APPS` in your
    Mezannine project’s `settings.py`.
3.  Add the following settings to your project’s `settings.py`:

        INLINE_EDITING_ENABLED = False
        
        PAGE_MENU_TEMPLATES = ((1, 'Sidebar', 'pages/menus/tree.html'),
        (2, 'Footer', 'pages/menus/footer.html'),)
        
        PAGE_MENU_TEMPLATES_DEFAULT = '1'

Things To Do
------------

-   Remove hardcoded links to editing in admin and find out why admin
    link doesn’t lead to pages’ editing interface, while it works for
    the blog.
-   Finalize styling of all pages, including Mezzanine accounts, forms
    and galleries.
-   Fix image max-width.
-   Custom blog archive.
-   Fixtures for initial example blog post, about page and footer page.
-   Code syntax highlighting.
-   Print stylesheet.

Future Features That Would Be Nice
----------------------------------

-   Drag and drop images into library upload area on sidebar, and then
    onto post.
-   Option for static generation under tools?
    -   Deployment.
    -   Download backup of all pages in zipped HTML archive including
        styles and Markdown text file duplicates, i.e. `About.html`,
        `About.md`
    -   Built-in [Pandoc](http://pandoc.org/) converter in admin interface.
-   Markdown editor with toggleable preview as default for creating
    pages and posts, possibly using HTML [Content Editable](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_Editable).
