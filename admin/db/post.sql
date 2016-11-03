-- =============================================================
--          admin app Post model SQL db mapper.
-- =============================================================

{% sql 'get', note='Get a Post model by id' %}

SELECT
  id,
  title,
  body,
  img,
  posted_at,
  likes,
  (select count(*) from admin.post_comment)::int total_comments

FROM admin.post
  WHERE id = {{ uid }}

{% endsql %}

{% sql 'count', note='Count total Posts' %}
SELECT
  count(id) total
FROM admin.post
{% endsql %}


{% sql 'all', note='Get all Post models' %}

SELECT
  id,
  title,
  body,
  img,
  posted_at,
  likes,
  (select count(*) from admin.post_comment)::int total_comments

FROM admin.post ORDER BY posted_at DESC

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
  posted_at,
  likes,
  (select count(a.*) from admin.post_comment a where a.post_id = admin.post.id)::int total_comments

FROM admin.post
  ORDER by posted_at DESC
LIMIT {{ limit }}

{% endsql %}

{% sql 'add_like', note='Add a Like to a post' %}

  UPDATE admin.post SET likes = likes + 1 WHERE
  id = {{ uid }}
  returning *

{% endsql %}


{% sql 'add_comment', note='Add comment to a post' %}

  INSERT INTO admin.post_comment (post_id, email, person, body) VALUES
  ({{ uid }}, '{{ email }}', '{{ person }}', $${{ body }}$$)
  returning *

{% endsql %}