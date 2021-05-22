# The Higher Lower Game API

## Overview

This API provides all the data from [The Higher Lower Game](https://www.higherlowergame.com/) collected using Data Scraping.

## Design

The v1 API is essentially a dump of in-memory data structures. We know, what works great locally in memory isn't so hot over the network. 

## Items

Search Volumne count, All Data are just items. They're live under `/api/v1/resources/data/all`.

API Endpoints

API | Description
------|------------
/api/v1/resources/data/all | Dumps all the data.
/api/v1/resources/data/title/<title> | Dumps the data for particular title.
/api/v1/resources/data/searchvolume/<title> | Dumps the search volumne for particular title.
/api/v1/resources/data/higherlower/<title1>/<title2> | Returns Higher or Lower (Higher if Search results for title2 > title1 and vice versa)
  
For example, a title: http://sohamsahare123.pythonanywhere.com/api/v1/resources/data/title/ferrari

```javascript
[
  {
  "ID":1094,
  "searches":2240000,
  "title":"ferrari"
  }
]
```

For example, a search volume: http://sohamsahare123.pythonanywhere.com/api/v1/resources/data/searchvolume/ferrari

```javascript
2240000
```
  
For example, a higherlower: http://127.0.0.1:5000/api/v1/resources/data/higherlower/tesla/ferrari
  
 ```javascript
Lower
```
