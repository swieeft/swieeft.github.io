---
layout: page
title: "TAGS"
subtitle:
background: /assets/headerBackground.png
permalink: /tags/
---

<div id="archives">
{% for tag in site.data.tags %}
  <div class="archive-group">
    {% capture tag_name %}{{ site.data.format[tag] }}{% endcapture %}
    <a name="{{ tag_name | slugize }}"></a>
    <h2 id="#{{ tag_name | slugize }}">#{{ tag_name }}</h2>
    {% for post in site.tags[tag] %}
    <article class="archive-item">
      <p><a href="{{ root_url }}{{ post.url }}">{{post.title}}</a></p>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>