from flask_restful import Resource
from flask import request, jsonify
from db_models import SystemInfoTable
from sqlalchemy import desc
from flask_mail import Message
from mail import mail


class SystemInfo(Resource):
    def get(self):
        """Get System information"""
        sys_id = request.args.get('sys_id')
        db_rec = SystemInfoTable.query.filter_by(system_id=sys_id).order_by(desc('last_updated_timestamp')).first()
        return db_rec.json(), 200

    def post(self):
        sys_id = request.json['sys_id']
        sys_cpu_percentage = request.json['sys_cpu_percentage']
        sys_ram_usage = request.json['sys_ram_usage']
        if float(sys_cpu_percentage) > 90:
            msg = Message(f"Hello There, The CPU usage of {sys_id} is {sys_cpu_percentage}",
                          sender="from@example.com",
                          recipients=["to@example.com"])
            mail.send(msg)
        db_record = SystemInfoTable(sys_id, sys_cpu_percentage, sys_ram_usage)
        db_record.save_to_db()
        return dict(message='Saved to db'), 201
