-- migrate:up

CREATE TABLE sample (
  id serial,
  raw_data jsonb,
  created_at timestamp without time zone DEFAULT now() NOT NULL,
  updated_at timestamp without time zone DEFAULT now(),

  PRIMARY KEY (id)
);



-- migrate:down

DROP TABLE sample

