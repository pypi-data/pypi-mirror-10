# Bangoo

Bangoo is a content management system on the top of Django.

# Installation

-   Remove `django.contrib.admin` from `INSTALLED_APPS` and everything related to it (e.g.: imports in `urls.py`).

-   Add these lines to the `INSTALLED_APPS`:

    ```
    'angular',
    'crispy_forms',
    'easy_thumbnails',
    'mptt',
    'taggit',
    'bangoo.core',
    'bangoo.navigation',
    'bangoo.theming',
    'bangoo.admin',
    'bangoo.media',
    'bangoo.content',
    ```

-   Set `STATICFILES_FINDERS` to:

    ```
    STATICFILES_FINDERS = (
        'bangoo.theming.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder'
    )
    ```

-   Set `TEMPLATE_LOADERS` to:

    ```
    TEMPLATE_LOADERS = (
        'bangoo.theming.loaders.themes.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader'
    )
    ```
    
-   Set `MIDDLEWARE_CLASSES` to:

    ```
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'bangoo.theming.middleware.ThemeMiddleware',
        'bangoo.navigation.middleware.MenuResolverMiddleware'
    )
    ```
    
-   Set `TEMPLATE_CONTEXT_PROCESSORS` to:

    ```
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.core.context_processors.media',
        'django.core.context_processors.i18n',
        'bangoo.theming.context_processors.act_theme',
        'bangoo.navigation.context_processors.act_menu'
    )
    ```

-   Set `AUTH_USER_MODEL` to `core.User`

-   Set available system languages. Example:

    ```
    LANGUAGES = (
        ('en', u'English'),
        ('hu', u'Hungarian'),
    )
    ```
    
    Use [2 letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).

-   Set the theme template directory path:

    ```
    THEMES_BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'themes').replace('\\', '/')
    ```
    
    And the default theme:
    
    ```
    THEME = 'default'
    ```
    
    In the example above the `THEMES_BASE_DIR` is expected to point to the `themes` directory
    in the current working directory. `default` theme should be located in `themes/default` then.
    
-   Set `CRISPY_TEMPLATE_PACK` to `bootstrap3`. 
    (Or anything valid. See the [docs](http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs))

-   Add `admin` and `media` URLs and also append Bangoo's navigation URLs to your URL patterns:

    ```
    urlpatterns = patterns('',
        url(r'^admin/', include('bangoo.admin.urls')),
        url(r'^media/', include('bangoo.media.admin.urls'))
    ) + i18n_patterns('',
        url(r'', include('bangoo.navigation.urls')),
    )
    ```
    Don't forget to import `i18n_patterns`: `from django.conf.urls.i18n import i18n_patterns`

-   `python manage.py migrate`
-   Create the theme directory by invoking `python manage.py create-theme`


# Template blocks

Builtin and external plugins (e.g.: `bangoo.content`, `plugins.blog`) usually extend `base.html` template.
You should add `header` and `content` template blocks to this file to make these plugins work.
