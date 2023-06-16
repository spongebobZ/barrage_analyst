from util.connection_pool import ConnectionPool


class MysqlClient:
    def __init__(self):
        self.connection_pool = ConnectionPool()

    def query_last_ts_watermark(self, room_id):
        sql = 'select max(timeline) from ods_barrage where room_id = ' + room_id
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        last_ts_watermark = cursor.fetchone()[0]
        connection.close()
        return last_ts_watermark

    def insert_dwd_barrage(self, message):
        sql = 'insert into dwd_barrage(room_id, uid, nickname, timeline, isadmin, vip, svip, medal_owner, medal_name, ' \
              'medal_level, guard_level, text, key_words) values (?,?,?,?,?,?,?,?,?,?,?,?,?)'
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()

