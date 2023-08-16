class run_model:
    def __init__(self):
        self.array = []
        self.module_count = 0
        self.status = ""
        self.started_at = ""
        self.ended_at = ""
        self.duration = ""

    def append(self, module_count, status, started_at, ended_at):
        self.module_count = module_count
        self.status = status
        self.started_at = started_at
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        csv = (
            str(self.module_count),
            self.status,
            str(self.started_at),
            str(self.ended_at),
            str(self.duration),
        )
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
