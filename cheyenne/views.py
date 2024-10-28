import json
import gpustat
import subprocess
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    # gpuinfo = {'hostname': 'cheyenne', 'driver_version': '525.147.05', 'query_time': '2024-02-11T14:00:27.910911', 'gpus': [{'index': 0, 'uuid': 'GPU-e03437ed-299d-3847-94f8-c71edd678b0c', 'name': 'NVIDIA A40', 'temperature.gpu': 39, 'fan_speed': 0, 'utilization_gpu': 0, 'utilization_enc': 0, 'utilization_dec': 0, 'power_draw': 75, 'enforced_power_limit': 300, 'memory_used': 9105, 'memory_total': 46068, 'processes': [{'username': 'gnikesh', 'command': 'python3', 'full_command': ['/home/g/gnikesh/venvs/stance-cheyenne/bin/python3', '-m', 'ipykernel_launcher', '--f=/home/g/gnikesh/.local/share/jupyter/runtime/kernel-v2-1396033iidTNHgrPCPk.json'], 'gpu_memory_usage': 8484, 'cpu_percent': 0.0, 'cpu_memory_usage': 4447592448, 'pid': 1433835}]}, {'index': 1, 'uuid': 'GPU-b8bad2c2-d372-5e04-a187-232a344af098', 'name': 'NVIDIA A40', 'temperature.gpu': 20, 'fan_speed': 0, 'utilization_gpu': 0, 'utilization_enc': 0, 'utilization_dec': 0, 'power_draw': 15, 'enforced_power_limit': 300, 'memory_used': 621, 'memory_total': 46068, 'processes': []}, {'index': 2, 'uuid': 'GPU-b1603c0d-4b7d-160e-2409-8b703082b0be', 'name': 'NVIDIA A40', 'temperature.gpu': 19, 'fan_speed': 0, 'utilization_gpu': 0, 'utilization_enc': 0, 'utilization_dec': 0, 'power_draw': 14, 'enforced_power_limit': 300, 'memory_used': 621, 'memory_total': 46068, 'processes': []}, {'index': 3, 'uuid': 'GPU-55eeed00-c3ed-bd2d-f7f5-24f87cb78336', 'name': 'NVIDIA A40', 'temperature.gpu': 42, 'fan_speed': 0, 'utilization_gpu': 0, 'utilization_enc': 0, 'utilization_dec': 0, 'power_draw': 83, 'enforced_power_limit': 300, 'memory_used': 4431, 'memory_total': 46068, 'processes': [{'username': 'ngautam', 'command': 'python3', 'full_command': ['/home/n/ngautam/semiSuperLearning/semisl/bin/python3', '-m', 'ipykernel_launcher', '-f', '/home/n/ngautam/.local/share/jupyter/runtime/kernel-2e69b92a-292c-494a-911a-6940148f3086.json'], 'gpu_memory_usage': 3810, 'cpu_percent': 0.0, 'cpu_memory_usage': 2838548480, 'pid': 1526618}]}]}
    gpuinfo = subprocess.run(['gpustat', '--json'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    if not gpuinfo:
        return render(request, 'cheyenne/index.html', context={'context': {'server_error': 'Error fetching GPU information!'}})
    
    gpuinfo = gpuinfo.replace('fan.speed', 'fan_speed')
    gpuinfo = gpuinfo.replace('utilization.gpu', 'utilization_gpu')
    gpuinfo = gpuinfo.replace('memory.used', 'memory_used')
    gpuinfo = gpuinfo.replace('memory.total', 'memory_total')
    gpuinfo = gpuinfo.replace('utilization.enc', 'utilization_enc')
    gpuinfo = gpuinfo.replace('utilization.dec', 'utilization_dec')
    gpuinfo = gpuinfo.replace('power.draw', 'power_draw')
    gpuinfo = gpuinfo.replace('enforced.power.limit', 'enforced_power_limit')
    gpuinfo = json.loads(gpuinfo)

    context = {}
        
    context['hostname'] = gpuinfo.get('hostname', '')
    context['driver_version'] = gpuinfo.get('driver_version', '')
    context['gpus'] = gpuinfo.get('gpus', [])
    for gpu in context['gpus']:
        gpu['memory_utilization_percent'] = int(gpu['memory_used'] / gpu['memory_total'] * 100)
        
    context['gpu_count'] = len(context['gpus'])

    return render(request, 'cheyenne/index.html', context={'context': context})