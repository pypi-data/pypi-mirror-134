#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import csv
import logging
import os
from xmind2testcase.utils import get_xmind_testcase_list, get_absolute_path
from io import StringIO
import csv
import pandas as pd
import openpyxl
"""
Convert XMind fie to Zentao testcase csv file 

Zentao official document about import CSV testcase file: https://www.zentao.net/book/zentaopmshelp/243.mhtml 
"""
def csv_to_xls(csv_path, xls_path):
    with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    data_file = StringIO(data)
    print(data_file)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "sheet1"

    csv_reader = csv.reader(data_file)
    list_csv = []
    for row in csv_reader:
        list_csv.append(row)
    df_csv = pd.DataFrame(list_csv).applymap(str)
    writer = pd.ExcelWriter(xls_path)
    df_csv.to_excel(excel_writer=writer,
                    index=False,
                    header=False)
    writer.save()

def xmind_to_zentao_csv_file(xmind_file):
    """Convert XMind file to a zentao csv file"""
    xmind_file = get_absolute_path(xmind_file)
    logging.info('Start converting XMind file(%s) to zentao file...', xmind_file)
    testcases = get_xmind_testcase_list(xmind_file)

    fileheader = ["用例目录", "用例名称", "需求ID", "前置条件", "用例步骤", "预期结果", "用例类型", "用例状态", "用例等级", "创建人"]
    zentao_testcase_rows = [fileheader]
    for testcase in testcases:
        row = gen_a_testcase_row(testcase)
        zentao_testcase_rows.append(row)

    zentao_file = xmind_file[:-6] + '.csv'
    if os.path.exists(zentao_file):
        os.remove(zentao_file)
        # logging.info('The zentao csv file already exists, return it directly: %s', zentao_file)
        # return zentao_file

    with open(zentao_file, 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(zentao_testcase_rows)
        logging.info('Convert XMind file(%s) to a zentao csv file(%s) successfully!', xmind_file, zentao_file)

    return zentao_file


def gen_a_testcase_row(testcase_dict):
    case_id = gen_case_module(testcase_dict['suite'])
    case_title = testcase_dict['name']
    case_precontion = testcase_dict['preconditions']
    case_step, case_expected_result = gen_case_step_and_expected_result(testcase_dict['steps'])
    # case_keyword = ''
    case_module = ''
    case_status = gen_case_status('')
    case_priority = gen_case_priority(testcase_dict['importance'])
    case_type = gen_case_type('')
    case_creater = "李志中"
    # case_type = gen_case_type(testcase_dict['execution_type'])
    # case_apply_phase = '迭代测试'
    # row = [case_module, case_title, case_precontion, case_step, case_expected_result, case_keyword, case_priority, case_type, case_apply_phase]
    row = [case_module, case_title, case_id ,case_precontion, case_step, case_expected_result, case_type, case_status, case_priority, case_creater]

    return row


def gen_case_module(module_name):
    if module_name:
        module_name = module_name.replace('（', '(')
        module_name = module_name.replace('）', ')')
    else:
        module_name = '/'
    return module_name


def gen_case_step_and_expected_result(steps):
    case_step = ''
    case_expected_result = ''

    for step_dict in steps:
        case_step += str(step_dict['step_number']) + '. ' + step_dict['actions'].replace('\n', '').strip() + '\n'
        case_expected_result += str(step_dict['step_number']) + '. ' + \
            step_dict['expectedresults'].replace('\n', '').strip() + '\n' \
            if step_dict.get('expectedresults', '') else ''

    return case_step, case_expected_result

# 获取用例等级
def gen_case_priority(priority):
    mapping = {1: '高', 2: '中', 3: '低'}
    if priority in mapping.keys():
        return mapping[priority]
    else:
        return '中'

# 获取用例类型
def gen_case_type(case_type):
    mapping = {1: '功能测试', 2: '性能测试', 3:'安全性测试' , 4:'其他'}
    if case_type in mapping.keys():
        return mapping[case_type]
    else:
        return '功能测试'

# 获取用例状态
def gen_case_status(status):
    mapping = {1: "正常", 2: "待更新", 3: "已废弃"}
    if status in mapping.keys():
        return mapping[status]
    else:
        return '正常'


if __name__ == '__main__':
    xmind_file = '../docs/zentao_testcase_template.xmind'
    zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
    print('Conver the xmind file to a zentao csv file succssfully: %s', zentao_csv_file)