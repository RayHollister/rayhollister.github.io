---
id: 879
title: 'A Javascript bookmarklet to open PDFs in Chrome without the toolbar'
date: '2021-10-10T17:20:06-04:00'
author: 'Ray Hollister'
layout: post
guid: 'https://rayhollister.com/?p=879'
permalink: /2021/10/10/a-javascript-bookmarklet-to-open-pdfs-in-chrome-without-the-toolbar/
categories:
    - 'Personal Blog'
    - 'Web Development'
---

Every time I start working on designing a new website, I spend about 15 minutes searching the inter-webs looking for how to open a PDF in chrome without the annoying toolbar at the top of the page.

The reason why is, of course, I need to open the PDF that the designer sent me in the same browser as I am currently working in so that I have something to compare against.

I know all you have to do is put “toolbar=0” at the end of the URL and reload the page, but by the time I start working on a new site, I have completely forgotten how to do it.

I finally decided to take the time to automate this process as a JavaScript bookmarklet.

I wish Google would just put a button on the toolbar to make it go away, but until they do, here’s a decent solution:

```javascript
javascript: (function () { notoolbar = '#toolbar=0'; window.open(location + notoolbar)})()
```

Here’s what to do if you don’t know [how to install a bookmarklet](https://mreidsma.github.io/bookmarklets/installing.html).