Django SweetCAptcha
================
**Django SweetCaptcha form field/widget integration app.**

django-sweetcaptcha provides a form field to integrate the `sweetCaptcha <http://www.sweetcaptcha.com/>`_ service.


Installation
------------

#. Install or add ``django-sweetcaptcha`` to your Python path.

#. Add ``sweetcaptcha`` to your ``INSTALLED_APPS`` setting.

#. Register your sweetCaptcha account `here <http://www.sweetcaptcha.com/accounts/signup>`_.

#. Add ``SWEETCAPTCHA_APP_ID`` and ``SWEETCAPTCHA_APP_KEY`` settings to the project's ``settings.py`` file. These settings are provided by the previous step.

Usage
-----

Field
~~~~~
The quickest way to add sweetcaptcha to a form is to use the included ``SweetCaptchaField`` field type. A ``SweetCaptcha`` widget will be rendered with the field validating itself without any further action required from you. For example:

.. code-block:: python

    from django import forms
    from sweetcaptcha.fields import SweetCaptchaField

    class FormWithCaptcha(forms.Form):
        sweetcaptcha = SweetCaptchaField()

To allow for runtime specification of keys:

.. code-block:: python

    sweetcaptcha = SweetCaptchaField(
        app_id='your_app_id_here',
        app_key='your_key_here'
    )

If specified these parameters will be used instead the ones specified in your project settings.

Credits
-------

``client.py`` taken from `sweetcaptcha <https://pypi.python.org/pypi/sweetcaptcha>`_ by Jaime Wyant
.

Thanks to `sweetcaptcha <http://www.sweetcaptcha.com/>`_

