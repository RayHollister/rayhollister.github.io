---
layout: home
title: Blog
permalink: /blog/
---

{% for post in site.posts %}

  <div>
  
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  <a href="{{ post.url }}"><img src="{{ post.image }}"/></a>
  <div class="mv3">
      {{ post.content | strip_html | truncatewords: 50 }}
  </div>
  <a href="{{ post.url }}" class="f6 link ph3 pv2 mt2 dib white bg-black">Read more...</a>
  </div>
  <hr/>
  {% endfor %}
