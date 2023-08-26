class run_model:
    def append(self, id, status, started_at, ended_at):
        self.array = []
        self.id = id
        self.status = status
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        csv = (str(self.id), self.status, str(self.ended_at), str(self.duration))
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
