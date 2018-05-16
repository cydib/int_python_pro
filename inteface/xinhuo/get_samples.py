#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 18:07:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import MySQLdb
import urllib.request


def downimg():
    # 	'''
    # 	获取样本到samples文件夹
    # 	'''
    os.system("mkdir samples")
    db = MySQLdb.connect(host="68.71.4.151", port=3306, user="admin",
                         passwd="introcks", db="intellif_static", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT  extend_field,xm, gmsfhm from intellif_static.t_other_info WHERE id > 25009200  and gmsfhm like '4403011970%'  and extend_field <>'' group by gmsfhm LIMIT 500;"
#   sql1 = "SELECT extend_field,xm,gmsfhm from t_other_info WHERE id > 25009200 LIMIT 1000;"
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        url = i[0]
        name = i[1]
        idCard = i[2]
        print(url, name, idCard)
        urllib.request.urlretrieve(url, "./samples/"+name+"_"+idCard+".jpg")


if __name__ == '__main__':
	downimg()


