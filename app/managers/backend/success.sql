
{% sql 'list', note='Get all Success models by year' %}
SELECT
  id::text,
  full_name,
  school_year,
  university,
  promoted
FROM admin.success
  WHERE school_year = {{ year }}
{% endsql %}


{% sql 'years' %}
select distinct on (school_year) school_year from admin.success
order by school_year DESC;
{% endsql %}