import os, xlrd, json

#  格式化数据


def formatData(basic_file_data, new_data):

    basic_file_data['datas'][0]['data_id'] = new_data['data_id']
    # datas -> env
    basic_file_data['datas'][0]['env']['pre_server_ts'] = new_data['pre_server_ts']
    basic_file_data['datas'][0]['env']['factory'] = new_data['factory']
    basic_file_data['datas'][0]['env']['country'] = new_data['country']
    basic_file_data['datas'][0]['env']['language'] = new_data['language']
    basic_file_data['datas'][0]['env']['vin'] = new_data['vin']
    basic_file_data['datas'][0]['env']['device_id'] = new_data['device_id']
    basic_file_data['datas'][0]['env']['device_type'] = new_data['device_type']
    basic_file_data['datas'][0]['env']['device_ver'] = new_data['device_ver']
    basic_file_data['datas'][0]['env']['device_model'] = new_data['device_model']
    basic_file_data['datas'][0]['env']['t_store_size'] = new_data['t_store_size']
    basic_file_data['datas'][0]['env']['t_mem_size'] = new_data['t_mem_size']
    basic_file_data['datas'][0]['env']['screen_h'] = new_data['screen_h']
    basic_file_data['datas'][0]['env']['screen_w'] = new_data['screen_w']
    basic_file_data['datas'][0]['env']['screen_size'] = new_data['screen_size']
    basic_file_data['datas'][0]['env']['screen_ratio'] = new_data['screen_ratio']
    basic_file_data['datas'][0]['env']['screen_orient'] = new_data['screen_orient']
    basic_file_data['datas'][0]['env']['imsi'] = new_data['imsi']
    basic_file_data['datas'][0]['env']['imei'] = new_data['imei']
    basic_file_data['datas'][0]['env']['cpu'] = new_data['cpu']
    basic_file_data['datas'][0]['env']['brand'] = new_data['brand']
    basic_file_data['datas'][0]['env']['d_start_ts'] = new_data['d_start_ts']
    basic_file_data['datas'][0]['env']['d_stop_ts'] = new_data['d_stop_ts']
    basic_file_data['datas'][0]['env']['net_type'] = new_data['net_type']
    basic_file_data['datas'][0]['env']['carrier'] = new_data['carrier']
    basic_file_data['datas'][0]['env']['os_ver'] = new_data['os_ver']
    basic_file_data['datas'][0]['env']['os_type'] = new_data['os_type']
    basic_file_data['datas'][0]['env']['p_code'] = new_data['p_code']
    basic_file_data['datas'][0]['env']['c_code'] = new_data['c_code']
    basic_file_data['datas'][0]['env']['a_code'] = new_data['a_code']
    basic_file_data['datas'][0]['env']['contact_type'] = new_data['contact_type']
    basic_file_data['datas'][0]['env']['link_start_ts'] = new_data['link_start_ts']
    basic_file_data['datas'][0]['env']['link_stop_ts'] = new_data['link_stop_ts']

    basic_file_data['datas'][0]['env']['gps'][0]['c_lon'] = new_data['c_lon']
    basic_file_data['datas'][0]['env']['gps'][0]['c_lat'] = new_data['c_lat']
    basic_file_data['datas'][0]['env']['gps'][0]['c_alt'] = new_data['c_alt']
    basic_file_data['datas'][0]['env']['gps'][0]['c_direct'] = new_data['c_direct']
    basic_file_data['datas'][0]['env']['gps'][0]['c_ts'] = new_data['c_ts']

    # track
    basic_file_data['datas'][0]['track'][0]['app_id'] = new_data['app_id']
    basic_file_data['datas'][0]['track'][0]['app_ver'] = new_data['app_ver']
    basic_file_data['datas'][0]['track'][0]['app_package'] = new_data['app_package']
    basic_file_data['datas'][0]['track'][0]['ver_code'] = new_data['ver_code']
    basic_file_data['datas'][0]['track'][0]['app_type'] = new_data['app_type']
    basic_file_data['datas'][0]['track'][0]['che_name'] = new_data['che_name']
    basic_file_data['datas'][0]['track'][0]['che_type'] = new_data['che_type']
    basic_file_data['datas'][0]['track'][0]['session_id'] = new_data['session_id']
    basic_file_data['datas'][0]['track'][0]['app_start_ts'] = new_data['app_start_ts']
    basic_file_data['datas'][0]['track'][0]['app_stop_ts'] = new_data['app_stop_ts']

    basic_file_data['datas'][0]['track'][0]['backstage_ts'][0]['into_backstage_ts'] = new_data['into_backstage_ts']
    basic_file_data['datas'][0]['track'][0]['backstage_ts'][0]['out_backstage_ts'] = new_data['out_backstage_ts']

    basic_file_data['datas'][0]['track'][0]['is_first'] = new_data['is_first']
    basic_file_data['datas'][0]['track'][0]['is_update'] = new_data['is_update']
    basic_file_data['datas'][0]['track'][0]['first_day'] = new_data['first_day']
    basic_file_data['datas'][0]['track'][0]['first_use'] = new_data['first_use']
    basic_file_data['datas'][0]['track'][0]['keep_alive'] = new_data['keep_alive']
    basic_file_data['datas'][0]['track'][0]['user_id'] = new_data['user_id']
    basic_file_data['datas'][0]['track'][0]['access'] = new_data['access']
    basic_file_data['datas'][0]['track'][0]['acc_type'] = new_data['acc_type']
    basic_file_data['datas'][0]['track'][0]['c_store_size'] = new_data['c_store_size']
    basic_file_data['datas'][0]['track'][0]['c_mem_size'] = new_data['c_mem_size']
    basic_file_data['datas'][0]['track'][0]['user_name'] = new_data['user_name']

    basic_file_data['datas'][0]['track'][0]['page'][0]['page_code'] = new_data['page_code']
    basic_file_data['datas'][0]['track'][0]['page'][0]['p_into_ts'] = new_data['p_into_ts']
    basic_file_data['datas'][0]['track'][0]['page'][0]['p_out_ts'] = new_data['p_out_ts']
    basic_file_data['datas'][0]['track'][0]['page'][0]['backstage_ts'][0]['into_backstage_ts'] = new_data['into_backstage_ts']
    basic_file_data['datas'][0]['track'][0]['page'][0]['backstage_ts'][0]['out_backstage_ts'] = new_data['out_backstage_ts']

    basic_file_data['datas'][0]['track'][0]['evt'][0]['evt_code'] = new_data['evt_code']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['evt_beg_ts'] = new_data['evt_beg_ts']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['evt_end_ts'] = new_data['evt_end_ts']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['backstage_ts'][0]['into_backstage_ts'] = new_data['into_backstage_ts']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['backstage_ts'][0]['out_backstage_ts'] = new_data['out_backstage_ts']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['touch_type'] = new_data['touch_type']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['evt_detail'][0]['item_name'] = new_data['item_name']
    basic_file_data['datas'][0]['track'][0]['evt'][0]['evt_detail'][0]['item_value'] = new_data['item_value']

    basic_file_data['datas'][0]['track'][0]['err'][0]['device_id'] = new_data['device_id']
    basic_file_data['datas'][0]['track'][0]['err'][0]['app_id'] = new_data['app_id']
    basic_file_data['datas'][0]['track'][0]['err'][0]['session_id'] = ""
    basic_file_data['datas'][0]['track'][0]['err'][0]['ip_addr'] = new_data['ip_addr']
    basic_file_data['datas'][0]['track'][0]['err'][0]['app_ver'] = new_data['app_ver']
    basic_file_data['datas'][0]['track'][0]['err'][0]['error'] = new_data['error']
    basic_file_data['datas'][0]['track'][0]['err'][0]['err_ts'] = new_data['err_ts']

    basic_file_data['datas'][0]['ext'] = new_data['ext']
    basic_file_data['datas'][0]['status'] = new_data['status']
    basic_file_data['datas'][0]['gen_ts'] = new_data['gen_ts']

    return basic_file_data

# 标准json格式数据读取
dir = os.getcwd()
basic_file = dir + '/basic.json'
basic_data_file = open(basic_file, encoding="utf-8")
basic_data_res = basic_data_file.read()
basic_file_data = json.loads(basic_data_res)
# print(basic_file_data)
# print(type(basic_file_data))

# 基础数据配置文件

basic_data = {}
bank_file = dir + '/bank_file-2.7.txt'
with open(bank_file, 'r', encoding='utf-8-sig') as fp:
    contents = fp.readlines()
    print(contents)
for info in contents:
    info = info.strip()  # 移除头尾的换行符
    # print(info)
    if info.find('=')>0:
        line_info = info.split('=')
        # print(line_info)
        key = line_info[0].strip()
        value = line_info[1].strip()
        # print(key, value)
        basic_data[key] = value
# print(basic_data)

# 读取测试用例

excel_file = dir + '/case.xlsx'
excel_open = xlrd.open_workbook(excel_file)
table = excel_open.sheet_by_name('清洗规则')   # 获取工作表（通过名称获取）
n_rows = table.nrows
n_cols = table.ncols
# print(n_rows,n_cols)
for row in range(n_rows):
    if row <= 1:
        continue
    number = int(table.cell_value(row, 0))  # 获取行号
    is_skip = table.cell_value(row, 3)
    input_data = table.cell_value(row, 4)   # 获取单元格值
    is_copy = table.cell_value(row, 5)
    # print(is_skip, input_data, is_copy)
    input_data_arr = {}
    new_data = {}
    if is_skip == 'Y':
        print("跳过第 %d 行" % number)
        continue
    input_data = input_data.split(';')
    print(input_data)
    for info1 in input_data:
        info1 = info1.split('=')
        print(info1)
        key = info1[0].strip()
        value = info1[1].strip()
        input_data_arr[key] = value
    print(input_data_arr)
    exit()
    # 组合测试数据
    new_data.update(basic_data)
    new_data.update(input_data_arr)
    print(new_data)
    new_json = formatData(basic_file_data, new_data)

    #  输出数据
    # output_file = dir + '/Output/output_file_' + str(number) + '.txt'
    # fo = open(output_file, 'a')
    # fo.write(json.dumps(new_json, ensure_ascii=False) + '\n')
    # fo.close()

    # 输出数据到一个文件里面
    output_file = dir+'/Output/sdk.txt'    # sdk.txt文件不存在的话新建，但是注意不能新建文件夹
    with open(output_file, 'a') as f1:
        f1.write(json.dumps(new_json, ensure_ascii=False)+'\n')



















