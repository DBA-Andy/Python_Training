#python3
#exec(open("/vol/nwdba/python3/v-py3/bin/activate_this.py").read())

import cx_Oracle
import datetime
import custom_sqlnet
from multiprocessing import Pool
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    print ("The timeout module was invoked")
    raise TimeoutException


def get_master_connection():
    v_master_connection = cx_Oracle.connect('nwadbprd/Nwpwstr1@nfaes02d')
    v_master_cursor = v_master_connection.cursor()
    v_get_run_id_text = "select max(monitor_id) from monitor_framework_run";
    v_master_cursor.prepare(v_get_run_id_text)
    v_master_cursor.execute(v_get_run_id_text)
    v_run_id = v_master_cursor.fetchall();
    v_run_id_str = ''.join(str(v_run_id[0][0]))

    return v_master_connection, v_master_cursor, v_run_id_str

def setup_run():
    print ("Starting setup_run" + " at " + str(datetime.datetime.now()))
    v_tstart = datetime.datetime.now()

    v_master_connection, v_master_cursor, v_run_id_str = get_master_connection()

    v_insert_run_text = "insert into nwadbprd.monitor_framework_run (monitor_id, monitor_run_time) values (nwadbprd.monitor_framework_run_seq.nextval, sysdate)"
    v_master_cursor.prepare(v_insert_run_text)
    v_master_cursor.execute(v_insert_run_text)
    v_master_connection.commit()
    print ("Finished get_supported_databases" + " at " + str(datetime.datetime.now()))

    v_master_cursor.close()
    v_master_connection.close()


    return v_run_id_str, v_tstart

def get_supported_databases(v_run_id_str):
    print ("Starting get_supported_databases" + " at " + str(datetime.datetime.now()))

    custom_sqlnet.reset_tns()

    v_master_connection, v_master_cursor, v_run_id_str = get_master_connection()

    v_db_query_text = "select database_name from table(nfadsprd.rdds_common.get_supported_databases(v_technology=>'ORACLE',v_excluded_usage=>'DR', v_support_team=>'ASSURANCE'))"
    v_db_query_text = v_db_query_text + "WHERE host_name NOT IN ('EHPLORAC9081', 'EHPLORAC9082', 'EHPLORAC9091', 'EHPLORAC9092', 'EHPLORAC9101', 'EHPLORAC9102', 'EHPLORAC9111',"
    v_db_query_text = v_db_query_text + "'EHPLORAC9112', 'NHPLORAC9081', 'NHPLORAC9082', 'NHPLORAC9091', 'NHPLORAC9092', 'NHPLORAC9101', 'NHPLORAC9102', 'NHPLORAC9111', 'NHPLORAC9112')"
    #v_db_query_text = v_db_query_text + "and database_name like 'D%'"
    v_master_cursor.prepare(v_db_query_text)
    v_master_cursor.execute(v_db_query_text)
    v_database_list = sorted(set(v_master_cursor.fetchall()))
    print (str(len((v_database_list))) + " databases will have attempts to query made for run ID " + v_run_id_str + ".")
    print ("Finished get_supported_databases" + " at " + str(datetime.datetime.now()))

    v_master_cursor.close()
    v_master_connection.close()

    return v_database_list

def process_supported_databases(v_database_list):

    signal.signal(signal.SIGALRM, timeout_handler)

    v_databases_processed = 1
    v_master_connection, v_master_cursor, v_run_id_str = get_master_connection()

    for v_database in v_database_list:
        v_db = str(v_database)
        v_query_text = 'select query_text, query_result_insert_stmt from nwadbprd.monitoring_queries_vw where database_name is null or database_name = ' + "'" + v_db + "'"
        v_master_cursor.prepare(v_query_text)
        v_master_cursor.execute(v_query_text)
        v_query_list = v_master_cursor.fetchall()

        try:
            v_query_connect_string = 'nwadbprd/Nwpwstr1@' + v_db
            v_query_connection = cx_Oracle.connect(v_query_connect_string)
            v_query_cursor = v_query_connection.cursor()
        except cx_Oracle.OperationalError as v_db_error_ops:
            print (v_db + " had error " + str(v_db_error_ops) + " while executing.")
        except cx_Oracle.DatabaseError as v_db_error:
            print (v_db + " had error " + str(v_db_error) + " while executing.")
        else:
            v_insert_counter = 0
            for v_query in v_query_list:
                v_query_iterator = 0
                v_query_text = v_query[v_query_iterator]
                v_query_insert = v_query[v_query_iterator + 1]
                v_query_to_run = str(v_query_text)
                try:
                    v_query_cursor.prepare(v_query_to_run)
                    v_query_cursor.execute(v_query_to_run)
                    try:
                        signal.alarm(30)
                        v_query_result = v_query_cursor.fetchall()
                        signal.alarm(0)
                    except TimeoutException:
                        pass
                    if v_query_insert is not None:
                       v_bind_variables = [v_run_id_str, v_db]
                       v_bind_list = []
                       try:
                           v_master_cursor.prepare(v_query_insert)
                           for v_list in v_query_result:
                               for v_tuple in v_list:
                                   v_bind_variables.append(v_tuple)
                               v_bind_list.append(v_bind_variables)
                               v_bind_variables = [v_run_id_str, v_db]
                           v_insert_counter += 1
                           v_master_cursor.executemany(None,v_bind_list)
                       except cx_Oracle.DatabaseError as v_insert_error:
                           print (v_insert_error)
                    v_query_iterator += 1
                except cx_Oracle.DatabaseError as v_inner_query_db_error:
                    print (str(v_inner_query_db_error) + "exception occurred on database " + str(v_db))
                except Exception as v_exception:
                    print (v_exception)
            if v_insert_counter > 0:
                if v_databases_processed%100 == 0:
                    print ("Executing Commit # " + str(v_databases_processed) + " at " + str(datetime.datetime.now()))
                v_master_connection.commit()
                v_databases_processed += 1
                v_insert_counter = 0
                v_tuple_iterator = 0
            v_query_cursor.close()
            v_query_connection.close()
    v_master_cursor.close()
    v_master_connection.close()

def finish_run(v_tstart):
    print ("Starting finish_run" + " at " + str(datetime.datetime.now()))
    v_tend = datetime.datetime.now()
    v_runtime = v_tend - v_tstart
    print ("Started at " + str(v_tstart) + ", ended at " + str(v_tend) + ", and ran for " + str(v_runtime))
    print ("Finished finish_run" + " at " + str(datetime.datetime.now()))

def main():
    print ("Starting Main" + " at " + str(datetime.datetime.now()))
    v_run_id_str, v_tstart =  setup_run()
    v_database_list = get_supported_databases(v_run_id_str)

    print ("Starting process_supported_databases" + " at " + str(datetime.datetime.now()))
    try:
        with Pool(30) as pool:
            pool.map(process_supported_databases, v_database_list)
    except Exception as v_exception:
        print(v_exception)
    print ("Finished process_supported_databases" + " at " + str(datetime.datetime.now()))

    finish_run(v_tstart)
    print ("Finished Main" + " at " + str(datetime.datetime.now()))

if __name__ == "__main__":
    main()
