mama-survey
===========

|travis|_ |coveralls|_

.. |travis| image:: https://travis-ci.org/praekelt/mama-survey.png?branch=develop
.. _travis: https://travis-ci.org/praekelt/mama-survey

.. |coveralls| image:: https://coveralls.io/repos/praekelt/mama-survey/badge.png?branch=develop
.. _coveralls: https://coveralls.io/r/praekelt/mama-survey

mama-survey provides a simple multiple-choice question-only survey capability
for the askMAMA mobi site.

Administrators can create questionnaires in the admin site, and view and export
answers sheets.

The first available questionnaire will only be showed to users on their 2nd
login. A link will also be displayed at the bottom of the home page.

Users can choose to complete the questionnaire immediately, later, or decline
to participate.  Decline will apply to all future questionnaires as well.

Users can bail out of a questionnaire halfway, and resume it later.

Statistics about completed, aborted and declined questionnaires will be sent to
the apporpriate holodeck metrics tracker on a regular basis.


Dependencies
------------

- django-userprofile


Usage
-----

For production, install the application in the askMAMA site with::

    python setup.py install

For development, install the application in the askMAMA development site with::

    python setup.py develop

Settings
++++++++

The following settings must be added to settings.py::

    TEMPLATE_DIRS += (
        os.path.join(PATH, "survey", "templates", "mobi"),
    )

    INSTALLED_APPS += (
        'survey',
    )

    LOGIN_REDIRECT_URL = '/survey/check-for-survey/'

    HOLODECK_URL = 'http://localhost:8001/'
