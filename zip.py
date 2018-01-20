import os
import time
source = ['"h:\\webbt\\Test"']
target_dir = 'H:\\backup'
# 如果目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today_dir = target_dir + os.sep + time.strftime('%Y%m%d')

if not os.path.exists(today_dir):
    os.mkdir(today_dir)

comment = input('Enter a comment -->')

if len(comment) == 0:
    target = today_dir + os.sep + \
             time.strftime('%Y%m%d%H%M%S') + '.zip'
else:
    target = today_dir + os.sep + \
             time.strftime('%Y%m%d%H%M%S') + '_' + comment.replace(' ','_') + '.zip'


zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('Zip command is:')
print(zip_command)
print('Runing:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('backup failed')