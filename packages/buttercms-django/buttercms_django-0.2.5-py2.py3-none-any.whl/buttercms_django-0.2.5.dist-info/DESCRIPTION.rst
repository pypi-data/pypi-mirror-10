Butter CMS for Django
=========================

https://www.buttercms.com

**Why Butter?**

Butter makes setting up a company blog on Django insanely easy. It's built for Django developers to save us from hosting, DB setup, themeing, maintaining yet another Wordpress install. It's designed to be quickly integrated to an existing Django project.

Butter provides a marketing friendly blogging UI, hosted on buttercms.com, and exposes blog content created via an API.

This package provides thin wrapper that interacts with the Butter API and a quick start blog application.


Setup
-----
Requires Python 2.7.9 or newer. If you're on an older version of 2.7 please take a few seconds to upgrade: https://www.python.org/downloads/

.. code:: bash

    $ pip install buttercms-django


.. code:: python

    # In settings.py
    # Add buttercms to INSTALLED_APPS
    INSTALLED_APPS = (
        ...
        'buttercms-django',
    )

Grab your API token from https://buttercms.com/api_token

.. code:: python

    # In settings.py
    # Add your BUTTER_CMS_TOKEN
    BUTTER_CMS_TOKEN = '<your_api_token>'

Define your blog path

.. code:: python

    # In urls.py
    # Add your new blog path
    urlpatterns = patterns('',
        ...
        url(r'^blog/', include('buttercms.urls')),
    )


Nice job. You've now got a blog running natively in your Django project. Nothing but Python goodness. (No PHP scripts here ;))

Check it out! http://localhost:8000/blog


Customize the Blog Template
---------------------------
We've provided a default theme but we expect you'll want skin it with your branding so we've made this as simple as extending your base template.

First create a template file called blog.html that both extends your base template and your main content block.

.. code:: html

    {% extends "base.html" %}

    {% block content %}
        {% for post in recent_posts %}
        <div>
            <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
            <p>Posted by <a href="{% url 'blog_author' post.author.slug %}">{{ post.author.first_name }} {{ post.author.last_name }}</a> on {{ post.created }}</p>
            <p>{{ post.summary }}</p>
        </div>
        {% endfor %}
    {% endblock %}

Then add this template name to your settings.py:

.. code:: python

    # In settings.py
    BUTTER_CMS_BLOG_TEMPLATE = 'blog.html'

Go to http://localhost:8000/blog and you'll see your new professional branded blog!

If you don't make sure you're both extending the correct base template (the example assumes "base.html") and implementing the correct block name (the example assumes {% block content %} is the name of your main body block between the header and footer).

Log into https://buttercms.com/ to start blogging!

Customize the Blog Post Template
--------------------------------
Now that you've customized the Blog template, you can also do the same for the individual blog post template in the same fashion.

.. code:: html

    <!-- note it's important this template extends the variable name 'base_template' -->
    {% extends base_template %}

    {% block content %}
    <div class="post-preview">
        <a href="{% url 'blog_post' post.slug %}">
          <h2 class="post-title">
              {{ post.title }}
          </h2>
        </a>
        <p class="post-meta">Posted by <a href="{% url 'blog_author' post.author.slug %}">{{ post.author.first_name }} {{ post.author.last_name }}</a> on {{ post.created }}</p>
        <p class="post-subtitle">{{ post.body }}</p>
    </div>
    {% endblock %}

Then add this template name to your settings.py:

.. code:: python

    # In settings.py
    BUTTER_CMS_BLOG_POST_TEMPLATE = 'blog_post.html'



