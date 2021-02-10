from db import db


class SystemInfoTable(db.Model):
    __tablename__ = 'system_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    system_id = db.Column(db.String(80))
    sys_cpu_percentage = db.Column(db.String(80))
    sys_ram_usage = db.Column(db.String(80))
    last_updated_timestamp = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, system_id, sys_cpu_percentage, sys_ram_usage):
        self.system_id = system_id
        self.sys_cpu_percentage = sys_cpu_percentage
        self.sys_ram_usage = sys_ram_usage

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'systemId': self.system_id, 'cpuPercentage': self.sys_cpu_percentage,
                'ramUsage': self.sys_ram_usage}
