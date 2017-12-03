# DreamBox - API


**Endpoints**

## `GET` /oauth2/get/token

### Descrição
> Autentica o usuário com o openbanking do banco original utilizando o protocolo OAuth2.

### Response
> access_token

---

## `GET` /user/balance

### Descrição
> Retorna os saldos atuais do cliente.

### Response
> current_balance
> alguma coisa que eu não lembro
> current_limit

---

## `GET` /user/balance/rewards
> Retorna os pontos acumulados no Rewards.

### Response
> reward_balance

---

## `GET` /user/classify
> Classifica o cliente de acordo com seu histórico de saldos e transações.

### Response
> customer_category

---

## `POST` /user/canbuyproduct
> Verifica se o cliente pode comprar a um produto de acordo com seu saldo.

### Body
> product_url

### Response
> buy_status
> buy_classification

---

## `POST` /product/info
> Retorna informações sobre um produto.

### Body
> product_url

### Response
> product_value
> product_x
> product_monthly