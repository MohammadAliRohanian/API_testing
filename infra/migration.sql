create table runs
(
    id         int unsigned auto_increment
        primary key,
    status     enum ('Pass', 'Fail') null,
    started_at datetime              null,
    ended_at   datetime              null,
    duration   varchar(128)          null
);

create table cases
(
    id          int unsigned auto_increment
        primary key,
    run_id      int unsigned          not null,
    status      enum ('Pass', 'Fail') not null,
    module      varchar(256)          not null,
    name        varchar(256)          not null,
    description varchar(1024)         not null,
    route       varchar(512)          not null,
    http_code   int                   not null,
    started_at  datetime              not null,
    ended_at    datetime              not null,
    duration    varchar(128)          not null,
    constraint cases_runs_id_fk
        foreign key (run_id) references runs (id)
);