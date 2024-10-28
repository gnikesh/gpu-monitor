import json
import subprocess


if __name__ == "__main__":
    gpuinfo = subprocess.run(['gpustat', '--json'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    gpuinfo = gpuinfo.replace('fan.speed', 'fan_speed')
    gpuinfo = gpuinfo.replace('utilization.gpu', 'utilization_gpu')
    gpuinfo = gpuinfo.replace('memory.used', 'memory_used')
    gpuinfo = gpuinfo.replace('memory.total', 'memory_total')
    gpuinfo = gpuinfo.replace('utilization.enc', 'utilization_enc')
    gpuinfo = gpuinfo.replace('utilization.dec', 'utilization_dec')
    gpuinfo = gpuinfo.replace('power.draw', 'power_draw')
    gpuinfo = gpuinfo.replace('enforced.power.limit', 'enforced_power_limit')


    gpuinfo = json.loads(gpuinfo)

    hostname = gpuinfo.get('hostname', '')
    driver_ver = gpuinfo.get('driver_version', '')
    gpus = gpuinfo.get('gpus', [])
    print(gpuinfo)