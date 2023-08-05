============
Mail Mangler
============

A simple Django app providing template tags that attempt to obfuscate raw
e-mail addresses to make them ever so slightly more difficult to scrape.

To be less-obtrusive, JavaScript is used to translate mangled source into a
normal e-mail address. If JavaScript is not present, the reCAPTCHA mailhide
service is offered to deobfuscate the addresses.

Using images, LTR-RTL hacks, or forcing reCAPTCHA access might be better at
keeping your address safe from bots, but it's annoying for legitimate users.
By using JavaScript, hopefully we can thwart some of the dumbest bots into
farming someone else's email address without much of a usability hit.

Quick start
-----------

1. In your Django's settings:

  * Add ``'mailmangler'`` to your ``INSTALLED_APPS``.

  * Add ``MAILMANGLE_PUBLIC`` and ``MAILMANGLE_SECRET``,
    with keys from the reCAPTCHA Mailhide API:
    <http://www.google.com/recaptcha/mailhide/apikey>, e.g. ::

      MAILMANGLE_PUBLIC = 'your-key...=='
      MAILMANGLE_SECRET = '123789...abcd'

2. Load the tag library with ``{% load mailmangler %}``

3. In the ``<head>`` of your template, add ``{% mailmangle_js %}``

4. Pipe (filter) email addresses through ``mailmangle`` or
   ``mailmangle_linked``, e.g. ::

    {{ my_email_var|mailmangle }}
    {{ "alice@example.com"|mailmangle }}
    {{ "bob@example.net"|mailmangle_linked }}

   will produce:

   1. A JS obfuscated, unlinked string of whatever ``my_email_var`` was.
   2. A JS obfuscated, unlinked string of "alice@example.com"
   3. A JS obfuscated, string with mailto link of "bob@example.com"

   If JS is not present, a reCAPTCHA mailhide link is available in
   ``<noscript>`` tags.


