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
    <h2 id="#{{ tag_name | slugize }}">#{{ tag_name }}</h2>
    <a name="{{ tag_name | slugize }}"></a>
    {% for post in site.tags[tag] %}
    <article class="archive-item">
      <p><a href="{{ root_url }}{{ post.url }}">{{post.title}}</a></p>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>