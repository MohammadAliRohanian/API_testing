class case_model:
    def append(
        self,
        run_id,
        status,
        module,
        name,
        description,
        api_route,
        http_code,
        started_at,
        ended_at,
    ):
        self.array = []
        self.run_id = run_id
        self.status = status
        self.module = module
        self.name = name
        self.description = description
        self.api_route = api_route
        self.http_code = http_code
        self.started_at = started_at
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        csv = (
            self.run_id,
            self.status,
            self.module,
            self.name,
            self.description,
            self.api_route,
            self.http_code,
            str(self.started_at),
            str(self.ended_at),
            str(self.duration),
        )
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
