import base64
import json
from http.client import HTTPSConnection
import uuid
from datetime import datetime
from errors_list import errors_en

from .classess import Company, Transaction, CustomerPurchase, \
    CustomerPurchaseCalc, Customer, LoyaltyProgramSettings, MembershipTier, \
    ListMembershipTiers, Condition, CustomerShortInfo, TotalCashSpent, \
    EffectiveInvitedCount, CashierShortInfo, BranchShortInfo, Participant, \
    Item, GoodsOffer, Category, VaryingItem, GoodsInventory, ListVariants, \
    Order, DeliveryType, OnlinePayment, PaymentMethod, ListOrderItems, \
    DeliveryTypes, DeliveryCase, Response, Error, Voucher, ImageUploadUrl


# Функция возвращает целое число или None
# The function returns an integer or None
def int_or_none(x, default=None):
    if x in ('', 'None', None):
        return default
    return int(x)


# Функция заменяет None на пустое значение
# The function replaces None with an empty value
def str_parse(x):
    if str(x) in ('', 'None', None):
        x = ''
    return str(x)


# Функция удаляет лишние символы с номере телефона
# The function removes unnecessary characters from the phone number
def phone_optimization(phone, default=None):
    if phone in ('', 'None', None):
        return default
    phone = ''.join(str(phone).split())
    phone = phone.replace('-', '')
    phone = phone.replace('=', '')
    phone = phone.replace('(', '')
    phone = phone.replace(')', '')
    return str(phone)


# Функция удаляет лишние символы в номере телефона и заменяет символ '+' на %2b
# The function removes extra characters in the phone number and replaces the '+' character with% 2b
def phone_optimization_find(phone, default=None):
    if phone in ('', 'None', None):
        return default
    phone = phone_optimization(phone)
    phone = phone.replace('+', '%2b')
    return str(phone)


# Функция удаляет пробелы и заменяет "," на "." в цене
# The function removes spaces and replaces "," on "."
def decimal_or_none(x, default=None):
    if x in ('', 'None', None):
        return default
    x = ''.join(
        str(x).split())
    x = float(x.replace(',', '.'))
    x = round(x, 2)
    return str(x)


# Функция кодирует ID компании и API Key для авторизации Basic Auth
# Function encodes company ID and API Key for Basic Auth authorization
def partner_auth(company_id: str, api_key: str):
    base64_message = str(company_id) + ':' + str(api_key)
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64encode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message


# Функция для получения настроек компании
# Function for getting company settings
def company(company_id: str or int, api_key: str):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/settings',
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        company_info = Company(

            id=response_data['id'],
            name=response_data['name'],
            promo_code=response_data.get('promoCode'),
            currency=response_data.get('currency'),
            base_discount_policy=response_data.get('baseDiscountPolicy'),
            purchase_by_phone=response_data.get('purchaseByPhone'),
            write_invoice=response_data.get('writeInvoice'),
            burn_points_on_purchase=response_data.get('burnPointsOnPurchase'),
            burn_points_on_price=response_data.get(
                'burnPointsOnPricelist'),
            slug=response_data.get('slug'),

            loyalty_program_settings=LoyaltyProgramSettings(
                max_scores_discount=response_data.get(
                    'loyaltyProgramSettings').get('maxScoresDiscount'),
                referral_cashback_rates=response_data.get(
                    'loyaltyProgramSettings').get('referralCashbackRates'),
                cashier_award=response_data.get('loyaltyProgramSettings').get(
                    'cashierAward'),
                referral_reward=response_data.get(
                    'loyaltyProgramSettings').get(
                    'referralReward'),
                receipt_limit=response_data.get('loyaltyProgramSettings').get(
                    'receiptLimit'),
                defer_points_for_days=response_data.get(
                    'loyaltyProgramSettings').get('deferPointsForDays'),

                base_membership_tier=MembershipTier(
                    uid=response_data.get('loyaltyProgramSettings').get(
                        'baseMembershipTier').get('uid'),
                    name=response_data.get('loyaltyProgramSettings').get(
                        'baseMembershipTier').get('name'),
                    rate=response_data.get('loyaltyProgramSettings').get(
                        'baseMembershipTier').get('rate'),
                    condition=Condition(total_cash_spent=response_data.get(
                        'loyaltyProgramSettings').get(
                        'baseMembershipTier').get('conditions').get(
                        'totalCashSpent'),
                        effective_invited_count=response_data.get(
                            'loyaltyProgramSettings').get(
                            'baseMembershipTier').get(
                            'conditions').get(
                            'effectiveInvitedCount'))
                ),
                membership_tiers=ListMembershipTiers(
                    *response_data.get('loyaltyProgramSettings').get(
                        'membershipTiers'))
            )
        )
        return response_info, company_info
    else:
        return response_info, "error"


# Запрос получения списка транзакций
# max - Ограничить количество результатов в ответе.
# Тип integer <= 50. Значение по умолчанию : 10
# cursor - Идентификатор для получения следующей пачки транзакций. Получается
# при каждом следующем запросе.
# Тип string. Значение по умолчанию: None
# Request to get a list of transactions
# max - Limit number of results in response.
# Type integer <= 50. Default: 10
# cursor - Identifier for getting the next batch of transactions.
# It is obtained with every next request.
# Type string. Default value: None
def transactions_list(company_id: str, api_key: str, max: int = 10,
                      cursor: str = None):
    auth = partner_auth(company_id, api_key)
    try:
        params = 'max=' + str_parse(max) + '&cursor=' + str_parse(
            cursor)
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/operations?' + params,
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    transactionList = list()
    if response.status == 200:
        for transaction in response_data['rows']:
            transaction_info = Transaction(
                id=transaction['id'],
                date_created=transaction.get('dateCreated'),
                action=transaction.get('action'),
                state=transaction.get('state'),
                customer=CustomerShortInfo(
                    id=transaction.get('customer').get('id'),
                    display_name=transaction.get('customer').get(
                        'displayName'),
                    uid=transaction.get('customer').get('uid'),
                    membership_tier=MembershipTier(
                        uid=transaction.get('customer').get(
                            'membershipTier').get('uid'),
                        name=transaction.get('customer').get(
                            'membershipTier').get('name'),
                        rate=transaction.get('customer').get(
                            'membershipTier').get('rate'),
                        condition=Condition(total_cash_spent=TotalCashSpent(
                            target=transaction.get('customer').get(
                                'membershipTier').get('conditions').get(
                                'totalCashSpent').get(
                                'target')) if transaction.get(
                            'customer').get(
                            'membershipTier').get(
                            'conditions').get(
                            'totalCashSpent') else None,
                                            effective_invited_count=EffectiveInvitedCount(
                                                # target=None))
                                                target=transaction.get(
                                                    'customer').get(
                                                    'membershipTier').get(
                                                    'conditions').get(
                                                    'effectiveInvitedCount').get(
                                                    'target')) if transaction.get(
                                                'customer').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount') else None)

                        if transaction.get('customer').get(
                            'membershipTier').get(
                            'conditions') else None) if transaction.get(
                        'customer').get(
                        'membershipTier') else None) if transaction.get(
                    'customer') else None,
                cashier=CashierShortInfo(
                    id=transaction.get('cashier').get('id'),
                    display_name=transaction.get('cashier').get(
                        'displayName')) if transaction.get(
                    'cashier') else None,
                branch=BranchShortInfo(
                    id=transaction.get('branch').get('id'),
                    display_name=transaction.get('branch').get(
                        'displayName')) if transaction.get('branch') else None,
                points=transaction.get('point'),
                receipt_number=transaction.get('receiptNumber'),
                origin=transaction.get('origin'),
                total=transaction.get('total'),
                cash=transaction.get('cash')
            )
            transactionList.append(transaction_info)
        cursor = response_data['cursor']

        return response_info, transactionList, cursor
    else:
        return response_info, "error", None


#  Запрос на создание операции
# total - Сумма счета
# cash - Сумма оплаты деньгами
# points - Сумма оплаты бонусами
# code - Код на оплату
# uid - Идентификатор клиента в приложении
# phone - Номер телефона клиента
# nonce - Уникальный идентификатор операции (UUID)
# externalId - Внешний идентификатор кассира. ExternalId может состоять
# только из цифр и латинских букв.
# name - Имя кассира
# number - Номер чека
# skipLoyaltyTotal - Сумма стоимости товаров, на которую не должны
# начисляться бонусы
# Request to create an operation
# total - Total bill amount (in currency units).
# cash - Bill amount (in currency units).
# points - Bill amount (in points).
# code - Code for payment
# uid - Customer UID in the UDS.
# phone - Customer phone number.
# nonce - Transaction unique identifier (UUID).
# externalId - External cashier identifier.
# name - Cashier name
# number - Bill number.
# skipLoyaltyTotal - A part of the bill amount for which cashback is not credited and to which the discount does not apply (in currency units).

def transaction_create(company_id: str, api_key: str, total: float,
                       cash: float, points: float, code: str = None,
                       uid: str = None, phone: str = None, nonce: str = None,
                       external_id: str = None, name: str = None,
                       number: str = None,
                       skip_loyalty_total: float = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/operations',
            body=json.dumps({
                "code": code,
                "participant": {
                    "uid": uid,
                    "phone": phone_optimization(phone)
                },
                "nonce": nonce,
                "cashier": {
                    "externalId": external_id,
                    "name": name
                },
                "receipt": {
                    "total": decimal_or_none(total, 0),
                    "cash": decimal_or_none(cash, 0),
                    "points": decimal_or_none(points, 0),
                    "number": number,
                    "skipLoyaltyTotal": skip_loyalty_total
                }
            }),

            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        transaction_info = Transaction(
            id=response_data['id'],
            date_created=response_data.get('dateCreated'),
            action=response_data.get('action'),
            state=response_data.get('state'),
            customer=CustomerShortInfo(
                id=response_data.get('customer').get('id'),
                display_name=response_data.get('customer').get('displayName'),
                uid=response_data.get('customer').get('uid'),
                membership_tier=MembershipTier(
                    uid=response_data.get('customer').get(
                        'membershipTier').get('uid'),
                    name=response_data.get('customer').get(
                        'membershipTier').get('name'),
                    rate=response_data.get('customer').get(
                        'membershipTier').get('rate'),
                    condition=Condition(total_cash_spent=TotalCashSpent(
                        target=response_data.get('customer').get(
                            'membershipTier').get('conditions').get(
                            'totalCashSpent').get(
                            'target')) if response_data.get('customer').get(
                        'membershipTier').get('conditions').get(
                        'totalCashSpent') else None,
                                        effective_invited_count=EffectiveInvitedCount(
                                            target=response_data.get(
                                                'customer').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount').get(
                                                'target')) if response_data.get(
                                            'customer').get(
                                            'membershipTier').get(
                                            'conditions').get(
                                            'effectiveInvitedCount') else None,
                                        )
                    if response_data.get('customer').get('membershipTier').get(
                        'conditions') else None) if response_data.get(
                    'customer').get(
                    'membershipTier') else None) if response_data.get(
                'customer') else None,
            cashier=CashierShortInfo(id=response_data.get('cashier').get('id'),
                                     display_name=response_data.get(
                                         'cashier').get(
                                         'displayName')) if response_data.get(
                'cashier') else None,
            branch=BranchShortInfo(
                id=response_data.get('branch').get('id'),
                display_name=response_data.get('branch').get(
                    'displayName')) if response_data.get('branch') else None,
            points=response_data.get('point'),
            receipt_number=response_data.get('receiptNumber'),
            origin=response_data.get('origin'),
            total=response_data.get('total'),
            cash=response_data.get('cash')
        )

        return response_info, transaction_info
    else:
        return response_info, "error"


# Запрос информации об операции
# operationId - Идентификатор операции в UDS
# Request information about the transaction
# operationId -Transaction ID in the UDS
def transaction_get(company_id, api_key, operation_id):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app')
        con.request(
            method='GET',
            url='/partner/v2/operations/' + str(operation_id),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        transaction_info = Transaction(
            id=response_data['id'],
            date_created=response_data.get('dateCreated'),
            action=response_data.get('action'),
            state=response_data.get('state'),
            customer=CustomerShortInfo(
                id=response_data.get('customer').get('id'),
                display_name=response_data.get('customer').get('displayName'),
                uid=response_data.get('customer').get('uid'),
                membership_tier=MembershipTier(
                    uid=response_data.get('customer').get(
                        'membershipTier').get('uid'),
                    name=response_data.get('customer').get(
                        'membershipTier').get('name'),
                    rate=response_data.get('customer').get(
                        'membershipTier').get('rate'),
                    condition=Condition(total_cash_spent=TotalCashSpent(
                        target=response_data.get('customer').get(
                            'membershipTier').get('conditions').get(
                            'totalCashSpent').get(
                            'target')) if response_data.get('customer').get(
                        'membershipTier').get('conditions').get(
                        'totalCashSpent') else None,
                                        effective_invited_count=EffectiveInvitedCount(
                                            target=response_data.get(
                                                'customer').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount').get(
                                                'target')) if response_data.get(
                                            'customer').get(
                                            'membershipTier').get(
                                            'conditions').get(
                                            'effectiveInvitedCount') else None)
                    if response_data.get('customer').get('membershipTier').get(
                        'conditions') else None) if response_data.get(
                    'customer').get(
                    'membershipTier') else None) if response_data.get(
                'customer') else None,
            cashier=CashierShortInfo(id=response_data.get('cashier').get('id'),
                                     display_name=response_data.get(
                                         'cashier').get(
                                         'displayName')) if response_data.get(
                'cashier') else None,
            branch=BranchShortInfo(
                id=response_data.get('branch').get('branch_id'),
                display_name=response_data.get('branch').get(
                    'branch_displayName')) if response_data.get(
                'branch') else None,
            points=response_data.get('point'),
            receipt_number=response_data.get('receiptNumber'),
            origin=response_data.get('origin'),
            total=response_data.get('total'),
            cash=response_data.get('cash')
        )

        return response_info, transaction_info
    else:
        return response_info, "error"


#  Запрос на создание возврата по операции
# Если в запросе не указать параметр partialAmount, то возврат будет сделан на всю сумму
#  operationId - Идентификатор операции в UDS, по которой нужно сделать возврат
#  partialAmount - Сумма, на которую производится возврат.
# Request to create a return for an transaction
# If parameter attribute partialAmount is set, refund will be partial, otherwise invocation of this method will cause full refund.
# operationId - ID of the transaction in UDS for which you want to make a return
# partialAmount - Refund amount.

def transaction_refund(company_id: str or int, api_key: str,
                       operation_id: str or int, partial_amount: float = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/operations/' + str(operation_id) + '/refund',
            body=json.dumps({
                'partialAmount': partial_amount
            }),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        transaction_info = Transaction(
            id=response_data['id'],
            date_created=response_data.get('dateCreated'),
            action=response_data.get('action'),
            state=response_data.get('state'),
            customer=CustomerShortInfo(
                id=response_data.get('customer').get('id'),
                display_name=response_data.get('customer').get('displayName'),
                uid=response_data.get('customer').get('uid'),
                membership_tier=MembershipTier(
                    uid=response_data.get('customer').get(
                        'membershipTier').get('uid'),
                    name=response_data.get('customer').get(
                        'membershipTier').get('name'),
                    rate=response_data.get('customer').get(
                        'membershipTier').get('rate'),
                    condition=Condition(total_cash_spent=TotalCashSpent(
                        target=response_data.get('customer').get(
                            'membershipTier').get('conditions').get(
                            'totalCashSpent').get(
                            'target')) if response_data.get('customer').get(
                        'membershipTier').get('conditions').get(
                        'totalCashSpent') else None,
                                        effective_invited_count=EffectiveInvitedCount(
                                            target=response_data.get(
                                                'customer').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount').get(
                                                'target')) if response_data.get(
                                            'customer').get(
                                            'membershipTier').get(
                                            'conditions').get(
                                            'effectiveInvitedCount') else None)
                    if response_data.get('customer').get(
                        'membershipTier').get(
                        'conditions') else None) if response_data.get(
                    'customer').get(
                    'membershipTier') else None) if response_data.get(
                'customer') else None,
            cashier=CashierShortInfo(id=response_data.get('cashier').get('id'),
                                     display_name=response_data.get(
                                         'cashier').get(
                                         'displayName')) if response_data.get(
                'cashier') else None,
            branch=BranchShortInfo(
                id=response_data.get('branch').get('branch_id'),
                display_name=response_data.get('branch').get(
                    'branch_displayName')) if response_data.get(
                'branch') else None,
            points=response_data.get('point'),
            receipt_number=response_data.get('receiptNumber'),
            origin=response_data.get('origin'),
            total=response_data.get('total'),
            cash=response_data.get('cash')
        )

        return response_info, transaction_info
    else:

        return response_info, "error"


# Запрос информации по сумме к оплате деньгами с учетом списываемых баллов
# total - Сумма счета
# points - Сумма оплаты бонусами
# code - Код на оплату
# uid - Идентификатор клиента в UDS
# phone - Номер телефона клиента
# skipLoyaltyTotal - Сумма товаров, на которую не должны начисляться бонусы
# Request information on the amount to be paid with money, taking into account the points deducted
# total - Total bill amount without discount.
# points - Number of points to be redeemed (maximum available number of points by default).
# code - Code for payment
# uid - Customer UID in the UDS
# phone - Customer phone number
# skipLoyaltyTotal - A part of the bill amount for which cashback is not credited and to which the discount does not apply (in currency units).
def transaction_calc(company_id: str or int, api_key: str, total: int,
                     code: str or int = None, uid: str = None,
                     phone: str = None, points: float = None,
                     skip_loyalty_total: float = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/operations/calc',
            body=json.dumps({
                'code': code,
                'participant': {
                    'uid': uid,
                    'phone': phone_optimization(phone)
                },
                'receipt': {
                    'total': decimal_or_none(total, 0),
                    'points': decimal_or_none(points, 0),
                    'skipLoyaltyTotal': skip_loyalty_total
                }
            }),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        transaction_info = CustomerPurchaseCalc(
            user=Customer(
                uid=response_data.get('user').get('uid'),
                avatar=response_data.get('user').get('avatar'),
                display_name=response_data.get('user').get('displayName'),
                gender=response_data.get('user').get('gender'),
                phone=response_data.get('user').get('phone'),
                birth_date=response_data.get('user').get('birthDate'),
                channel_name=response_data.get('user').get('channelName'),
                participant=Participant(
                    id=response_data.get('user').get('participant').get(
                        'id'),
                    inviter_id=response_data.get('user').get(
                        'participant').get(
                        'inviterId'),
                    points=response_data.get('user').get('participant').get(
                        'points'),
                    discount_rate=response_data.get('user').get(
                        'participant').get(
                        'discountRate'),
                    cashback_rate=response_data.get('user').get(
                        'participant').get(
                        'cashbackRate'),
                    membership_tier=MembershipTier(
                        uid=response_data.get('user').get(
                            'participant').get('membershipTier').get('uid'),
                        name=response_data.get('user').get(
                            'participant').get('membershipTier').get('name'),
                        rate=response_data.get('user').get(
                            'participant').get('membershipTier').get('rate'),
                        condition=Condition(total_cash_spent=TotalCashSpent(
                            target=response_data.get('user').get(
                                'participant').get('membershipTier').get(
                                'conditions').get('totalCashSpent').get(
                                'target')),
                            effective_invited_count=EffectiveInvitedCount(
                                target=response_data.get(
                                    'user').get('participant').get(
                                    'membershipTier').get(
                                    'conditions').get(
                                    'effectiveInvitedCount').get(
                                    'target')) if response_data.get(
                                'user').get('participant').get(
                                'membershipTier').get(
                                'conditions').get(
                                'effectiveInvitedCount') else None) if response_data.get(
                            'user').get('participant').get(
                            'membershipTier').get(
                            'conditions') else None) if response_data.get(
                        'user').get('participant').get(
                        'membershipTier') else None,
                    date_created=response_data.get('user').get(
                        'participant').get('dateCreated'),
                    last_transaction_time=response_data.get('user').get(
                        'participant').get(
                        'lastTransactionTime')) if response_data.get(
                    'user').get('participant') else None
            ) if response_data.get('user') else None,
            code=response_data.get('code') if response_data.get(
                'code') else None,
            purchase=CustomerPurchase(
                max_points=response_data.get('purchase').get('maxPoints'),
                total=response_data.get('purchase').get('total'),
                skip_loyalty_total=response_data.get('purchase').get(
                    'skipLoyaltyTotal'),
                discount_amount=response_data.get('purchase').get(
                    'discountAmount'),
                discount_percent=response_data.get('purchase').get(
                    'discountPercent'),
                points=response_data.get('purchase').get('points'),
                points_percent=response_data.get('purchase').get(
                    'pointsPercent'),
                net_discount=response_data.get('purchase').get('netDiscount'),
                net_discount_percent=response_data.get('purchase').get(
                    'netDiscountPercent'),
                cash=response_data.get('purchase').get('cash'),
                cash_total=response_data.get('purchase').get('cashTotal'),
                cash_back=response_data.get('purchase').get('cashBack'),
                extras=response_data.get('purchase').get('extras')
            ) if response_data.get('purchase') else None
        )

        return response_info, transaction_info
    else:
        return response_info, "error"


# Запрос на начисления / списание бонусных баллов вручную
# points - количество бонусов к начислению / списанию. Для спмсания бонусов нужно передать отрицательное значение
# participantId - Идентификаторы клиентов в компании
# comment - Комментарий для клиента
# silent - Не отправлять пуш-уведомление клиенту
# Request for crediting / debiting bonus points manually
# points - Number of points.
# participantId - Customer ID in the company
# comment - Comment for the customer
# silent - Do not send a push notification to the customer

def transaction_reward(company_id: str, api_key: str, points: float,
                       participant_id: str or int,
                       comment: str = None,
                       silent: bool = False):
    auth = partner_auth(company_id, api_key)

    try:
        participantIdList = list()
        participantIdList.append(participant_id)
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/operations/reward',
            body=json.dumps({
                'comment': comment,
                'participants': participantIdList,
                'points': decimal_or_none(points),
                'silent': silent
            }),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 202:
        accepted = response_data.get('accepted')
        return response_info, accepted
    else:
        return response_info, "error"


# Запрос получения списка клиентов
# max - Ограничить количество результатов в ответе.
# Тип integer <= 50. Значение по умолчанию : 10
# offset - Количество строк, которое будет пропущено перед выводом результата.
# Тип integer <= 10000. Значение по умолчанию : 0
# Request to get a list of clients
# max - Limit the number of results in the response.
# Type integer <= 50. Default: 10
# offset - Rows count to skip.
# Type integer <= 10000. Default value: 0

def customers_list(company_id: str or int, api_key: str, max: int = 10,
                   offset: int = 0):
    auth = partner_auth(company_id, api_key)
    try:
        params = 'max=' + str_parse(max) + '&offset=' + str_parse(offset)
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/customers?' + params,
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    customerList = list()
    if response.status == 200:
        for customer in response_data['rows']:
            customer_info = Customer(
                uid=customer.get('uid'),
                avatar=customer.get('avatar'),
                display_name=customer.get('displayName'),
                gender=customer.get('gender'),
                phone=customer.get('phone'),
                birth_date=customer.get('birthDate'),
                channel_name=customer.get('channelName'),
                participant=Participant(
                    id=customer.get('participant').get(
                        'id'),
                    inviter_id=customer.get(
                        'participant').get(
                        'inviterId'),
                    points=customer.get('participant').get(
                        'points'),
                    discount_rate=customer.get(
                        'participant').get(
                        'discountRate'),
                    cashback_rate=customer.get(
                        'participant').get(
                        'cashbackRate'),
                    membership_tier=MembershipTier(
                        uid=customer.get(
                            'participant').get('membershipTier').get('uid'),
                        name=customer.get(
                            'participant').get('membershipTier').get('name'),
                        rate=customer.get(
                            'participant').get('membershipTier').get('rate'),
                        condition=Condition(total_cash_spent=TotalCashSpent(
                            target=customer.get(
                                'participant').get('membershipTier').get(
                                'conditions').get('totalCashSpent').get(
                                'target')) if customer.get('participant').get(
                            'membershipTier').get(
                            'conditions').get(
                            'totalCashSpent') else None,
                                            effective_invited_count=EffectiveInvitedCount(
                                                target=customer.get(
                                                    'participant').get(
                                                    'membershipTier').get(
                                                    'conditions').get(
                                                    'effectiveInvitedCount').get(
                                                    'target')) if customer.get(
                                                'participant').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount') else None) if customer.get(
                            'participant').get(
                            'membershipTier').get(
                            'conditions') else None) if customer.get(
                        'participant').get(
                        'membershipTier') else None,
                    date_created=customer.get(
                        'participant').get('dateCreated'),
                    last_transaction_time=customer.get(
                        'participant').get('lastTransactionTime')
                ) if customer.get('participant') else None
            )
            customerList.append(customer_info)

            return response_info, customerList
        else:
            return response_info, "error"


# Запрос на получение информации о клиенте по коду,номеру телефона или идентификатору.
# total - Сумма счета.
# code - Код на оплату.
# uid - Идентификатор клиента в приложении.
# phone - Номер телефона клиента.
# skipLoyaltyTotal - Сумма стоимости товаров, на которую не должны начисляться бонусы.
# exchangeCode - Запрос на получение кода клиента длительностью 24 часа (вместо 6 значного кода)
# Request to get information about the client by code, phone number or identifier.
# total -Total bill amount (in currency units).
# code - Code for payment.
# uid - Customer UID in the UDS.
# phone - Phone number in E164 format in url encoded, for example, +79123456789 need to send as %2b79123456789.
# skipLoyaltyTotal - A part of the bill amount for which cashback is not credited and to which the discount does not apply (in currency units).
# exchangeCode - Exchange existing payment promo code (if present in query) to a new long-term one.

def customer_find(company_id: str or int, api_key: str,
                  code: str or int = None, uid: str = None, phone: str = None,
                  total: float = None, skip_loyalty_total: float = None,
                  exchange_code: bool = True):
    auth = partner_auth(company_id, api_key)
    phone = phone_optimization_find(phone)
    code = str_parse(code)
    phone = str_parse(phone)
    uid = str_parse(uid)
    total = str_parse(total)
    skip_loyalty_total = str_parse(skip_loyalty_total)
    exchange_code = str_parse(exchange_code)
    try:
        params = "code=" + code + "&phone=" + phone + "&uid=" + uid + "&total=" \
                 + total + "&skipLoyaltyTotal=" + skip_loyalty_total + \
                 "&exchangeCode=" + exchange_code
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/customers/find?' + params,
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        customer_info = CustomerPurchaseCalc(
            user=Customer(
                uid=response_data.get('user').get('uid'),
                avatar=response_data.get('user').get('avatar'),
                display_name=response_data.get('user').get('displayName'),
                gender=response_data.get('user').get('gender'),
                phone=response_data.get('user').get('phone'),
                birth_date=response_data.get('user').get('birthDate'),
                channel_name=response_data.get('user').get('channelName'),
                participant=Participant(
                    id=response_data.get('user').get('participant').get(
                        'id'),
                    inviter_id=response_data.get('user').get(
                        'participant').get(
                        'inviterId'),
                    points=response_data.get('user').get('participant').get(
                        'points'),
                    discount_rate=response_data.get('user').get(
                        'participant').get(
                        'discountRate'),
                    cashback_rate=response_data.get('user').get(
                        'participant').get(
                        'cashbackRate'),
                    membership_tier=MembershipTier(
                        uid=response_data.get('user').get(
                            'participant').get('membershipTier').get('uid'),
                        name=response_data.get('user').get(
                            'participant').get('membershipTier').get('name'),
                        rate=response_data.get('user').get(
                            'participant').get('membershipTier').get('rate'),
                        condition=Condition(total_cash_spent=TotalCashSpent(
                            target=response_data.get('user').get(
                                'participant').get('membershipTier').get(
                                'conditions').get('totalCashSpent').get(
                                'target')),
                            effective_invited_count=EffectiveInvitedCount(
                                target=response_data.get(
                                    'user').get('participant').get(
                                    'membershipTier').get(
                                    'conditions').get(
                                    'effectiveInvitedCount').get(
                                    'target')) if response_data.get(
                                'user').get('participant').get(
                                'membershipTier').get(
                                'conditions').get(
                                'effectiveInvitedCount') else None)
                        if response_data.get(
                            'user').get('participant').get(
                            'membershipTier').get(
                            'conditions') else None) if response_data.get(
                        'user').get('participant').get(
                        'membershipTier') else None,
                    date_created=response_data.get('user').get(
                        'participant').get('dateCreated'),
                    last_transaction_time=response_data.get('user').get(
                        'participant').get('lastTransactionTime')
                ) if response_data.get(
                    'user').get('participant') else None
            ) if response_data.get('user') else None,
            code=response_data.get('code'),
            purchase=CustomerPurchase(
                max_points=response_data.get('purchase').get('maxPoints'),
                total=response_data.get('purchase').get('total'),
                skip_loyalty_total=response_data.get('purchase').get(
                    'skipLoyaltyTotal'),
                discount_amount=response_data.get('purchase').get(
                    'discountAmount'),
                discount_percent=response_data.get('purchase').get(
                    'discountPercent'),
                points=response_data.get('purchase').get('points'),
                points_percent=response_data.get('purchase').get(
                    'pointsPercent'),
                net_discount=response_data.get('purchase').get('netDiscount'),
                net_discount_percent=response_data.get('purchase').get(
                    'netDiscountPercent'),
                cash=response_data.get('purchase').get('cash'),
                cash_total=response_data.get('purchase').get('cashTotal'),
                cash_back=response_data.get('purchase').get('cashBack'),
                extras=response_data.get('purchase').get('extras')
            ) if response_data.get('purchase') else None
        )

        return response_info, customer_info
    else:
        return response_info, "error"


# Запрос информации о клиенте по ID в компании.
# participantId - ID клиента в компании.
# Request information about the customer by ID in the company.
# participantId - Customer ID in the company.

def customer_get(company_id: str or int, api_key: str,
                 participant_id: str or int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app')
        con.request(
            method='GET',
            url='/partner/v2/customers/' + str(participant_id),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        customer_info = Customer(
            uid=response_data.get('uid'),
            avatar=response_data.get('avatar'),
            display_name=response_data.get('displayName'),
            gender=response_data.get('gender'),
            phone=response_data.get('phone'),
            birth_date=response_data.get('birthDate'),
            channel_name=response_data.get('channelName'),
            participant=Participant(
                id=response_data.get('participant').get(
                    'id'),
                inviter_id=response_data.get(
                    'participant').get(
                    'inviterId'),
                points=response_data.get('participant').get(
                    'points'),
                discount_rate=response_data.get(
                    'participant').get(
                    'discountRate'),
                cashback_rate=response_data.get(
                    'participant').get(
                    'cashbackRate'),
                membership_tier=MembershipTier(
                    uid=response_data.get(
                        'participant').get('membershipTier').get('uid'),
                    name=response_data.get(
                        'participant').get('membershipTier').get('name'),
                    rate=response_data.get(
                        'participant').get('membershipTier').get('rate'),
                    condition=Condition(total_cash_spent=TotalCashSpent(
                        target=response_data.get(
                            'participant').get('membershipTier').get(
                            'conditions').get('totalCashSpent').get(
                            'target')) if response_data.get('participant').get(
                        'membershipTier').get(
                        'conditions').get(
                        'totalCashSpent') else None,
                                        effective_invited_count=EffectiveInvitedCount(
                                            target=response_data.get(
                                                'participant').get(
                                                'membershipTier').get(
                                                'conditions').get(
                                                'effectiveInvitedCount').get(
                                                'target')) if response_data.get(
                                            'participant').get(
                                            'membershipTier').get(
                                            'conditions').get(
                                            'effectiveInvitedCount') else None)
                    if response_data.get(
                        'participant').get(
                        'membershipTier').get(
                        'conditions') else None) if response_data.get(
                    'participant').get(
                    'membershipTier') else None,
                date_created=response_data.get(
                    'participant').get('dateCreated'),
                last_transaction_time=response_data.get(
                    'participant').get('lastTransactionTime')
            ) if response_data.get('participant') else None
        )

        return response_info, customer_info
    else:
        return response_info, "error"


# Запрос на получение ссылки для загрузки фотографии в UDS
# image_type - Тип содержимого файла для загрузки.
#  Generate image upload presigned url
# image_type - Image file content type.
def image_upload_url(company_id: str or int, api_key: str, image_type: str):

    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/image-upload-url',
            body=json.dumps({
                "contentType": "image/" + image_type
                }
            ),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        upload_info = ImageUploadUrl(image_id=response_data.get('imageId'),
                             headers=response_data.get('headers'),
                             url=response_data.get('url'),
                             method=response_data.get('method'),
                             expires=response_data.get('expires'))

        return response_info, upload_info
    else:
        return response_info, "error"

# Запрос для загрузки фотографии в UDS
# image_type - Тип содержимого файла для загрузки.
# image_name - Имя файла для загрузки с расширением.
# Image upload
# image_type - Image file content type.
# image_name - Full image name.
def image_upload(company_id: str or int, api_key: str,  image_type: str,
                 image_name: str):
    response_info, upload_info = image_upload_url(company_id=company_id,
                                                  api_key=api_key,
                                                  image_type=image_type)
    if response_info.status_code == 200:

        with open(image_name, 'rb') as file:
            image = file.read()
        image_id = upload_info.image_id
        upload_url = upload_info.url
        upload_method = upload_info.method
        upload_headers = upload_info.headers
        upload_headers_content = upload_headers.get('Content-Type')
        upload_headers_expect = upload_headers.get('Expect')
        upload_headers_host = upload_headers.get('Host')
        for upload_header_content in upload_headers_content:
            header_content = upload_header_content
        for upload_header_expect in upload_headers_expect:
            header_expect = upload_header_expect
        for upload_header_host in upload_headers_host:
            header_host = upload_header_host
        try:
            con = HTTPSConnection(upload_headers_host, timeout=180)
            con.request(
                method=upload_method,
                url=upload_url,
                body=image,
                headers={
                    'Content-Type': header_content,
                    'Expect': header_expect,
                    'Host': header_host,
                    'X-Origin-Request-Id': str(uuid.uuid4()),
                    'X-Timestamp': datetime.now().isoformat(),
                })
            response = con.getresponse()
            data = response.read()
            con.close()

        except Exception as e:
            response_info = Response(status_code=500,
                                     response_data='Error',
                                     response_headers=None,
                                     error_info=Error(
                                         error_code="HTTPError",
                                         error_message=str(e.args),
                                         error_description=errors_en[
                                             'HTTPError']))
            return response_info, "error"

        response_data = json.loads(data)
        response_info = Response(status_code=response.status,
                                 response_data=response_data,
                                 response_headers=response.headers,
                                 error_info=Error(
                                     error_code=response_data.get('errorCode'),
                                     error_message=response_data.get(
                                         'message'),
                                     error_description=errors_en[
                                         response_data.get('errorCode')])
                                 if (response.status != 200) or
                                    (response.status != 204) else None)

        if response.status == 200:
            return response_info, image_id
        else:
            return response_info, "error"



# Запрос получения списка товаров и категорий.
# max - Ограничить количество результатов в ответе. Тип integer <= 50. Значение по умолчанию: 10.
# offset - Количество строк, которое будет пропущено перед выводом результата. Тип integer <= 10000. Значение по умолчанию : 0
# node_id - Идентификатор категории в UDS. Для прсмотра товаров и категорий, вложенных в эту категорию.
# Request to get a list of products and categories.
# max - Limit the number of results in the response. Type integer <= 50. Default value: 10.
# offset - Rows count to skip. Type integer <= 10000. Default value: 0.
# node_id - Category ID in UDS. To view items and categories nested in this category.

def items_list(company_id: str or int, api_key: str, max: int = 10,
               offset: int = 0, node_id: int = None):
    auth = partner_auth(company_id, api_key)
    try:
        params = "max=" + str_parse(max) + "&offset=" + str_parse(offset) + \
                 "&node_id=" + str_parse(node_id)
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/goods?' + params,
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    itemList = list()
    if response.status == 200:
        for item in response_data['rows']:
            if item.get('data').get('type') == 'CATEGORY':
                item_info = Category(id=item.get('id'),
                                     name=item.get('name'),
                                     hidden=item.get('hidden'),
                                     blocked=item.get('blocked'),
                                     type=item.get('data').get('type'),
                                     external_id=item.get('externalId'))
                itemList.append(item_info)

            elif item.get('data').get('type') == 'ITEM':
                item_info = Item(id=item.get('id'),
                                 name=item.get('name'),
                                 hidden=item.get('hidden'),
                                 blocked=item.get('blocked'),
                                 type=item.get('data').get('type'),
                                 sku=item.get('data').get('sku'),
                                 price=item.get('data').get('price'),
                                 description=item.get('data').get(
                                     'description'),
                                 external_id=item.get('externalId'),
                                 photos=item.get('data').get('photos'),
                                 image_urls=item.get('imageUrls'),
                                 offer=GoodsOffer(
                                     offer_price=item.get('data').get(
                                         'offer').get('offerPrice'),
                                     skip_loyalty=item.get('data').get(
                                         'offer').get(
                                         'skipLoyalty')) if item.get(
                                     'data').get('offer') else None,
                                 inventory=GoodsInventory(
                                     in_stock=item.get('data').get(
                                         'inventory').get(
                                         'inStock')) if item.get('data').get(
                                     'inventory') else None
                                 )
                itemList.append(item_info)

            elif item.get('data').get('type') == 'VARYING_ITEM':
                item_info = VaryingItem(id=item.get('id'),
                                        name=item.get('name'),
                                        hidden=item.get('hidden'),
                                        blocked=item.get('blocked'),
                                        type=item.get('data').get('type'),
                                        description=item.get('data').get(
                                            'description'),
                                        external_id=item.get('externalId'),
                                        photos=item.get('data').get('photos'),
                                        image_urls=item.get('imageUrls'),
                                        variants=ListVariants(
                                            item.get('data'))
                                        )
                itemList.append(item_info)

            return response_info, itemList
        else:
            return response_info, "error"


# Запрос на создание категории.
# name - Название категории.
# node_id - Идентификатор категории в UDS, в которую будет вложена
# создаваемая категория. Тип integer.
# externalId - Внешний идентификатор категории. externalId может состоять
# только из цифр и латинских букв.
# Request to create a category.
# name - Category name.
# node_id - ID of the category in the UDS, which will be nested category to create. Integer type.
# externalId - External ID of the category. ExternalId can be
# only from numbers and Latin letters.

def create_category(company_id: str or int, api_key: str, name: str,
                    node_id: int = None, external_id: str = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/goods',
            body=json.dumps({
                'name': name,
                'node_id': node_id,
                'externalId': external_id,
                'data': {
                    'type': 'CATEGORY'
                }
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })

        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = Category(id=response_data.get('id'),
                             name=response_data.get('name'),
                             hidden=response_data.get('hidden'),
                             blocked=response_data.get('blocked'),
                             type=response_data.get('data').get('type'),
                             external_id=response_data.get('externalId'))

        return response_info, item_info
    else:
        return response_info, "error"


# Запрос на создание товара без вариантов.
# name - Название товара.
# price - Цена товара.
# node_id - Идентификатор категории в UDS, в которую будет вложена создаваемый
# товар.Тип integer.
# externalId - Внешний идентификатор товара. externalId может состоять
# только из цифр и латинских букв.
# description - Описание товара. Максимум 5000 символов.
# photos - Список идентификаторов изображений на сервере UDS.
# offerPrice - Цена товара по акции.
# skipLoyalty - Не применять бонусную программу к товару (False / True ).
# hidden - Скрыт ли товар.
# Request to create a product without options.
# name - Item name.
# price - Item price.
# node_id - ID of the category in the UDS, which will be nested
# commodity.Type integer.
# externalId - External ID of the item. ExternalId can be
# only from numbers and Latin letters
# description - Item description. Maximum 5000 characters.
# photos - List of image IDs on the UDS server.
# offerPrice - Item price for the promotion.
# skipLoyalty - Do not apply the bonus program to the item (False / True).
# hidden - Is the item hidden.

def create_item(company_id: str or int, api_key: str, name: str, price: float,
                node_id: int = None, external_id: str = None,
                description: str = None, photos: list = None,
                in_stock: int = None,
                offer_price: float = None, skip_loyalty: bool = None,
                hidden: bool = False):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/goods',
            body=json.dumps({
                'name': name,
                'nodeId': node_id,
                'externalId': external_id,
                'hidden': hidden,
                'data': {
                    'type': 'ITEM',
                    'price': decimal_or_none(price),
                    'description': description,
                    'photos': photos,
                    'inventory': {
                        'inStock': int_or_none(in_stock)
                    },
                    'offer': {
                        'offerPrice': decimal_or_none(offer_price),
                        'skipLoyalty': skip_loyalty
                    } if offer_price is not None and skip_loyalty is not None
                    else None
                }
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = Item(id=response_data.get('id'),
                         name=response_data.get('name'),
                         hidden=response_data.get('hidden'),
                         blocked=response_data.get('blocked'),
                         type=response_data.get('data').get('type'),
                         sku=response_data.get('data').get('sku'),
                         price=response_data.get('data').get('price'),
                         description=response_data.get('data').get(
                             'description'),
                         external_id=response_data.get('externalId'),
                         photos=response_data.get('data').get('photos'),
                         image_urls=response_data.get('imageUrls'),
                         offer=GoodsOffer(
                             offer_price=response_data.get('data').get(
                                 'offer').get(
                                 'offerPrice'),
                             skip_loyalty=response_data.get('data').get(
                                 'offer').get(
                                 'skipLoyalty')) if response_data.get(
                             'data').get('offer') else None,
                         inventory=GoodsInventory(
                             in_stock=response_data.get('data').get(
                                 'inventory').get(
                                 'inStock')) if response_data.get('data').get(
                             'inventory') else None)

        return response_info, item_info
    else:

        return response_info, "error"


# Запрос на создание товара с вариантами. Максимально количество вариантов - 10
# name - Название товара
# price - Цена товара
# node_id - Идентификатор категории в UDS, в которую будет вложена создаваемый товар.Тип integer
# externalId - Внешний идентификатор товара. externalId может состоять только из цифр и латинских букв
# description - Описание товара. Максимум 5000 символов
# variants - Список вариантов, состоящий из имени (name), артикула (sku) и цены (price)
# offer_variants - Список акционных вариантов, состоящий из имени (name), артикула (sku), цены(price), цены по акции (offerPrice)
# photos - Список идентификаторов изображений на сервере UDS.
# skipLoyalty - Не применять бонусную программу к товару (False / True )
# hidden - Скрыт ли товар
# Request to create a product with variants. Maximum number of options - 10.
# name - Item name.
# price - Item price.
# node_id - ID of the category in UDS, in which the created product will be attached. Type integer.
# externalId - External ID of the item. externalId can only consist of numbers and Latin letters.
# description - Item description. Maximum 5000 characters.
# variants - List of variants, consisting of name (name), SKU and price (price).
# photos - List of image IDs on the UDS server.
# offer_variants - A list of promotional options, consisting of name (name), article (sku), price (price), price of the offer (offerPrice)
# skipLoyalty - Do not apply the bonus program to the product (False / True).
# hidden - Is the goods hidden.

def create_varying_item(company_id: str or int, api_key: str, name: str,
                        price: float = None, node_id: int = None,
                        external_id: str = None, description: str = None,
                        variants: list = None, photos: list = None,
                        skip_loyalty: bool = None, hidden: bool = False):
    auth = partner_auth(company_id, api_key)

    try:
        goods_variants = []
        variants = variants or []
        for variant in variants:
            variant_data = variant.split(';')
            if len(variant_data) < 5:
                continue
            offer_price = decimal_or_none(variant_data[4])
            goods_variants.append({
                "name": str_parse(variant_data[0]),
                "price": decimal_or_none(variant_data[1]),
                "sku": str_parse(variant_data[2]),
                "inventory": {
                    "inStock": int_or_none(variant_data[3])
                },
                "offer": {
                    "offerPrice": decimal_or_none(offer_price),
                    "skipLoyalty": skip_loyalty
                } if offer_price is not None and skip_loyalty is not None else None
            })
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/goods',
            body=json.dumps({
                'name': name,
                'nodeId': node_id,
                'externalId': external_id,
                'hidden': hidden,
                'data': {
                    'type': 'VARYING_ITEM',
                    'price': decimal_or_none(price),
                    'description': description,
                    'photos': photos,
                    'variants': goods_variants
                }
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = VaryingItem(id=response_data.get('id'),
                                name=response_data.get('name'),
                                hidden=response_data.get('hidden'),
                                blocked=response_data.get('blocked'),
                                type=response_data.get('data').get('type'),
                                description=response_data.get('data').get(
                                    'description'),
                                external_id=response_data.get('externalId'),
                                photos=response_data.get('data').get('photos'),
                                image_urls=response_data.get('imageUrls'),
                                variants=ListVariants(
                                    response_data.get('data'))
                                )

        return response_info, item_info
    else:
        return response_info, "error"


# Запрос информации о товаре или категории
# goodsId -Идентификатор товара или категории. Тип integer
# Request information about a item or category
# goodsId - Item or category identifier. Integer type

def item_or_category_get(company_id: str or int, api_key: str, goods_id: int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/goods/' + str(goods_id),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })

        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        if response_data.get('data').get('type') == 'CATEGORY':
            item_info = Category(id=response_data.get('id'),
                                 name=response_data.get('name'),
                                 hidden=response_data.get('hidden'),
                                 blocked=response_data.get('blocked'),
                                 type=response_data.get('data').get('type'),
                                 external_id=response_data.get('externalId'))

            return response_info, item_info
        elif response_data.get('data').get('type') == 'ITEM':
            item_info = Item(id=response_data.get('id'),
                             name=response_data.get('name'),
                             hidden=response_data.get('hidden'),
                             blocked=response_data.get('blocked'),
                             type=response_data.get('data').get('type'),
                             sku=response_data.get('data').get('sku'),
                             price=response_data.get('data').get('price'),
                             description=response_data.get('data').get(
                                 'description'),
                             external_id=response_data.get('externalId'),
                             photos=response_data.get('data').get('photos'),
                             image_urls=response_data.get('imageUrls'),
                             offer=GoodsOffer(
                                 offer_price=response_data.get('data').get(
                                     'offer').get('offerPrice'),
                                 skip_loyalty=response_data.get('data').get(
                                     'offer').get(
                                     'skipLoyalty')) if response_data.get(
                                 'data').get('offer') else None,
                             inventory=GoodsInventory(
                                 in_stock=response_data.get('data').get(
                                     'inventory').get(
                                     'inStock')) if response_data.get(
                                 'data').get('inventory') else None
                             )

            return response_info, item_info
        elif response_data.get('data').get('type') == 'VARYING_ITEM':
            item_info = VaryingItem(id=response_data.get('id'),
                                    name=response_data.get('name'),
                                    hidden=response_data.get('hidden'),
                                    blocked=response_data.get('blocked'),
                                    type=response_data.get('data').get('type'),
                                    description=response_data.get('data').get(
                                        'description'),
                                    external_id=response_data.get(
                                        'externalId'),
                                    photos=response_data.get('data').get(
                                        'photos'),
                                    image_urls=response_data.get('imageUrls'),
                                    variants=ListVariants(
                                        response_data.get('data'))
                                    )

            return response_info, item_info

    else:
        return response_info, "error"


# Запрос на обновление информации о категории
# categoryId - Идентификатор категории в UDS. Тип integer
# name - Название категории
# node_id - Идентификатор категории в UDS, в которую будет вложена создаваемая категория. Тип integer
# externalId - Внешний идентификатор категории. externalId может состоять только из цифр и латинских букв.
# Request to update category information.
# categoryId - Category ID in UDS. Integer type.
# name - Category name.
# node_id - ID of the category in the UDS, in which the created category will be nested. Integer type.
# externalId - External ID of the category. ExternalId can only consist of numbers and Latin letters.

def update_category(company_id: str or int, api_key: str, category_id: int,
                    name: str, node_id: int = None,
                    external_id: str = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='PUT',
            url='/partner/v2/goods/' + str(category_id),
            body=json.dumps({
                'name': name,
                'nodeId': node_id,
                'externalId': external_id,
                'data': {
                    'type': 'CATEGORY'
                }
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = Category(id=response_data.get('id'),
                             name=response_data.get('name'),
                             hidden=response_data.get('hidden'),
                             blocked=response_data.get('blocked'),
                             type=response_data.get('data').get('type'),
                             external_id=response_data.get('externalId'))

        return response_info, item_info
    else:

        return response_info, "error"


# Запрос на обновление информации о товаре без вариантов
# itemId - Идентификатор товара в UDS. Тип integer
# name - Название товара
# price - Цена товара
# node_id - Идентификатор категории в UDS, в которую будет вложена создаваемый товар.Тип integer
# externalId - Внешний идентификатор товара. ExternalId может состоять только из цифр и латинских букв
# description - Описание товара. Максимум 5000 символов
# offerPrice - Цена товара по акции
# skipLoyalty - Не применять бонусную программу к товару (False / True )
# hidden - Скрыт ли товар
# Request to update product information without options
# itemId - Product ID in UDS. Integer type
# name - Product name
# price - Product price
# node_id - ID of the category in UDS, in which the created product will be attached. Type integer
# externalId - External ID of the item. ExternalId can only consist of numbers and Latin letters
# description - Item description. Maximum 5000 characters
# offerPrice - Item price for the promotion
# skipLoyalty - Do not apply the bonus program to the product (False / True)
# hidden - Is the item hidden.

def update_item(company_id: str or int, api_key: str, item_id: int, name: str,
                price: float, node_id: int = None,
                external_id: str = None, description: str = None,
                in_stock: int = None,
                offer_price: float = None,
                skip_loyalty: bool = None,
                hidden: bool = False):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='PUT',
            url='/partner/v2/goods/' + str(item_id),
            body=json.dumps({
                'name': name,
                'nodeId': node_id,
                'externalId': external_id,
                'hidden': hidden,
                'data': {
                    'type': 'ITEM',
                    'price': decimal_or_none(price),
                    'description': description,
                    'inventory': {
                        'inStock': int_or_none(in_stock)
                    },
                    'offer': {
                        'offerPrice': decimal_or_none(offer_price),
                        'skipLoyalty': skip_loyalty
                    }
                }
            }
            ),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = Item(id=response_data.get('id'),
                         name=response_data.get('name'),
                         hidden=response_data.get('hidden'),
                         blocked=response_data.get('blocked'),
                         type=response_data.get('data').get('type'),
                         sku=response_data.get('data').get('sku'),
                         price=response_data.get('data').get('price'),
                         description=response_data.get('data').get(
                             'description'),
                         external_id=response_data.get('externalId'),
                         photos=response_data.get('data').get('photos'),
                         image_urls=response_data.get('imageUrls'),
                         offer=GoodsOffer(
                             offer_price=response_data.get('data').get(
                                 'offer').get(
                                 'offerPrice'),
                             skip_loyalty=response_data.get('data').get(
                                 'offer').get(
                                 'skipLoyalty')) if response_data.get(
                             'data').get('offer') else None,
                         inventory=GoodsInventory(
                             in_stock=response_data.get('data').get(
                                 'inventory').get(
                                 'inStock')) if response_data.get('data').get(
                             'inventory') else None)

        return response_info, item_info
    else:
        return response_info, "error"


# Запрос на обновление информации товара с вариантами. Максимально количество вариантов - 10
# itemId - Идентификатор товара в UDS. Тип integer
# name - Название товара
# price - Цена товара
# node_id - Идентификатор категории в UDS, в которую будет вложена создаваемый товар.Тип integer
# externalId - Внешний идентификатор категории. externalId может состоять только из цифр и латинских букв
# description - Описание товара. Максимум 5000 символов
# variants - Список вариантов, состоящий из имени (name), артикула (sku) и цены (price)
# offer_variants - Список акционных вариантов, состоящий из имени (name), артикула (sku), цены(price), цены по акции (offerPrice)
# skipLoyalty - Не применять бонусную программу к товару (False / True )
# hidden - Скрыт ли товар
# Request to update product information with options. Maximum number of options - 10.
# itemId - Product ID in UDS. Integer type.
# name - Item name.
# price - Item price.
# node_id - ID of the category in UDS, in which the created product will be attached. Type integer.
# externalId - External ID of the item. externalId can only consist of numbers and Latin letters.
# description - Item description. Maximum 5000 characters.
# variants - List of variants, consisting of name (name), SKU and price (price).
# offer_variants - A list of promotional options, consisting of name (name), article (sku), price (price), price of the offer (offerPrice)
# skipLoyalty - Do not apply the bonus program to the product (False / True).
# hidden - Is the item hidden.

def update_varying_item(company_id: str or int, api_key: str, item_id: int,
                        name: str, price: float = None,
                        node_id: int = None,
                        external_id: str = None, description: str = None,
                        variants: list = None,
                        skip_loyalty=None,
                        hidden=False):
    auth = partner_auth(company_id, api_key)

    try:
        variants = variants or []
        goods_variants = []
        for variant in variants:
            variant_data = variant.split(';')
            if len(variant_data) < 5:
                continue
            offer_price = decimal_or_none(variant_data[4])
            goods_variants.append({
                "name": str_parse(variant_data[0]),
                "price": decimal_or_none(variant_data[1]),
                "sku": str_parse(variant_data[2]),
                "inventory": {
                    "inStock": int_or_none(variant_data[3])
                },
                "offer": {
                    "offerPrice": offer_price,
                    "skipLoyalty": skip_loyalty
                } if offer_price is not None and skip_loyalty is not None else None
            })
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='PUT',
            url='/partner/v2/goods/' + str(item_id),
            body=json.dumps({
                'name': name,
                'nodeId': node_id,
                'externalId': external_id,
                'hidden': hidden,
                'data': {
                    'type': 'VARYING_ITEM',
                    'price': decimal_or_none(price),
                    'description': description,
                    'variants': goods_variants
                }
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        item_info = VaryingItem(id=response_data.get('id'),
                                name=response_data.get('name'),
                                hidden=response_data.get('hidden'),
                                blocked=response_data.get('blocked'),
                                type=response_data.get('data').get('type'),
                                description=response_data.get('data').get(
                                    'description'),
                                external_id=response_data.get('externalId'),
                                photos=response_data.get('data').get('photos'),
                                image_urls=response_data.get('imageUrls'),
                                variants=ListVariants(
                                    response_data.get('data'))
                                )

        return response_info, item_info
    else:
        return response_info, "error"


# Запрос на удаление товара или категории.
#  goodsId - Идентификатор товара или категории в UDS. Тип integer.
# Request to remove a item or category.
# goodsId - The identifier of a item or category in UDS. Integer type.
def delete_item_or_category(company_id: str or int, api_key: str,
                            goods_id: int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='DELETE',
            url='/partner/v2/goods/' + str(goods_id),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    if response.status == 204:
        response_data = None
    else:
        response_data = json.loads(data)

    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if response_data is not None else None)
    if response.status == 204:
        return response_info, response.status
    else:
        return response_info, "error"


# Запрос информации о заказе.
# orderId - Идентификатор заказа в UDS.Тип Integer.
# Request order information.
# orderId - Order ID in UDS. Type Integer.

def order_get(company_id: str or int, api_key: str, order_id: int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='GET',
            url='/partner/v2/goods-orders/' + str(order_id),
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        order_info = Order(id=response_data.get('id'),
                           date_created=response_data.get('dateCreated'),
                           comment=response_data.get('comment'),
                           state=response_data.get('state'),
                           cash=response_data.get('cash'),
                           points=response_data.get('points'),
                           total=response_data.get('total'),
                           certificate_points=response_data.get(
                               'certificatePoints'),
                           customer=CustomerShortInfo(
                               id=response_data.get('customer').get('id'),
                               display_name=response_data.get('customer').get(
                                   'displayName'),
                               uid=response_data.get('customer').get('uid'),
                               membership_tier=MembershipTier(
                                   uid=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'uid'),
                                   name=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'name'),
                                   rate=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'rate'),
                                   condition=Condition(
                                       total_cash_spent=TotalCashSpent(
                                           target=response_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'totalCashSpent').get(
                                               'target')) if response_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'totalCashSpent').get(
                                           'target') else None,
                                       effective_invited_count=EffectiveInvitedCount(
                                           target=response_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'effectiveInvitedCount').get(
                                               'target')) if response_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'effectiveInvitedCount') else None) if response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'conditions') else None) if response_data.get(
                                   'customer').get(
                                   'membershipTier') else None) if response_data.get(
                               'customer') else None,

                           delivery=DeliveryType(
                               receiver_name=response_data.get('delivery').get(
                                   'receiverName'),
                               receiver_phone=response_data.get(
                                   'delivery').get('receiverPhone'),
                               user_comment=response_data.get('delivery').get(
                                   'userComment'),
                               type=DeliveryTypes(
                                   type=response_data.get('delivery').get(
                                       'type'),
                                   address=response_data.get('delivery').get(
                                       'address'),
                                   branch=BranchShortInfo(
                                       id=response_data.get('delivery').get(
                                           'branch').get('id'),
                                       display_name=response_data.get(
                                           'delivery').get('branch').get(
                                           'displayName')) if response_data.get(
                                       'delivery').get('branch') else None,
                                   delivery=DeliveryCase(
                                       name=response_data.get('delivery').get(
                                           'deliveryCase').get('name'),
                                       value=response_data.get('delivery').get(
                                           'deliveryCase').get(
                                           'value')) if response_data.get(
                                       'delivery').get(
                                       'deliveryCase') else None
                               ),
                           ) if response_data.get('delivery') else None,
                           online_payment=OnlinePayment(
                               payment_provider=response_data.get(
                                   'onlinePayment').get(
                                   'paymentProvider'),
                               id=response_data.get(
                                   'onlinePayment').get(
                                   'id'),
                               completed=response_data.get(
                                   'onlinePayment').get(
                                   'completed')) if response_data.get(
                               'onlinePayment') else None,
                           payment_method=PaymentMethod(type=response_data.get(
                               'paymentMethod').get(
                               'type'),
                               name=response_data.get(
                                   'paymentMethod').get(
                                   'name')) if response_data.get(
                               'paymentMethod') else None,
                           items=ListOrderItems(*response_data.get('items')))

        return response_info, order_info
    else:
        return response_info, "error"


# Запрос на обновление информации о заказе.
# orderId - Идентификатор заказа в UDS.Тип Integer.
# items - Список товаров из UDS, состоящий из идентификатора товара в UDS (id), варианта товара при наличии  (variantName) и количества (qty)
# new_items - Список товаров, состоящий из имени товара (name), цены товара (price), количества (qty), внешнего идентификатора товара (externalId) и параметра не применять бонусную программу (skipLoyalty (True / False))
# deliveryName - Название типа доставки.
# deliveryAmount - Стоимость доставки.
# Request to update order information.
# orderId - Order ID in UDS. Type Integer.
# items - A list of goods from UDS, consisting of a product identifier in UDS (id), product variant if available (variantName) and quantity (qty)
# new_items - List of products, consisting of product name (name), product price (price), quantity (qty), external product identifier (externalId) and the parameter do not apply the bonus program (skipLoyalty (True / False))
# deliveryName - Delivery name.
# deliveryAmount - Cost of delivery.

def update_order(company_id: str or int, api_key: str, order_id: int,
                 items: list = None, new_items: list = None,
                 delivery_name: str = None, delivery_amount: float = None):
    auth = partner_auth(company_id, api_key)
    try:
        goods = None
        if items or new_items:
            goods = []
            if items:
                for item in items:
                    item_data = item.split(';')
                    if len(item_data) < 3:
                        continue
                    qty = int_or_none(item_data[2])
                    goods.append({
                        'id': item_data[0],
                        'variantName': str_parse(item_data[1]),
                        'qty': qty
                    })

            if new_items:
                for new_item in new_items:
                    item_data = new_item.split(';')
                    if len(item_data) < 5:
                        continue
                    qty = int_or_none(item_data[2])
                    goods.append({
                        "name": str_parse(item_data[0]),
                        "price": item_data[1],
                        'qty': qty,
                        'externalId': str_parse(item_data[3]),
                        'skipLoyalty': item_data[4]
                    })
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='PUT',
            url='/partner/v2/goods-orders/' + str(order_id),
            body=json.dumps({
                'deliveryCase': {
                    'name': str_parse(delivery_name),
                    'value': str_parse(decimal_or_none(delivery_amount))
                } if delivery_name is not None and delivery_amount is not None else None,
                'items': goods if goods is not None else None
            }),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Accept-Charset': 'utf-8',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })

        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        order_info = Order(id=response_data.get('id'),
                           date_created=response_data.get('dateCreated'),
                           comment=response_data.get('comment'),
                           state=response_data.get('state'),
                           cash=response_data.get('cash'),
                           points=response_data.get('points'),
                           total=response_data.get('total'),
                           certificate_points=response_data.get(
                               'certificatePoints'),
                           customer=CustomerShortInfo(
                               id=response_data.get('customer').get('id'),
                               display_name=response_data.get('customer').get(
                                   'displayName'),
                               uid=response_data.get('customer').get('uid'),
                               membership_tier=MembershipTier(
                                   uid=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'uid'),
                                   name=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'name'),
                                   rate=response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'rate'),
                                   condition=Condition(
                                       total_cash_spent=TotalCashSpent(
                                           target=response_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'totalCashSpent').get(
                                               'target')) if response_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'totalCashSpent').get(
                                           'target') else None,
                                       effective_invited_count=EffectiveInvitedCount(
                                           target=response_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'effectiveInvitedCount').get(
                                               'target')) if response_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'effectiveInvitedCount') else None) if response_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'conditions') else None) if response_data.get(
                                   'customer').get(
                                   'membershipTier') else None) if response_data.get(
                               'customer') else None,

                           delivery=DeliveryType(
                               receiver_name=response_data.get('delivery').get(
                                   'receiverName'),
                               receiver_phone=response_data.get(
                                   'delivery').get('receiverPhone'),
                               user_comment=response_data.get('delivery').get(
                                   'userComment'),
                               type=DeliveryTypes(
                                   type=response_data.get('delivery').get(
                                       'type'),
                                   address=response_data.get('delivery').get(
                                       'address'),
                                   branch=BranchShortInfo(
                                       id=response_data.get('delivery').get(
                                           'branch').get('id'),
                                       display_name=response_data.get(
                                           'delivery').get('branch').get(
                                           'displayName')) if response_data.get(
                                       'delivery').get('branch') else None,
                                   delivery=DeliveryCase(
                                       name=response_data.get('delivery').get(
                                           'deliveryCase').get('name'),
                                       value=response_data.get('delivery').get(
                                           'deliveryCase').get(
                                           'value')) if response_data.get(
                                       'delivery').get(
                                       'deliveryCase') else None
                               ),
                           ) if response_data.get('delivery') else None,
                           online_payment=OnlinePayment(
                               payment_provider=response_data.get(
                                   'onlinePayment').get(
                                   'paymentProvider'),
                               id=response_data.get(
                                   'onlinePayment').get(
                                   'id'),
                               completed=response_data.get(
                                   'onlinePayment').get(
                                   'completed')) if response_data.get(
                               'onlinePayment') else None,
                           payment_method=PaymentMethod(type=response_data.get(
                               'paymentMethod').get(
                               'type'),
                               name=response_data.get(
                                   'paymentMethod').get(
                                   'name')) if response_data.get(
                               'paymentMethod') else None,
                           items=ListOrderItems(*response_data.get('items')))

        return response_info, order_info
    else:
        return response_info, "error"


# Запрос для закрытия заказа.
# orderId - Идентификатор заказа в UDS.Тип Integer.
# Request to complete an order.
# orderId - Order ID in UDS. Type Integer.

def complete_order(company_id: str or int, api_key: str, order_id: int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/goods-orders/' + str(order_id) + '/complete',
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            }
        )
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        transaction_id = response_data.get('transaction').get('id')
        order_data = response_data.get('order')
        order_info = Order(id=order_data.get('id'),
                           date_created=order_data.get('dateCreated'),
                           comment=order_data.get('comment'),
                           state=order_data.get('state'),
                           cash=order_data.get('cash'),
                           points=order_data.get('points'),
                           total=order_data.get('total'),
                           certificate_points=order_data.get(
                               'certificatePoints'),
                           customer=CustomerShortInfo(
                               id=order_data.get('customer').get('id'),
                               display_name=order_data.get('customer').get(
                                   'displayName'),
                               uid=order_data.get('customer').get('uid'),
                               membership_tier=MembershipTier(
                                   uid=order_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'uid'),
                                   name=order_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'name'),
                                   rate=order_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'rate'),
                                   condition=Condition(
                                       total_cash_spent=TotalCashSpent(
                                           target=order_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'totalCashSpent').get(
                                               'target')) if order_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'totalCashSpent').get(
                                           'target') else None,
                                       effective_invited_count=EffectiveInvitedCount(
                                           target=order_data.get(
                                               'customer').get(
                                               'membershipTier').get(
                                               'conditions').get(
                                               'effectiveInvitedCount').get(
                                               'target')) if order_data.get(
                                           'customer').get(
                                           'membershipTier').get(
                                           'conditions').get(
                                           'effectiveInvitedCount') else None) if order_data.get(
                                       'customer').get(
                                       'membershipTier').get(
                                       'conditions') else None) if order_data.get(
                                   'customer').get(
                                   'membershipTier') else None) if order_data.get(
                               'customer') else None,

                           delivery=DeliveryType(
                               receiver_name=order_data.get('delivery').get(
                                   'receiverName'),
                               receiver_phone=order_data.get(
                                   'delivery').get('receiverPhone'),
                               user_comment=order_data.get('delivery').get(
                                   'userComment'),
                               type=DeliveryTypes(
                                   type=order_data.get('delivery').get(
                                       'type'),
                                   address=order_data.get('delivery').get(
                                       'address'),
                                   branch=BranchShortInfo(
                                       id=order_data.get('delivery').get(
                                           'branch').get('id'),
                                       display_name=order_data.get(
                                           'delivery').get('branch').get(
                                           'displayName')) if order_data.get(
                                       'delivery').get('branch') else None,
                                   delivery=DeliveryCase(
                                       name=order_data.get('delivery').get(
                                           'deliveryCase').get('name'),
                                       value=order_data.get('delivery').get(
                                           'deliveryCase').get(
                                           'value')) if order_data.get(
                                       'delivery').get(
                                       'deliveryCase') else None
                               ),
                           ) if order_data.get('delivery') else None,
                           online_payment=OnlinePayment(
                               payment_provider=order_data.get(
                                   'onlinePayment').get(
                                   'paymentProvider'),
                               id=order_data.get(
                                   'onlinePayment').get(
                                   'id'),
                               completed=order_data.get(
                                   'onlinePayment').get(
                                   'completed')) if order_data.get(
                               'onlinePayment') else None,
                           payment_method=PaymentMethod(type=order_data.get(
                               'paymentMethod').get(
                               'type'),
                               name=order_data.get(
                                   'paymentMethod').get(
                                   'name')) if order_data.get(
                               'paymentMethod') else None,
                           items=ListOrderItems(*order_data.get('items')))

        return response_info, order_info, transaction_id
    else:
        return response_info, "error", "notFound"


# Запрос на создание кода клиента, по которому можно закрыть заказ.
# orderId - Идентификатор заказа в UDS.Тип Integer.
# Request to create a client code by which you can close the order.
# orderId - Order ID in UDS. Type Integer.

def generate_complete_order_code(company_id: str or int, api_key: str,
                                 order_id: int):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/goods-orders/' + str(order_id) + '/code',
            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            }
        )
        response = con.getresponse()
        data = response.read()
        con.close()

    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        code = response_data.get('code')
        return response_info, code
    else:

        return response_info, "error"


# Запрос на создание ваучера.
# code -Код ваучера UDS.
# qrCodeText - Информация о ваучере UDS для генерации QR-кода.
# qrCode128 - Ссылка для генерации изображения QR-кода (размер 128).
# qrCode256 - Ссылка для генерации изображения QR-кода (размер 256).
# expiresIn - Срок действия кода ваучера истекает в (часовой пояс UTC).
# points - Минимальное количество баллов для получения по ваучеру.
# Request to create a voucher.
# code	- UDS voucher code.
# qrCodeText - UDS voucher info for qrcode.
# qrCode128 - Link for generate qrcode image (size 128).
# qrCode256 - Link for generate qrcode image (size 256)
# expiresIn - Voucher code expires in (UTC time-zone).
# points - Minimum points for withdrawal.

def voucher_create(company_id: str or int, api_key: str, total: float,
                   nonce: str = None,
                   external_id: str = None, name: str = None,
                   number: str = None,
                   skip_loyalty_total: str = None):
    auth = partner_auth(company_id, api_key)
    try:
        con = HTTPSConnection('api.uds.app', timeout=60)
        con.request(
            method='POST',
            url='/partner/v2/operations/voucher',
            body=json.dumps({
                "nonce": nonce,
                "cashier": {
                    "externalId": external_id,
                    "name": name
                },
                "receipt": {
                    "total": decimal_or_none(total, 0),
                    "number": number,
                    "skipLoyaltyTotal": skip_loyalty_total
                }
            }),

            headers={
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'X-Origin-Request-Id': str(uuid.uuid4()),
                'X-Timestamp': datetime.now().isoformat(),
            })
        response = con.getresponse()
        data = response.read()
        con.close()
    except Exception as e:
        response_info = Response(status_code=500,
                                 response_data='Error',
                                 response_headers=None,
                                 error_info=Error(
                                     error_code="HTTPError",
                                     error_message=str(e.args),
                                     error_description=errors_en[
                                         'HTTPError']))
        return response_info, "error"

    response_data = json.loads(data)
    response_info = Response(status_code=response.status,
                             response_data=response_data,
                             response_headers=response.headers,
                             error_info=Error(
                                 error_code=response_data.get('errorCode'),
                                 error_message=response_data.get('message'),
                                 error_description=errors_en[
                                     response_data.get('errorCode')])
                             if (response.status != 200) or
                                (response.status != 204) else None)

    if response.status == 200:
        voucher_info = Voucher(
            code=response_data['code'],
            qr_code_text=response_data.get('qrCodeText'),
            qr_code_128=response_data.get('qrCode128'),
            qr_code_256=response_data.get('qrCode256'),
            expires_in=response_data.get('expiresIn'),
            points=response_data.get('points')
        )

        return response_info, voucher_info
    else:
        return response_info, "error"
