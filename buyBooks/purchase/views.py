from django.shortcuts import render, redirect
import requests
import ssl
import urllib3

def purchase_view(request):
    print(ssl.OPENSSL_VERSION)
    print("purchase_view() 작동. purchase.html로 넘어갑니다~")
    return render(request, 'purchase/purchase.html')


def purchase_action(request):
    print("나 보여? purchase_action() 작동")
    print(request.method) # POST 나온다. 

    if request.method == "POST":
        URL = 'https://open-api.kakaopay.com/online/v1/payment/ready'
        headers = {
            "Authorization": "SECRET_KEY " + "시크릿키", 
            "Content-Type": "application/json",  
        }
        params = {
            "cid": "TC0ONETIME",
            "partner_order_id": "1212",
            "partner_user_id": "wonjilee",
            "item_name": "초코파이",
            "quantity": "1",
            "total_amount": "2200",
            "vat_amount": "200",
            "tax_free_amount": "0",
            "approval_url": "/purchase/success.html",
            "fail_url": "/purchase/failed.html",
            "cancel_url": "/purchase/cancel.html",
        }

        # Now use the session to make requests
        res = requests.post(URL, headers=headers, params=params, verify=False)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        print("뭐가 나올까")   
        print(res.json()['tid'])
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

    return render(request, 'purchase/purchase.html')