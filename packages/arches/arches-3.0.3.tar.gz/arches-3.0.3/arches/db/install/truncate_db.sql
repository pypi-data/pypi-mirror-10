SELECT pg_terminate_backend(pid) from pg_stat_activity where datname='arches_arches_hip';

DROP DATABASE IF EXISTS arches_arches_hip;

CREATE DATABASE arches_arches_hip
  WITH ENCODING='UTF8'
       OWNER=postgres
       TEMPLATE=template_postgis_20
       CONNECTION LIMIT=-1;

