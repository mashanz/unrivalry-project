# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe
import os
import subprocess
import re
import shutil
import _thread


class Profiling:
    def _cpu():
        statistics = {}

        # Get Physical and Logical CPU Count
        physical_and_logical_cpu_count = os.cpu_count()
        statistics['physical_and_logical_cpu_count'] = physical_and_logical_cpu_count
        """
        # Load average 
        # This is the average system load calculated over a given period of time of 1, 5 and 15 minutes.
        # In our case, we will show the load average over a period of 15 minutes.
    
        # The numbers returned by os.getloadavg() only make sense if
        # related to the number of CPU cores installed on the system.
    
        # Here we are converting the load average into percentage. The higher the percentage the higher the load
        """
        cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
        statistics['cpu_load'] = round(cpu_load)
        return statistics

    def _ram():
        statistics = {}
        matcher = re.compile('\d+')
        # Memory usage
        total_ram = subprocess.run(
            ['sysctl', 'hw.memsize'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[
            0].decode('utf-8')
        vmLines = vm.split('\n')

        wired_memory = (
            int(matcher.search(vmLines[6]).group()) * 4096) / 1024 ** 3
        free_memory = (
            int(matcher.search(vmLines[1]).group()) * 4096) / 1024 ** 3
        active_memory = (
            int(matcher.search(vmLines[2]).group()) * 4096) / 1024 ** 3
        inactive_memory = (
            int(matcher.search(vmLines[3]).group()) * 4096) / 1024 ** 3

        # Used memory = wired_memory + inactive + active

        ram_total = int(matcher.search(total_ram).group()) / 1024 ** 3
        ram_used = round(wired_memory + active_memory + inactive_memory, 2)

        statistics['ram'] = dict({
            'total_ram': ram_total,
            'used_ram': ram_used,
            'precentage': round(ram_used / ram_total * 100, 1)
        })
        return statistics

    def _disk():
        statistics = {}
        # Top command on mac displays and updates sorted information about processes.
        top_command = subprocess.run(
            ['top', '-l 1', '-n 0'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        # Disk usage
        # Get total disk size, used disk space, and free disk
        total, used, free = shutil.disk_usage("/")
        # Number of Read and write operations
        # from the top command, the read written result will be as follows
        # 'Disks: XXXXXX/xxG read, XXXX/xxG written.'
        # we thus need to extract the read and written from this.
        read_written = top_command[9].split(':')[1].split(',')
        read = read_written[0].split(' ')[1]
        written = read_written[1].split(' ')[1]

        total_disk_space = round(total / 1024 ** 3, 1)
        free_disk_space = round(free / 1024 ** 3, 1)
        used_space = round(total / 1024 ** 3, 1) - round(free / 1024 ** 3, 1)
        precentage = round(used_space / total_disk_space * 100, 1)
        statistics['disk'] = dict(
            {
                'total_disk_space': total_disk_space,
                # 'used_disk_space': round(used / 1024 ** 3, 1),
                'used_disk_space': used_space,
                'free_disk_space': free_disk_space,
                'precentage': precentage,
                'read_write': {
                    'read': read,
                    'written': written
                }
            }
        )
        return statistics

    def _network():
        statistics = {}
        # Network latency
        """
        Here we will ping google at an interval of five seconds for five times and record the
        min response time, average response time, and the max response time.
        """
        ping_result = subprocess.run(['ping', '-i 5', '-c 5', 'google.com'], stdout=subprocess.PIPE).stdout.decode(
            'utf-8').split('\n')

        min, avg, max = ping_result[-2].split('=')[-1].split('/')[:3]
        statistics['network_latency'] = dict(
            {
                'min': min.strip(),
                'avg': avg.strip(),
                'max': max.strip(),
            }
        )
        return statistics


class AdminViews:

    @login_required(login_url="/login/")
    def index(request):
        main_content = "adm/video.html"
        return render(
            request,
            "adm/index.html",
            {
                "main_content": 'adm/blank.html',
            }
        )

    def video(request):
        main_content = "adm/video.html"
        return render(
            request,
            "adm/index.html",
            {
                "main_content": main_content,
            }
        )

    def dashboard(request):
        main_content = "adm/dashboard.html"
        statistics = dict()
        # try:
        #     _thread.start_new_thread(statistics.update, (Profiling._cpu(),))
        #     _thread.start_new_thread(statistics.update, (Profiling._ram(),))
        #     _thread.start_new_thread(statistics.update, (Profiling._disk(),))
        # except:
        #     print("Error: unable to start thread")

        statistics.update(Profiling._cpu())
        # statistics.update(Profiling._ram())
        statistics.update(Profiling._disk())

        return render(
            request,
            "adm/index.html",
            {
                "main_content": main_content,
                "profiling": statistics
            }
        )
