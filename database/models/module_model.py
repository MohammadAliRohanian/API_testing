class module_model:
    def __init__(self):
        self.array = []
        self.run_id = 0
        self.route = ""
        self.case_count = 0
        self.status = ""
        self.started_at = ""
        self.ended_at = ""
        self.duration = ""

    def append(self, run_id, route, case_count, status, started_at, ended_at):
        self.run_id = run_id
        self.route = route
        self.case_count = case_count
        self.status = status
        self.started_at = started_at
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        csv = (
            self.run_id,
            self.route,
            self.case_count,
            self.status,
            str(self.started_at),
            str(self.ended_at),
            str(self.duration),
        )
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
