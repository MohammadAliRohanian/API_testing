class run_model:
    def append(self, status, started_at, ended_at, id):
        self.array = []
        self.status = status
        self.ended_at = ended_at
        self.duration = ended_at - started_at
        self.id = id
        csv = (self.status, str(self.ended_at), str(self.duration), str(self.id))
        self.array.append(csv)

    def get_csv_array(self):
        return self.array
