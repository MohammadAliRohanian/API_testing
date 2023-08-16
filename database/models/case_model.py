class case_model:
    def __init__(self):
        self.array = []
        self.module_id = 0
        self.name = ""
        self.status = ""
        self.http_code = 0
        self.started_at = ""
        self.ended_at = ""
        self.duration = ""

    def append(self, module_id, name, status, http_code, started_at, ended_at):
        self.module_id = module_id
        self.name = name
        self.status = status
        self.http_code = http_code
        self.started_at = started_at
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        csv = (
            self.module_id,
            self.name,
            self.status,
            self.http_code,
            str(self.started_at),
            str(self.ended_at),
            str(self.duration),
        )
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
