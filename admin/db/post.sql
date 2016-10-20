-- =============================================================
--          admin app Post model SQL db mapper.
-- =============================================================

{% sql 'get', note='Get a Post model by id' %}

SELECT
  id,
  title,
  body,
  img,
  posted_at

FROM admin.post
  WHERE id = {{ uid }}

{% endsql %}


{% sql 'all', note='Get all Post models' %}

SELECT
  id,
  title,
  body,
  img,
  posted_at

FROM admin.post

{% if offset %}
OFFSET {{ offset|guards.integer }}
{% endif %}

{% if limit %}
LIMIT {{ limit|guards.integer }}
{% endif %}

{% endsql %}


{% sql 'Create', note='Create a new post' %}

INSERT INTO admin.post (title, body, img) VALUES
('{{ title|guards.string }}', $${{ body }}$$, '{{ img|guards.string }}')
RETURNING *;

{% endsql %}


{% sql 'get_latest', note='Retrieve n-latest posts' %}

SELECT
  id,
  title,
  body,
  img,
  posted_at

FROM admin.post
  ORDER by posted_at DESC
LIMIT {{ limit }}

{% endsql %}


