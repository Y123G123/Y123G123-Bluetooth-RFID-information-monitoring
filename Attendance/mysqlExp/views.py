from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import BluetoothData

@csrf_exempt
def save_bluetooth_data(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        if card_number:
            # 查找最近的相同卡号的刷卡记录
            existing_entry = BluetoothData.objects.filter(card_number=card_number).order_by('-timestamp').first()

            # 确定是打卡还是签退
            if existing_entry and existing_entry.status == '打卡':
                status = '签退'
            else:
                status = '打卡'

            # 创建新的记录
            BluetoothData.objects.create(card_number=card_number, status=status)
            return JsonResponse({'status': 'success', 'message': f'{status} 成功'})
        else:
            return JsonResponse({'status': 'error', 'message': '卡号为空'})
    return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

def view_bluetooth_data(request):
    bluetooth_data = BluetoothData.objects.all()
    return render(request, 'bluetooth_data.html', {'bluetooth_data': bluetooth_data})
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import BluetoothData, Employee

# @csrf_exempt
# def save_bluetooth_data(request):
#     if request.method == 'POST':
#         card_number = request.POST.get('card_number')
#         if card_number:
#             # 去除卡号的空格和特殊字符
#             normalized_card_number = ''.join(filter(str.isalnum, card_number))

#             # 检查卡号是否在员工表中存在
#             if normalized_card_number == "非法卡" or not Employee.objects.filter(card_number=normalized_card_number).exists():
#                 return JsonResponse({'status': 'error', 'message': '无效的卡号'})

#             # 查找最近的相同卡号的刷卡记录
#             existing_entry = BluetoothData.objects.filter(card_number=normalized_card_number).order_by('-timestamp').first()

#             # 确定是打卡还是签退
#             if existing_entry and existing_entry.status == '打卡':
#                 status = '签退'
#             else:
#                 status = '打卡'

#             # 创建新的记录
#             BluetoothData.objects.create(card_number=normalized_card_number, status=status)
#             return JsonResponse({'status': 'success', 'message': f'{status} 成功'})
#         else:
#             return JsonResponse({'status': 'error', 'message': '卡号为空'})
#     return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

# def view_bluetooth_data(request):
#     bluetooth_data = BluetoothData.objects.all()
#     for data in bluetooth_data:
#         if data.card_number.strip() == "":
#             data.card_number = "非法卡"
#     return render(request, 'bluetooth_data.html', {'bluetooth_data': bluetooth_data})

