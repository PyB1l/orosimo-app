-- =============================================================
--          admin app Post model SQL db mapper.
-- =============================================================

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

{% sql 'count', note='Count total Posts' %}
SELECT
  count(id) total
FROM admin.post
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

FROM admin.post ORDER BY posted_at DESC

{% if offset %}
OFFSET {{ offset|guards.integer }}
{% endif %}

{% if limit %}
LIMIT {{ limit|guards.integer }}
{% endif %}

{% endsql %}

