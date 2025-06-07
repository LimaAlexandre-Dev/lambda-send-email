# 📨 Função Lambda: Envio de E-mail via Amazon SES

## 📋 Descrição
Esta função Lambda em Python envia um e-mail usando o serviço Amazon SES da AWS. É útil para notificações automáticas em aplicações serverless.

## 🚀 Como funciona
A função é acionada (por exemplo, via teste no console Lambda) e usa o `boto3` para enviar um e-mail pré-definido via SES.

## 🧾 Entrada e Saída
- **Entrada**: Evento genérico (pode ser vazio para testes).
- **Saída**: Mensagem de sucesso ou erro em formato JSON.

## 📦 Dependências
- `boto3` (já incluso nas Lambdas Python padrão da AWS)

## 🔧 Instruções de Execução
1. Verifique os e-mails no Amazon SES (origem e destino).
2. Cole o código na função Lambda.
3. Clique em **Testar** com um payload vazio `{}`.
4. Verifique a caixa de entrada.

## 🧪 Testes
Use o botão **Testar** no console Lambda para validar a execução.

## 🔒 Segurança
Certifique-se de que a função está em modo privado e que os e-mails foram verificados (modo sandbox limita destinatários).

## 🔗 Link Lambda
Informe o ARN da função aqui depois de criada.

## 🔗 Repositório GitHub
[https://github.com/seuusuario/lambda-send-email](https://github.com/seuusuario/lambda-send-email)
