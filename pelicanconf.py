AUTHOR = 'andrew stewart'
SITENAME = "andrew stewart - under construction"
SITESUBTITLE = "personal site - under construction"
SITEURL = ""
GITHUB_URL = "https://github.com/ahstewart"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#PAGE_PATHS = ["pages", "projects/Astronomy"]

#DISPLAY_CATEGORIES_ON_MENU = True
#DISPLAY_PAGES_ON_MENU = False


# # Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

THEME = "../pelican-themes/bootstrap"
#PLUGINS = ["pelican_just_table"]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

from markdown.extensions.tables import TableExtension
MARKDOWN = {
    "extensions": [TableExtension()]
}
