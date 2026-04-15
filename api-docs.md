---
title: Music Appreciation and Discovery API v0.2.0
language_tabs:
  - python: Python
  - javascript: Node.js
language_clients:
  - python: ""
  - javascript: ""
toc_footers: []
includes: []
search: false
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="music-appreciation-and-discovery-api">Music Appreciation and Discovery API v0.2.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

A coursework API for track exploration, reviews, tags, collections, and simple analytics. Built with FastAPI, SQLAlchemy, and SQLite.

<h1 id="music-appreciation-and-discovery-api-general">General</h1>

## Root

<a id="opIdroot__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /`

Return a welcome message with links to documentation.

> Example responses

> 200 Response

```json
{}
```

<h3 id="root-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="root-responseschema">Response Schema</h3>

Status Code **200**

*Response Root  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## Health

<a id="opIdhealth_health_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/health', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/health',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /health`

Return a simple health-check response.

> Example responses

> 200 Response

```json
{}
```

<h3 id="health-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="health-responseschema">Response Schema</h3>

Status Code **200**

*Response Health Health Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-genres">Genres</h1>

## List Genres

<a id="opIdlist_genres_genres_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/genres', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/genres',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /genres`

Return all genres ordered alphabetically.

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string"
  }
]
```

<h3 id="list-genres-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="list-genres-responseschema">Response Schema</h3>

Status Code **200**

*Response List Genres Genres Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Genres Genres Get|[[GenreRead](#schemagenreread)]|false|none|[Schema for genre responses.]|
|» GenreRead|[GenreRead](#schemagenreread)|false|none|Schema for genre responses.|
|»» id|integer|true|none|none|
|»» name|string|true|none|none|
|»» description|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Genre

<a id="opIdget_genre_genres__genre_id__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/genres/{genre_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/genres/{genre_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /genres/{genre_id}`

Return a single genre by its ID.

<h3 id="get-genre-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|genre_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string"
}
```

<h3 id="get-genre-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[GenreRead](#schemagenreread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-tracks">Tracks</h1>

## List Tracks

<a id="opIdlist_tracks_tracks_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/tracks', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/tracks',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /tracks`

List tracks with optional filtering, sorting, and pagination.

<h3 id="list-tracks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|title|query|any|false|Filter tracks by title (partial match)|
|artist|query|any|false|Filter tracks by artist name (partial match)|
|genre|query|any|false|Filter tracks by genre name (partial match)|
|mood|query|any|false|Filter tracks by mood keyword (partial match)|
|sort_by|query|string|false|Sort field: title, artist, rating, play_count|
|order|query|string|false|Sort order: asc or desc|
|limit|query|integer|false|Maximum number of results|
|offset|query|integer|false|Number of results to skip|

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "title": "string",
    "artist_name": "string",
    "album_title": "string",
    "duration_seconds": 0,
    "mood": "string",
    "play_count": 0,
    "average_rating": 0,
    "genre": {
      "id": 0,
      "name": "string",
      "description": "string"
    }
  }
]
```

<h3 id="list-tracks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="list-tracks-responseschema">Response Schema</h3>

Status Code **200**

*Response List Tracks Tracks Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Tracks Tracks Get|[[TrackRead](#schematrackread)]|false|none|[Schema for track responses (includes nested genre).]|
|» TrackRead|[TrackRead](#schematrackread)|false|none|Schema for track responses (includes nested genre).|
|»» id|integer|true|none|none|
|»» title|string|true|none|none|
|»» artist_name|string|true|none|none|
|»» album_title|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» duration_seconds|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|integer|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» mood|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» play_count|integer|true|none|none|
|»» average_rating|number|true|none|none|
|»» genre|[GenreRead](#schemagenreread)|true|none|Schema for genre responses.|
|»»» id|integer|true|none|none|
|»»» name|string|true|none|none|
|»»» description|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»»» *anonymous*|null|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Track

<a id="opIdget_track_tracks__track_id__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/tracks/{track_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/tracks/{track_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /tracks/{track_id}`

Return a single track by its ID.

<h3 id="get-track-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|track_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "title": "string",
  "artist_name": "string",
  "album_title": "string",
  "duration_seconds": 0,
  "mood": "string",
  "play_count": 0,
  "average_rating": 0,
  "genre": {
    "id": 0,
    "name": "string",
    "description": "string"
  }
}
```

<h3 id="get-track-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TrackRead](#schematrackread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-reviews">Reviews</h1>

## Create Review

<a id="opIdcreate_review_reviews_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/reviews', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "track_id": 0,
  "reviewer_name": "Alice",
  "rating": 4,
  "comment": "A beautiful and moving piece."
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/reviews',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /reviews`

Create a new review for a track.

> Body parameter

```json
{
  "track_id": 0,
  "reviewer_name": "Alice",
  "rating": 4,
  "comment": "A beautiful and moving piece."
}
```

<h3 id="create-review-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ReviewCreate](#schemareviewcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "track_id": 0,
  "reviewer_name": "string",
  "rating": 0,
  "comment": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="create-review-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[ReviewRead](#schemareviewread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## List Reviews

<a id="opIdlist_reviews_reviews_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/reviews', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/reviews',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /reviews`

List reviews with optional filtering and pagination.

<h3 id="list-reviews-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|track_id|query|any|false|Filter reviews by track ID|
|reviewer_name|query|any|false|Filter by reviewer name (partial match)|
|min_rating|query|any|false|Minimum rating filter|
|limit|query|integer|false|Maximum number of results|
|offset|query|integer|false|Number of results to skip|

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "track_id": 0,
    "reviewer_name": "string",
    "rating": 0,
    "comment": "string",
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="list-reviews-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="list-reviews-responseschema">Response Schema</h3>

Status Code **200**

*Response List Reviews Reviews Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Reviews Reviews Get|[[ReviewRead](#schemareviewread)]|false|none|[Schema for review responses.]|
|» ReviewRead|[ReviewRead](#schemareviewread)|false|none|Schema for review responses.|
|»» id|integer|true|none|none|
|»» track_id|integer|true|none|none|
|»» reviewer_name|string|true|none|none|
|»» rating|integer|true|none|none|
|»» comment|string|true|none|none|
|»» created_at|string(date-time)|true|none|none|
|»» updated_at|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Review

<a id="opIdget_review_reviews__review_id__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/reviews/{review_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/reviews/{review_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /reviews/{review_id}`

Return a single review by its ID.

<h3 id="get-review-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|review_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "track_id": 0,
  "reviewer_name": "string",
  "rating": 0,
  "comment": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="get-review-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ReviewRead](#schemareviewread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Update Review

<a id="opIdupdate_review_reviews__review_id__put"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/reviews/{review_id}', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "reviewer_name": "string",
  "rating": 1,
  "comment": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/reviews/{review_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PUT /reviews/{review_id}`

Update an existing review (partial update supported).

> Body parameter

```json
{
  "reviewer_name": "string",
  "rating": 1,
  "comment": "string"
}
```

<h3 id="update-review-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|review_id|path|integer|true|none|
|body|body|[ReviewUpdate](#schemareviewupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "track_id": 0,
  "reviewer_name": "string",
  "rating": 0,
  "comment": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="update-review-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ReviewRead](#schemareviewread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Delete Review

<a id="opIddelete_review_reviews__review_id__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/reviews/{review_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/reviews/{review_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /reviews/{review_id}`

Delete a review by its ID.

<h3 id="delete-review-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|review_id|path|integer|true|none|

> Example responses

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

<h3 id="delete-review-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-tags">Tags</h1>

## Create Tag

<a id="opIdcreate_tag_tags_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/tags', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "track_id": 0,
  "tag_name": "melancholic",
  "created_by": "Alice"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/tags',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /tags`

Create a user tag for a track.

> Body parameter

```json
{
  "track_id": 0,
  "tag_name": "melancholic",
  "created_by": "Alice"
}
```

<h3 id="create-tag-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserTagCreate](#schemausertagcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "track_id": 0,
  "tag_name": "string",
  "created_by": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="create-tag-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[UserTagRead](#schemausertagread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## List Tags

<a id="opIdlist_tags_tags_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/tags', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/tags',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /tags`

List user tags with optional track filtering.

<h3 id="list-tags-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|track_id|query|any|false|Filter tags by track ID|

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "track_id": 0,
    "tag_name": "string",
    "created_by": "string",
    "created_at": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="list-tags-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="list-tags-responseschema">Response Schema</h3>

Status Code **200**

*Response List Tags Tags Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Tags Tags Get|[[UserTagRead](#schemausertagread)]|false|none|[Schema for user tag responses.]|
|» UserTagRead|[UserTagRead](#schemausertagread)|false|none|Schema for user tag responses.|
|»» id|integer|true|none|none|
|»» track_id|integer|true|none|none|
|»» tag_name|string|true|none|none|
|»» created_by|string|true|none|none|
|»» created_at|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Delete Tag

<a id="opIddelete_tag_tags__tag_id__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/tags/{tag_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/tags/{tag_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /tags/{tag_id}`

Delete a user tag by its ID.

<h3 id="delete-tag-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tag_id|path|integer|true|none|

> Example responses

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

<h3 id="delete-tag-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-collections">Collections</h1>

## List Collections

<a id="opIdlist_collections_collections_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/collections', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/collections',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /collections`

Return all collections ordered by creation date.

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "created_by": "string",
    "created_at": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="list-collections-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="list-collections-responseschema">Response Schema</h3>

Status Code **200**

*Response List Collections Collections Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Collections Collections Get|[[CollectionRead](#schemacollectionread)]|false|none|[Schema for collection list responses.]|
|» CollectionRead|[CollectionRead](#schemacollectionread)|false|none|Schema for collection list responses.|
|»» id|integer|true|none|none|
|»» name|string|true|none|none|
|»» description|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» created_by|string|true|none|none|
|»» created_at|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Create Collection

<a id="opIdcreate_collection_collections_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/collections', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "name": "Evening Chill",
  "description": "Tracks for winding down.",
  "created_by": "Alice"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/collections',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /collections`

Create a new track collection.

> Body parameter

```json
{
  "name": "Evening Chill",
  "description": "Tracks for winding down.",
  "created_by": "Alice"
}
```

<h3 id="create-collection-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CollectionCreate](#schemacollectioncreate)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "created_by": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="create-collection-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[CollectionRead](#schemacollectionread)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Get Collection

<a id="opIdget_collection_collections__collection_id__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/collections/{collection_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/collections/{collection_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /collections/{collection_id}`

Return a collection with its track items.

<h3 id="get-collection-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|collection_id|path|integer|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get-collection-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get-collection-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete Collection

<a id="opIddelete_collection_collections__collection_id__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/collections/{collection_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/collections/{collection_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /collections/{collection_id}`

Delete a collection and all its items.

<h3 id="delete-collection-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|collection_id|path|integer|true|none|

> Example responses

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

<h3 id="delete-collection-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Add Track To Collection

<a id="opIdadd_track_to_collection_collections__collection_id__items_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/collections/{collection_id}/items', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "track_id": 0,
  "note": "Great opening track."
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/collections/{collection_id}/items',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /collections/{collection_id}/items`

Add a track to an existing collection.

> Body parameter

```json
{
  "track_id": 0,
  "note": "Great opening track."
}
```

<h3 id="add-track-to-collection-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|collection_id|path|integer|true|none|
|body|body|[CollectionItemCreate](#schemacollectionitemcreate)|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="add-track-to-collection-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add-track-to-collection-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Remove Item From Collection

<a id="opIdremove_item_from_collection_collections__collection_id__items__item_id__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/collections/{collection_id}/items/{item_id}', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/collections/{collection_id}/items/{item_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /collections/{collection_id}/items/{item_id}`

Remove a track item from a collection.

<h3 id="remove-item-from-collection-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|collection_id|path|integer|true|none|
|item_id|path|integer|true|none|

> Example responses

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

<h3 id="remove-item-from-collection-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="music-appreciation-and-discovery-api-analytics">Analytics</h1>

## Top Rated Tracks

<a id="opIdtop_rated_tracks_analytics_top_rated_tracks_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analytics/top-rated-tracks', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/analytics/top-rated-tracks',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /analytics/top-rated-tracks`

Return the highest-rated tracks that have at least one review.

<h3 id="top-rated-tracks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|Number of top tracks to return|

> Example responses

> 200 Response

```json
null
```

<h3 id="top-rated-tracks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="top-rated-tracks-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Genre Summary

<a id="opIdgenre_summary_analytics_genre_summary_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analytics/genre-summary', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/analytics/genre-summary',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /analytics/genre-summary`

Return a summary of each genre including track count and average rating.

> Example responses

> 200 Response

```json
null
```

<h3 id="genre-summary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="genre-summary-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Top Tags

<a id="opIdtop_tags_analytics_top_tags_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analytics/top-tags', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/analytics/top-tags',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /analytics/top-tags`

Return the most frequently used tags across all tracks.

<h3 id="top-tags-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|Number of top tags to return|

> Example responses

> 200 Response

```json
null
```

<h3 id="top-tags-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="top-tags-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Mood Distribution

<a id="opIdmood_distribution_analytics_mood_distribution_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analytics/mood-distribution', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/analytics/mood-distribution',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /analytics/mood-distribution`

Return the distribution of moods across all tracks.

> Example responses

> 200 Response

```json
null
```

<h3 id="mood-distribution-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="mood-distribution-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Review Activity

<a id="opIdreview_activity_analytics_review_activity_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analytics/review-activity', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/analytics/review-activity',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /analytics/review-activity`

Return overall review activity summary and per-reviewer breakdown.

> Example responses

> 200 Response

```json
null
```

<h3 id="review-activity-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="review-activity-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_CollectionCreate">CollectionCreate</h2>
<!-- backwards compatibility -->
<a id="schemacollectioncreate"></a>
<a id="schema_CollectionCreate"></a>
<a id="tocScollectioncreate"></a>
<a id="tocscollectioncreate"></a>

```json
{
  "name": "Evening Chill",
  "description": "Tracks for winding down.",
  "created_by": "Alice"
}

```

CollectionCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_by|string|true|none|none|

<h2 id="tocS_CollectionItemCreate">CollectionItemCreate</h2>
<!-- backwards compatibility -->
<a id="schemacollectionitemcreate"></a>
<a id="schema_CollectionItemCreate"></a>
<a id="tocScollectionitemcreate"></a>
<a id="tocscollectionitemcreate"></a>

```json
{
  "track_id": 0,
  "note": "Great opening track."
}

```

CollectionItemCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|track_id|integer|true|none|none|
|note|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CollectionRead">CollectionRead</h2>
<!-- backwards compatibility -->
<a id="schemacollectionread"></a>
<a id="schema_CollectionRead"></a>
<a id="tocScollectionread"></a>
<a id="tocscollectionread"></a>

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "created_by": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

CollectionRead

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_by|string|true|none|none|
|created_at|string(date-time)|true|none|none|

<h2 id="tocS_GenreRead">GenreRead</h2>
<!-- backwards compatibility -->
<a id="schemagenreread"></a>
<a id="schema_GenreRead"></a>
<a id="tocSgenreread"></a>
<a id="tocsgenreread"></a>

```json
{
  "id": 0,
  "name": "string",
  "description": "string"
}

```

GenreRead

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ReviewCreate">ReviewCreate</h2>
<!-- backwards compatibility -->
<a id="schemareviewcreate"></a>
<a id="schema_ReviewCreate"></a>
<a id="tocSreviewcreate"></a>
<a id="tocsreviewcreate"></a>

```json
{
  "track_id": 0,
  "reviewer_name": "Alice",
  "rating": 4,
  "comment": "A beautiful and moving piece."
}

```

ReviewCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|track_id|integer|true|none|none|
|reviewer_name|string|true|none|none|
|rating|integer|true|none|none|
|comment|string|true|none|none|

<h2 id="tocS_ReviewRead">ReviewRead</h2>
<!-- backwards compatibility -->
<a id="schemareviewread"></a>
<a id="schema_ReviewRead"></a>
<a id="tocSreviewread"></a>
<a id="tocsreviewread"></a>

```json
{
  "id": 0,
  "track_id": 0,
  "reviewer_name": "string",
  "rating": 0,
  "comment": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z"
}

```

ReviewRead

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|track_id|integer|true|none|none|
|reviewer_name|string|true|none|none|
|rating|integer|true|none|none|
|comment|string|true|none|none|
|created_at|string(date-time)|true|none|none|
|updated_at|string(date-time)|true|none|none|

<h2 id="tocS_ReviewUpdate">ReviewUpdate</h2>
<!-- backwards compatibility -->
<a id="schemareviewupdate"></a>
<a id="schema_ReviewUpdate"></a>
<a id="tocSreviewupdate"></a>
<a id="tocsreviewupdate"></a>

```json
{
  "reviewer_name": "string",
  "rating": 1,
  "comment": "string"
}

```

ReviewUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reviewer_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rating|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_TrackRead">TrackRead</h2>
<!-- backwards compatibility -->
<a id="schematrackread"></a>
<a id="schema_TrackRead"></a>
<a id="tocStrackread"></a>
<a id="tocstrackread"></a>

```json
{
  "id": 0,
  "title": "string",
  "artist_name": "string",
  "album_title": "string",
  "duration_seconds": 0,
  "mood": "string",
  "play_count": 0,
  "average_rating": 0,
  "genre": {
    "id": 0,
    "name": "string",
    "description": "string"
  }
}

```

TrackRead

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|title|string|true|none|none|
|artist_name|string|true|none|none|
|album_title|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|duration_seconds|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mood|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|play_count|integer|true|none|none|
|average_rating|number|true|none|none|
|genre|[GenreRead](#schemagenreread)|true|none|Schema for genre responses.|

<h2 id="tocS_UserTagCreate">UserTagCreate</h2>
<!-- backwards compatibility -->
<a id="schemausertagcreate"></a>
<a id="schema_UserTagCreate"></a>
<a id="tocSusertagcreate"></a>
<a id="tocsusertagcreate"></a>

```json
{
  "track_id": 0,
  "tag_name": "melancholic",
  "created_by": "Alice"
}

```

UserTagCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|track_id|integer|true|none|none|
|tag_name|string|true|none|none|
|created_by|string|true|none|none|

<h2 id="tocS_UserTagRead">UserTagRead</h2>
<!-- backwards compatibility -->
<a id="schemausertagread"></a>
<a id="schema_UserTagRead"></a>
<a id="tocSusertagread"></a>
<a id="tocsusertagread"></a>

```json
{
  "id": 0,
  "track_id": 0,
  "tag_name": "string",
  "created_by": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

UserTagRead

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|track_id|integer|true|none|none|
|tag_name|string|true|none|none|
|created_by|string|true|none|none|
|created_at|string(date-time)|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

