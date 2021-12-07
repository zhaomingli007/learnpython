import os
def disk_usage(path):
    size = os.path.getsize(path)
    if os.path.isdir(path):
        for d in os.listdir(path):
            size += disk_usage(os.path.join(path, d)) 
    print('{0:<7}'.format(size), path)
    return size

disk_usage('/tmp')


