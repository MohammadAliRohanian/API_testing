create table runs
(
    id           int unsigned auto_increment
        primary key,
    module_count int                   null,
    status       enum ('Pass', 'Fail') null,
    started_at   datetime              null,
    ended_at     datetime              null,
    duration     varchar(50)           null
);

create table modules
(
    id         int unsigned auto_increment
        primary key,
    run_id     int unsigned          not null,
    route      varchar(100)          null,
    case_count int                   null,
    status     enum ('Pass', 'Fail') null,
    started_at datetime              null,
    ended_at   datetime              null,
    duration   varchar(50)           null,
    constraint modules_runs_id_fk
        foreign key (run_id) references runs (id)
);

create table cases
(
    id         int unsigned auto_increment
        primary key,
    module_id  int unsigned          not null,
    name       varchar(100)          not null,
    status     enum ('Pass', 'Fail') null,
    http_code  int                   not null,
    started_at datetime              null,
    ended_at   datetime              null,
    duration   varchar(50)           null,
    constraint cases_modules_id_fk
        foreign key (module_id) references modules (id)
);

