===============================
Django Molder
===============================

.. image:: https://img.shields.io/pypi/v/django_molder.svg
        :target: https://pypi.python.org/pypi/django_molder


Another one painless way to working with forms and they fields

* Free software: BSD license

Features
--------

It provides multiple tags for rendering form fields in a custom template.
Bootstrap3 classes and html as default but you can simple override this for your specification -
just make ``molder`` directory in your templates folder.

Example:
--------

In your template:


.. code:: html

    {% loads molder_tags %}

    <div class="container-fluid">
        <div class="row">
            <form class="form">
                <div class="col-md-6">
                    {% render_field form_one.char_field class="+big_input" placeholder="Hello world" %}
                    {% render_field form_one.radio_field help_on_top=True %}
                    {% render_field form_one.file_field template="myapp/coolest_file_field.html" %}
                </div>
                <div class="col-md-6">
                    {% render_field form_one.multiple_select_field show_help=False required=False %}
                    {% render_field form_one.checkbox_field %}
                </div>
            </form>
        </div>
    </div>


Template tags
-------------

render_field
============

Gets the bound_field and the extra kwargs and then render it.

Special kwargs:

* show_help - show/hide field help_text
* show_label - show/hide field label
* help_on_top - show help_text on top
* template - template used for this field
* required - override field required attr for visual fake


render_form
===========

Gets form as first arg. Iterates through the fields and render them. Extra kwargs passed in each field.


render_messages
===============

Just render the messages (django.contrib.messages)
