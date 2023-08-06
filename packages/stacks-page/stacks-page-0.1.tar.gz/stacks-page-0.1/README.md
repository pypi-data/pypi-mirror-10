# stacks-page

A Stacks application for generating static HTML pages. Stacks is an in-development, open-source initiative of WGBH (http://www.wgbh.org/)

## Dependencies

* `django-versatileimagefield` >= 1.0.2
* `django-textplusstuff` >= 0.4

## Required Settings

### `STACKSPAGE_STATIC_PUBLISH_SERVERS`

Used to define servers where pages can be published to.

```
STACKSPAGE_STATIC_PUBLISH_SERVERS = {
    'staging': {
        'server': 'user@staging_server',
        'webroot_folder': '/absolute/path/to/webroot/on/server',
        'base_url': 'http://staging.somesite.com'
    },
    'production': {
        'server': 'user@prod_server',
        'webroot_folder': '/absolute/path/to/webroot/on/server',
        'base_url': 'http://www.somesite.com'
    }
}
```

TODO: Document 'path_processor'!

### `STACKSPAGE_BUILD_DIRECTORY`

A path on local disc where statically generated StacksPage instances
should be saved-to.

```
STACKSPAGE_BUILD_DIRECTORY = '/path/to/folder'
```

For local development, you'll probably want to set this dynamically. The following code will create a directory named `stackspage_build` at the same level as your project's settings file:

```
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)
STACKSPAGE_BUILD_DIRECTORY = os.path.join(BASE_DIR, 'stackspage_build')
```

### `STACKSPAGE_URL_PREFIX`

The path your Stacks application is running from, defaults to '/'.
