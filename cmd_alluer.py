import os

# allure generate ：生成allure测试报告的命令
# ./report :allure ：运行生成的临时报告文件路径
# -o ./new_report ：输出HTML的报告到report路径下
# --clean ：清除报告目录下原有的历史数据

# 打开本地服务器查看 allure open ./new_report
# 临时报告 allure serve ./report

run_cmd = "allure generate ./report -o ./new_report --clean"
os.system(run_cmd)