create schema if not exists job;

drop table if exists job.jobs cascade;

create table job.jobs (
  id bigserial not null primary key,
  name text not null,
  args json,
  priority int not null default 0,
  serialization_key_id bigint,
  started_at timestamptz,
  completed_at timestamptz,
  error_message text,
  created_at timestamptz not null default now()
);

drop table if exists job.serialization_keys cascade;

create table job.serialization_keys (
  id bigserial not null primary key,
  key text not null unique,
  active_job_id bigint references job.jobs (id)
);

create index jobs_serialization_key_id_idx on jobs (serialization_key_id);

alter table job.jobs add constraint job_jobs_serialization_key_id_fkey
foreign key (serialization_key_id) references job.serialization_keys (id);

create or replace function tg_notify_on_new_job()
returns trigger as
$BODY$
begin
  perform pg_notify('job_inserted', NEW.id::text);
  return null;
end
$BODY$
language plpgsql;

drop trigger if exists job_jobs_notify_on_insert_tg on job.jobs;

create trigger job_jobs_notify_on_insert_tg
after insert
on job.jobs
for each row
execute procedure tg_notify_on_new_job();

