# Django CMS Contact

A contact system for Django CMS.

This aplication provide an apphook and a form plugin to allow users to send a contact message.

**WARNING**: I created this to use in a personal website and future versions will have hard changes that will break backward compatibility.

## Table of contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Usage](#usage)
- [Settings](#settings)
- [Templates](#templates)
- [Todo](#todo)
- [License](#license)

## Requirements

* Django 1.7
* Django CMS 3.x

## Quick start

##### 1. Install djangocms-contact:

```
pip install djangocms-contact
```

This will install the dependencies automatically.

##### 2. Add "djangocms_contact" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = (
    ...
    'cms',
    'djangocms_contact',  # You **must** add 'djangocms_contact' **after** 'cms'.
    ...
)
```

##### 3. Migrate to create the application models:

```
python manage.py migrate
```

## Usage

#### Apphook

You need to use [apphooks](http://docs.django-cms.org/en/3.1.2/how_to/apphooks.html) to integrate the application with Django CMS:

* Create a new Django CMS page
* Go to Advanced Settings and select `Contact` under "Application"
* Restart the project instance to properly load urls

You can access the application via the URL `SELECTED_PAGE_URL/contact/`. This consists of a page with a contact form and a page for success message.

#### Plugin

The form plugin will be available in the CMS frontend ready for use without any additional configuration, but requires the apphook instance. You can put the plugin in any [placeholder](http://docs.django-cms.org/en/3.1.2/introduction/templates_placeholders.html).

## Settings

You can receive a email notification when a user sends a message. This is optional and disabled by default.

First you must configure the email for [Django](<https://docs.djangoproject.com/en/1.7/topics/email/>):

```python
# This provides a email backend in console mode for testing and it must be
# modified to use in production.
# See <https://docs.djangoproject.com/en/1.7/topics/email/> for more info.
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Then provide the server email address to send notifications and the external email to receive it.

```python
# Server email, to send a notification to your personal email each time a user
# sends a message using the contact form.
NOTIFICATIONS_FROM_EMAIL = 'example@domain.com'

# Your personal email where you will receive notifications.
NOTIFICATIONS_TO_EMAIL = 'example@gmail.com'
```

## Templates

A `djangocms_contact/base.html` template is used for all the application templates. The templates extends a `base.html` template and the content is put in a `contact_content` block. You can override the templates to fit your needs creating a `djangocms_contact` directory in your template directory.

## Todo

* Refactor to allow creating individual and configurable forms.
* Add antispam protections.
* Write more tests.
* Add support for Django 1.8.
* Translate to more languages.

## License

Released under the MIT license.
