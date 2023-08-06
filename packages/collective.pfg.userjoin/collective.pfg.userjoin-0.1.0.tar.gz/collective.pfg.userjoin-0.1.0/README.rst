Easily **subscribe** new user to you Plone site by using a **custom PloneFormGen join form**  

.. contents:: **Table fo contents**

Introduction
============

The scope of this add-on is to collect join request to your site without enabling the
"*Enable self-registration*" option in the security control panel.

Every join request is stored in a new PloneFormGen adapter called "**User Join Adapter**", then
site administrator or other power users can "confirm" the request (and create a new site's member)
or discard it.

Configuration
=============

PloneFormGen form
-----------------

First of all create you Form Folder with all the fields you want to use.
Not every field you use must be used as user data, for example you can required fields that will
be used by other adapters.

Fields you must include are the ones that ask for the new userid and (probably) the email.
The password field is not required (and will not be used) because the adapter will rely onto the Plone
native password reset feature.

.. image:: https://raw.githubusercontent.com/PloneGov-IT/collective.pfg.userjoin/7ade30d07f94d2e127b780eb0cf2a9cd94a7152a/docs/collective.pfg.userjoin.0.1.0-01.png
   :alt: Form filling example

**Please note** that a captcha protection is probably something you don't want to miss.
See the PloneFormGen documentation for more.

Adapter configuration
---------------------

Now create the adapter.

.. image:: https://raw.githubusercontent.com/PloneGov-IT/collective.pfg.userjoin/7ade30d07f94d2e127b780eb0cf2a9cd94a7152a/docs/collective.pfg.userjoin.0.1.0-04.png
   :alt: Adapter edit form

You must properly configure the "*Userid form field*", where you must select the form field where you plan to
ask form username.

The same must be done for "*Email form field*" and (optionally) "*Fullname form field*".

Please remember to enable the adapter in the PloneFormGen edit form.

Advanced user configuration
---------------------------

Your user configuration fieldset can be different from the Plone default, for example you can have a complex
configuration that ask for additional informations like phone number, SSN, ...

You can handle this by also filling the "*Map additional user's data*" field.
For every user properties on the right you can select which form field (on the left) must be used to populate
that user info when the user will be finally created.

Groups
------

You can configure the adapter to automatically add users to one or more groups when the join request
will be confirmed.

Manage join requests
====================

By navigate to the adapter a list of join requests is provided.

.. image:: https://raw.githubusercontent.com/PloneGov-IT/collective.pfg.userjoin/7ade30d07f94d2e127b780eb0cf2a9cd94a7152a/docs/collective.pfg.userjoin.0.1.0-02.png
   :alt: Show join requests

The table will recap all form fields that you included in the adapter configuration, showing values provided
at the form submission.
Please note that *every* form field provided is stored (you can preview all of the data by clicking on the userid link).

Then you can *confirm* join requests, that means you will create one or more new members, or discard them deleting
the data.

As said above, this product will not handle passwords so after a request is confirmed the default site reset password
feature is triggered: the user will receive the standard password reset email.

Advanced usage
==============

Integration with Email adapter
------------------------------

This product will not send any email so you probably like to use the standard PloneFormGen mailer adapter
if you need to warn power user to evaluate new submissions.
To help in this a ``@@join-detail`` view is provided.

.. image:: https://raw.githubusercontent.com/PloneGov-IT/collective.pfg.userjoin/7ade30d07f94d2e127b780eb0cf2a9cd94a7152a/docs/collective.pfg.userjoin.0.1.0-03.png
   :alt: Show/Confirm a single join request

The adapter will add two new request informations you can use in the mailer (adapter execution orders matters):

``pfguserjoin_obj``
  Adapter object
``pfguserjoin_newid``
  Record id of the request

For example you can edit the "*Mail-Body Template*" as follow::

    <html xmlns="http://www.w3.org/1999/xhtml">
    
      <head><title></title></head>
    
      <body>
        <p tal:content="here/getBody_pre | nothing" />
        <dl>
            <tal:block repeat="field options/wrappedFields | nothing">
                <dt tal:content="field/fgField/widget/label" />
                <dd tal:content="structure python:field.htmlValue(request)" />
            </tal:block>
        </dl>
        <p tal:content="here/getBody_post | nothing" />
        <pre tal:content="here/getBody_footer | nothing" />
        <p>Go to the
            <a tal:attributes="href string:${request/pfguserjoin_obj/absolute_url}/@@join-detail?id:int=${request/pfguserjoin_newid}">
                subscription confirmation page
            </a>
        </p>
      </body>
    </html>

Advanced security
-----------------

By default this add-on will limit dangerous features to Managers and Site administrators.
Please note that a badly configured adapter can open your site to security issues.

``collective.pfg.userjoin: Edit Awkward Fields``
  This permission is the one that controls who can edit problematic adapter fields
  (user configuration, groups, ...)
``collective.pfg.userjoin: Manage Join Attempts``
  This permission is the one that controls who can confirm join requests or discard them
``collective.pfg.userjoin: View Sentive Data``
  By playing with this permission you can limit people able to see submitted data.

Credits
=======

Developed with the support of `S. Anna Hospital, Ferrara`__; S. Anna Hospital supports the
`PloneGov initiative`__.

__ http://www.ospfe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
