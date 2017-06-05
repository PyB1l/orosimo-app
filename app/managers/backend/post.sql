-- =============================================================
--          admin app Post model SQL db mapper.
-- =============================================================

{% sql 'count', note='Count total Posts' %}
SELECT
  count(id) total
FROM admin.post
  WHERE is_public = TRUE
{% endsql %}


{% sql 'create', note='Create a new Post model.' %}
INSERT INTO admin.post (title, body, img) values (
  {{ title|guards.string }},
  $${{ body }}$$,
  {{ img|guards.string }}
)
RETURNING
  id::text,
  title,
  body,
  img,
  posted_at::text,
  likes,
  (select count(a.*) from admin.post_comment a where a.post_id = admin.post.id)::int total_comments

{% endsql %}


{% sql 'retrieve', note='Get a Post model by id' %}

SELECT
  id::text,
  title,
  body,
  img,
  posted_at::text,
  likes,
  (select count(a.*) from admin.post_comment a where a.post_id = admin.post.id)::int total_comments

FROM admin.post
  WHERE id = {{ uid }}

{% endsql %}


{% sql 'delete', note='Delete a Post model by id' %}
DELETE FROM admin.post where id = {{ uid }}
RETURNING
  id::text,
  title,
  body,
  img,
  posted_at::text,
  likes,
  (select count(a.*) from admin.post_comment a where a.post_id = admin.post.id)::int total_comments

{% endsql %}


{% sql 'list', note='Get all Post models' %}

SELECT
  id::text,
  title,
  body,
  img,
  posted_at::text,
  likes,
  (select count(a.*) from admin.post_comment a where a.post_id = admin.post.id)::int total_comments

FROM admin.post
  WHERE is_public = TRUE
ORDER BY posted_at DESC

{% if offset %}
OFFSET {{ offset|guards.integer }}
{% endif %}

{% if limit %}
LIMIT {{ limit|guards.integer }}
{% endif %}

{% endsql %}

