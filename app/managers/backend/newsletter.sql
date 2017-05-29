{% sql 'create', note='Create a newsletter entry' %}
INSERT INTO admin.newsletter (email, registered_at) VALUES
({{ email|guards.string }}, now())
RETURNING id::text, email, registered_at::text
{% endsql %}


{% sql 'list', note='List all newsletters' %}

SELECT
  id::text,
  email,
  registered_at::text,

FROM admin.newsletter
  ORDER BY registered_at DESC;

{% endsql %}
