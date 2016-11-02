{% sql 'get', note='Get a Success model by id' %}

SELECT
  id,
  full_name,
  school_year,
  university,
  promoted
FROM admin.success
  WHERE id = {{ uid }}

{% endsql %}


{% sql 'get_year', note='Get all Success models by year' %}
SELECT
  id,
  full_name,
  school_year,
  university,
  promoted
FROM admin.success
  WHERE school_year = {{ year }}
{% endsql %}


{% sql 'get_promoted', note='GEt all promoted Success models by year' %}
SELECT
  id,
  full_name,
  school_year,
  university,
  promoted,
  promotion_banner ''
FROM admin.success
  WHERE school_year = {{ year }}
  AND promoted = True
{% endsql %}

{% sql 'available_years' %}
select distinct on (school_year) school_year from admin.success
order by school_year DESC;
{% endsql %}